# DEFINE ABSTRACT MDP CLASS

class MDP:
    def __init__(self, states, actions, discount):
        """
        Initialise states, actions and discount.
        """
        self.states = states
        self.actions = actions
        self.discount = discount

    def transition_model(self, state, action, next_state) -> float:
        """
        returns transition model: P (s′ | s, a)
        """
        pass

    def reward_function(self, state):
        """
        returns reward of given state: R(s)
        """
        pass

    def get_next_states(self, state, action):
        """
        Given current state and action to take, return all possible next states
        """
        pass

