from typing import Any


class BehaviorTree:
    _root: Any

    def __init__(self):
        self._create_bt()

    def _create_bt(self):
        pass

    def tick(self):
        self._root.tick_once()
