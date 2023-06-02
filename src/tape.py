BLANK = "\\0"


class Tape:
    def __init__(self, tape: list[str]):
        self.tape: list[str] = tape
        self.head: int = 0

    def __len__(self) -> int:
        return len(self.tape)

    def __getitem__(self, index: int) -> str:
        if index < 0 or index >= len(self.tape):
            return BLANK
        return self.tape[index]

    def __setitem__(self, index: int, value: str) -> None:
        if index < 0:
            raise IndexError("Index out of range")
        if index >= len(self.tape):
            self.tape += [BLANK] * (index - len(self.tape) + 1)
        self.tape[index] = value

    def read(self) -> str:
        return self[self.head]

    def write(self, symbol: str) -> None:
        self[self.head] = symbol

    def move_head(self, direction: str) -> None:
        if direction == "R":
            self.head += 1
        elif direction == "L":
            self.head -= 1
        elif direction == "S":
            pass
