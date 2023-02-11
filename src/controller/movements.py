from collections import deque
from src.model.movement import Movement


class Movements:
    def __init__(self):
        self._undo_stack = deque()
        self._redo_stack = deque()

    def move(self, movement: Movement):
        self._undo_stack.append(movement)
        self._redo_stack.clear()

    def undo(self):
        try:
            movement = self._undo_stack.pop()
            self._redo_stack.append(movement)
            return movement
        except:
            return None

    def redo(self):
        try:
            movement = self._redo_stack.pop()
            self._undo_stack.append(movement)
            return movement
        except:
            return None
