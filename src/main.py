import time
from rich.live import Live
from rich.prompt import Prompt

from tape import Tape
from turing_machine import TuringMachine

BLANK = "\\0"


def transition_function(
    state: str, symbols: list[str]
) -> tuple[str, list[str], list[str]]:
    symbol = symbols[0]

    if symbol.isalpha():
        match state:
            case "q0":
                return ("q1", [symbol, "b"], ["R", "R"])
            case "q1":
                return ("q2", [symbol, "r"], ["R", "R"])
            case "q2":
                return ("q3", [symbol, "u"], ["R", "R"])
            case "q3":
                return ("q4", [symbol, "h"], ["R", "R"])
            case "q4":
                return ("q4", [symbol, BLANK], ["R", "S"])
    elif symbol == " ":
        match state:
            case "q0":
                return ("q0", [" ", " "], ["R", "R"])
            case "q1":
                return ("q5", [" ", " "], ["S", "S"])
            case "q2":
                return ("q6", [" ", " "], ["S", "S"])
            case "q3":
                return ("q7", [" ", " "], ["S", "S"])
            case "q4":
                return ("q0", [" ", " "], ["R", "R"])
            case "q5":
                return ("q6", [" ", "r"], ["S", "R"])
            case "q6":
                return ("q7", [" ", "u"], ["S", "R"])
            case "q7":
                return ("q8", [" ", "h"], ["S", "R"])
            case "q8":
                return ("q4", [" ", " "], ["S", "S"])
    elif symbol == BLANK:
        match state:
            case "q0":
                return ("q_accept", [BLANK, BLANK], ["S", "S"])
            case "q1":
                return ("q2", [BLANK, "r"], ["S", "R"])
            case "q2":
                return ("q3", [BLANK, "u"], ["S", "R"])
            case "q3":
                return ("q4", [BLANK, "h"], ["S", "S"])
            case "q4":
                return ("q_accept", [BLANK, BLANK], ["S", "S"])
            case "q8":
                return ("q_accept", [BLANK, BLANK], ["S", "S"])


tape = list(Prompt.ask("Enter a string", default="Hello World"))

initial_state, final_state = "q0", "q_accept"
Tape1, Tape2 = Tape(tape), Tape([])

turing_machine = TuringMachine(
    [Tape1, Tape2],
    initial_state,
    final_state,
    transition_function,
)

with Live(refresh_per_second=4) as live:
    while True:
        live.update(turing_machine.display.generate_display())
        time.sleep(1)
        if turing_machine.step():
            break
