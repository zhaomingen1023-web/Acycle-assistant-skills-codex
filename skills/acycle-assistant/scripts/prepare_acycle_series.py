#!/usr/bin/env python3
"""Prepare a two-column Acycle-ready text series from tabular input."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize a table into a two-column numeric file for Acycle."
    )
    parser.add_argument("--input", required=True, help="Source CSV/TSV/TXT file")
    parser.add_argument("--output", required=True, help="Output text file")
    parser.add_argument(
        "--x",
        help="X column name or zero-based column index; defaults to first column",
    )
    parser.add_argument(
        "--y",
        help="Y column name or zero-based column index; defaults to second column",
    )
    parser.add_argument(
        "--delimiter",
        choices=["auto", "comma", "tab", "space", "semicolon"],
        default="auto",
        help="Input delimiter",
    )
    parser.add_argument(
        "--header",
        choices=["auto", "yes", "no"],
        default="auto",
        help="Whether the first row is a header",
    )
    parser.add_argument(
        "--output-delimiter",
        choices=["tab", "comma", "space"],
        default="tab",
        help="Delimiter for the output file",
    )
    parser.add_argument(
        "--sort",
        action="store_true",
        help="Sort rows ascending by x before writing",
    )
    parser.add_argument(
        "--deduplicate",
        choices=["error", "first", "last", "average"],
        default="error",
        help="How to handle duplicate x-values",
    )
    parser.add_argument(
        "--skiprows",
        type=int,
        default=0,
        help="Skip this many non-comment rows before parsing",
    )
    parser.add_argument(
        "--comment-prefix",
        default="#",
        help="Ignore lines starting with this prefix; empty disables comment handling",
    )
    parser.add_argument(
        "--on-invalid",
        choices=["skip", "error"],
        default="skip",
        help="How to handle rows with missing or non-numeric x/y values",
    )
    parser.add_argument(
        "--write-header",
        action="store_true",
        help="Write x and y column labels to the output file",
    )
    return parser.parse_args()


def infer_delimiter(lines: list[str], declared: str) -> str | None:
    if declared != "auto":
        return {
            "comma": ",",
            "tab": "\t",
            "space": None,
            "semicolon": ";",
        }[declared]

    sample = "\n".join(lines[:10])
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;")
        return dialect.delimiter
    except csv.Error:
        return None


def split_rows(lines: list[str], delimiter: str | None) -> list[list[str]]:
    if delimiter is None:
        return [line.split() for line in lines]
    return list(csv.reader(lines, delimiter=delimiter))


def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def infer_header(first_row: list[str], header_mode: str) -> bool:
    if header_mode == "yes":
        return True
    if header_mode == "no":
        return False
    return not all(is_number(cell.strip()) for cell in first_row)


def parse_column_ref(
    ref: str | None, default_index: int, header: list[str] | None
) -> tuple[int, str]:
    if ref is None:
        if header and default_index < len(header):
            return default_index, header[default_index].strip()
        return default_index, f"column_{default_index}"

    candidate = ref.strip()
    if candidate.isdigit():
        index = int(candidate)
        label = header[index].strip() if header and index < len(header) else f"column_{index}"
        return index, label

    if not header:
        raise ValueError(f"Column name '{candidate}' requires a header row.")

    normalized = {name.strip(): idx for idx, name in enumerate(header)}
    if candidate not in normalized:
        raise ValueError(
            f"Column '{candidate}' not found. Available columns: {', '.join(header)}"
        )
    return normalized[candidate], candidate


def deduplicate_rows(rows: list[tuple[float, float]], mode: str) -> tuple[list[tuple[float, float]], int]:
    buckets: defaultdict[float, list[float]] = defaultdict(list)
    for x_value, y_value in rows:
        buckets[x_value].append(y_value)

    duplicate_count = sum(1 for values in buckets.values() if len(values) > 1)
    if duplicate_count == 0:
        return rows, 0
    if mode == "error":
        raise ValueError("Duplicate x-values found. Re-run with --deduplicate.")

    result: list[tuple[float, float]] = []
    for x_value in sorted(buckets):
        values = buckets[x_value]
        if mode == "first":
            result.append((x_value, values[0]))
        elif mode == "last":
            result.append((x_value, values[-1]))
        else:
            result.append((x_value, mean(values)))
    return result, duplicate_count


def output_delimiter_token(name: str) -> str:
    return {"tab": "\t", "comma": ",", "space": " "}[name]


def main() -> int:
    args = parse_args()
    source = Path(args.input)
    target = Path(args.output)

    if not source.is_file():
        raise SystemExit(f"Input file not found: {source}")

    raw_lines = source.read_text(encoding="utf-8-sig").splitlines()
    filtered_lines: list[str] = []
    skipped_preface = 0
    for raw_line in raw_lines:
        stripped = raw_line.strip()
        if not stripped:
            continue
        if args.comment_prefix and stripped.startswith(args.comment_prefix):
            continue
        if skipped_preface < args.skiprows:
            skipped_preface += 1
            continue
        filtered_lines.append(raw_line)

    if not filtered_lines:
        raise SystemExit("No data rows remained after filtering.")

    delimiter = infer_delimiter(filtered_lines, args.delimiter)
    rows = split_rows(filtered_lines, delimiter)
    if not rows:
        raise SystemExit("No rows could be parsed from the input.")

    has_header = infer_header(rows[0], args.header)
    header = rows[0] if has_header else None
    data_rows = rows[1:] if has_header else rows

    x_index, x_label = parse_column_ref(args.x, 0, header)
    y_index, y_label = parse_column_ref(args.y, 1, header)

    parsed_rows: list[tuple[float, float]] = []
    invalid_count = 0
    for row_number, row in enumerate(data_rows, start=2 if has_header else 1):
        if max(x_index, y_index) >= len(row):
            invalid_count += 1
            if args.on_invalid == "error":
                raise SystemExit(f"Row {row_number} does not have enough columns.")
            continue
        x_raw = row[x_index].strip()
        y_raw = row[y_index].strip()
        try:
            parsed_rows.append((float(x_raw), float(y_raw)))
        except ValueError:
            invalid_count += 1
            if args.on_invalid == "error":
                raise SystemExit(
                    f"Row {row_number} contains non-numeric x/y values: {x_raw}, {y_raw}"
                )

    if not parsed_rows:
        raise SystemExit("No valid numeric rows remained after parsing.")

    sorted_before = parsed_rows == sorted(parsed_rows, key=lambda item: item[0])
    if args.sort:
        parsed_rows = sorted(parsed_rows, key=lambda item: item[0])

    parsed_rows, duplicate_groups = deduplicate_rows(parsed_rows, args.deduplicate)

    target.parent.mkdir(parents=True, exist_ok=True)
    token = output_delimiter_token(args.output_delimiter)
    with target.open("w", encoding="utf-8", newline="") as handle:
        if args.write_header:
            handle.write(f"{x_label}{token}{y_label}\n")
        for x_value, y_value in parsed_rows:
            handle.write(f"{x_value:g}{token}{y_value:g}\n")

    x_values = [row[0] for row in parsed_rows]
    min_x = min(x_values)
    max_x = max(x_values)
    spacing_text = "n/a"
    if len(x_values) > 1:
        spacings = [b - a for a, b in zip(x_values, x_values[1:])]
        spacing_text = f"{mean(spacings):g}"

    print(f"Input: {source}")
    print(f"Output: {target}")
    print(f"Rows written: {len(parsed_rows)}")
    print(f"Invalid rows skipped: {invalid_count}")
    print(f"Duplicate x groups handled: {duplicate_groups}")
    print(f"Header detected: {'yes' if has_header else 'no'}")
    print(f"Columns used: x={x_label}, y={y_label}")
    print(f"Sorted before write: {'yes' if args.sort or sorted_before else 'no'}")
    print(f"x range: {min_x:g} to {max_x:g}")
    print(f"Mean spacing: {spacing_text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
