# Shared Intcode computer used by days 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25


def load_program(input_file):
  with open(input_file, "r") as f:
    return list(map(int, f.read().strip().split(",")))


class Intcode:
  def __init__(self, program, inputs=None):
    self.memory = dict(enumerate(program))
    self.ip = 0
    self.relative_base = 0
    self.inputs = list(inputs) if inputs else []
    self.outputs = []
    self.halted = False

  def _addr(self, offset, modes):
    mode = (modes // (10 ** (offset - 1))) % 10
    raw = self.memory.get(self.ip + offset, 0)
    if mode == 1:
      return self.ip + offset
    if mode == 2:
      return self.relative_base + raw
    return raw

  def _read(self, offset, modes):
    return self.memory.get(self._addr(offset, modes), 0)

  def _write(self, offset, modes, value):
    self.memory[self._addr(offset, modes)] = value

  def run(self):
    # Runs until an output is produced (True), input is needed (False) or the program halts (None).
    while True:
      instr = self.memory.get(self.ip, 0)
      opcode = instr % 100
      modes = instr // 100

      if opcode == 1:
        self._write(3, modes, self._read(1, modes) + self._read(2, modes))
        self.ip += 4
      elif opcode == 2:
        self._write(3, modes, self._read(1, modes) * self._read(2, modes))
        self.ip += 4
      elif opcode == 3:
        if not self.inputs:
          return False
        self._write(1, modes, self.inputs.pop(0))
        self.ip += 2
      elif opcode == 4:
        self.outputs.append(self._read(1, modes))
        self.ip += 2
        return True
      elif opcode == 5:
        self.ip = self._read(2, modes) if self._read(1, modes) != 0 else self.ip + 3
      elif opcode == 6:
        self.ip = self._read(2, modes) if self._read(1, modes) == 0 else self.ip + 3
      elif opcode == 7:
        self._write(3, modes, 1 if self._read(1, modes) < self._read(2, modes) else 0)
        self.ip += 4
      elif opcode == 8:
        self._write(3, modes, 1 if self._read(1, modes) == self._read(2, modes) else 0)
        self.ip += 4
      elif opcode == 9:
        self.relative_base += self._read(1, modes)
        self.ip += 2
      elif opcode == 99:
        self.halted = True
        return None
      else:
        raise Exception("Unknown opcode %d at %d" % (opcode, self.ip))

  def run_all(self):
    # Runs until halt or input starvation and returns all outputs collected so far.
    while self.run():
      pass
    return self.outputs

  def step_output(self):
    # Runs until the next output; returns it, or None if halted / waiting for input.
    n = len(self.outputs)
    self.run()
    return self.outputs[-1] if len(self.outputs) > n else None
