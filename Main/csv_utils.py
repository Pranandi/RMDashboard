from typing import Any, Iterable


FORMULA_PREFIXES = ('=', '+', '-', '@', '\t', '\r', '\n')


def sanitize_csv_value(value: Any) -> str:
    text = '' if value is None else str(value)
    if text.startswith(FORMULA_PREFIXES):
        return "'" + text
    return text


def write_csv_row(writer: Any, row: Iterable[Any]) -> None:
    writer.writerow([sanitize_csv_value(value) for value in row])