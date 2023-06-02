import unittest

from tape import Tape
from turing_machine import TuringMachine


class TestTuringMachine(unittest.TestCase):
    def test_single_tape(self):
        # Test a Turing machine with a single tape
        tape = Tape(list("0010"))
        tm = TuringMachine(
            [tape],
            initial_state="q0",
            final_state="q1",
            transition_function=lambda state, symbols: (
                "q1",
                ["0"],
                ["R"],
            ),
        )
        self.assertTrue(tm.step())
        self.assertEqual(tape.read(), "0")

    def test_multiple_tapes(self):
        # Test a Turing machine with multiple tapes
        tape1 = Tape(list("0010"))
        tape2 = Tape(list("1011"))
        tm = TuringMachine(
            [tape1, tape2],
            initial_state="q0",
            final_state="q1",
            transition_function=lambda state, symbols: (
                "q1",
                ["0", "1"],
                ["R", "L"],
            ),
        )
        self.assertTrue(tm.step())
        self.assertEqual(tape1.read(), "0")
        self.assertEqual(tape2.read(), "\\0")

    def test_no_transition_function(self):
        # Test a Turing machine with no transition function
        tape = Tape(list("0010"))
        tm = TuringMachine(
            [tape],
            initial_state="q0",
            final_state="q1",
            transition_function=None,
        )
        with self.assertRaises(TypeError):
            tm.step()


if __name__ == "__main__":
    unittest.main()
