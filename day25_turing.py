import re
import sys

BEGIN_RE = re.compile("Begin in state (.*)\.")
DIAGNOSTIC_RE = re.compile("Perform a diagnostic checksum after (.*) steps\.")
IN_STATE_RE = re.compile("In state (.*):")
IF_RE = re.compile("  If the current value is (\d):")
WRITE_RE = re.compile("    - Write the value (\d)\.")
MOVE_RE = re.compile("    - Move one slot to the (.*)\.")
CONTINUE_RE = re.compile("    - Continue with state (.*)\.")

class TuringMachine:
    def __init__(self, start, states):
        self._tape = set()
        self._cursor = 0
        self._state = start
        self._states = states

    def step(self):
        write, move, state = self._states[self._state][
            self._cursor in self._tape]
        if write:
            self._tape.add(self._cursor)
        else:
            self._tape.discard(self._cursor)
        if move == 'left':
            self._cursor -= 1
        else:
            self._cursor += 1
        self._state = state

def parse_case(lines, i):
    """Parse 4 lines out: IF, WRITE, MOVE, and CONTINUE.

    Returns: Tuple of (current_val, write, move, continue)
    """
    if_val = int(IF_RE.match(lines[i]).group(1))
    write = int(WRITE_RE.match(lines[i + 1]).group(1))
    move = MOVE_RE.match(lines[i + 2]).group(1)
    state = CONTINUE_RE.match(lines[i + 3]).group(1)
    return (if_val, write, move, state)

def part_1(start, diag_step, states):
    tm = TuringMachine(start, states)
    for i in xrange(diag_step):
        tm.step()
    return len(tm._tape)

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    start = BEGIN_RE.match(lines[0]).group(1)
    diag_step = int(DIAGNOSTIC_RE.match(lines[1]).group(1))
    i = 3  # Skip blank line

    states = {}
    while i < len(lines):
        state = IN_STATE_RE.match(lines[i]).group(1)
        states[state] = {}
        i += 1
        for _ in xrange(2):
            if_val, write, move, next_state = parse_case(lines, i)
            states[state][if_val] = (write, move, next_state)
            i += 4
        i += 1 # Skip blank line
    print part_1(start, diag_step, states)

