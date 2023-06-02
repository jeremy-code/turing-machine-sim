from typing import Callable

from tape import Tape
from display import Display


class TuringMachine:
    def __init__(
        self,
        tapes: list[Tape],
        initial_state: str,
        final_state: str,
        transition_function: Callable[
            [str, list[str]], tuple[str, list[str], list[str]]
        ],
    ):
        self.tapes = tapes
        self.current_state = initial_state
        self.final_state = final_state
        self.transition_function = transition_function
        self.display = Display(tapes, initial_state)

    def update(self):
        self.display.update(self.tapes, self.current_state)

    def step(self) -> bool:
        current_symbols = [tape.read() for tape in self.tapes]
        self.current_state, new_symbols, directions = self.transition_function(
            self.current_state, current_symbols
        )

        for tape, symbol, direction in zip(self.tapes, new_symbols, directions):
            tape.write(symbol)
            tape.move_head(direction)

        self.update()

        return self.current_state == self.final_state
