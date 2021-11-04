
from .views import State
#Find an existing class that contains state-dependent code,
#  or create a suitable context class. 
# It should include a reference to a specific state as well
#  as a method for switching between states.

class Context:

    _state = None

    def __init__(self, state: State) -> None:
        self.setState(state)

    def setState(self, state: State):

        print(f"Book Status {type(state).__name__}")
        self._state = state
        self._state.context = self

    def markStatus(self):
        self._state.markStatus()

