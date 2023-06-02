from typing import List, Union
from rich.table import Table
from rich.layout import Layout
from rich.style import Style
from rich.padding import Padding
from rich.panel import Panel

from tape import Tape

ROW_STYLES: List[Union[Style, str]] = [
    Style(bold=True),
    Style(color="cyan", bold=True),
    Style(color="white"),
]


class Display:
    def __init__(self, tapes: list[Tape], initial_state: str):
        self.tapes = tapes

        self.current_state = initial_state

    def generate_display(self) -> Layout:
        layout = Layout()
        tables = [self.generate_table(tape) for tape in self.tapes]

        tape_info = "\n".join(
            [
                f"Tape {i}: Head position: {tape.head}, Current character: {tape.read()}"
                for i, tape in enumerate(self.tapes)
            ]
        )
        panel_text = f"Current state: {self.current_state}\n{tape_info}"
        tables.append(Panel(panel_text))

        layout.split_column(*tables)

        return layout

    def generate_table(self, tape: Tape) -> Table:
        table = Table(show_header=False, padding=(0, 2), row_styles=ROW_STYLES)
        head = tape.head

        arrow = Padding("⌄", (1, 0))
        table.add_row(*[arrow if i == head else " " for i in range(head + 1)])
        table.add_row(*map(str, range(len(tape))))
        table.add_row(*tape.tape)

        return table

    def update(self, tapes, current_state):
        self.tapes = tapes
        self.current_state = current_state
