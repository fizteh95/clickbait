from tabulate import tabulate


def render_table(rows: list[dict], headers: list[str]) -> None:
    if not rows:
        print("(no data)")
        return
    table_data = [[row.get(h, "") for h in headers] for row in rows]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
