# IMPLEMENT MAZE CLASS WHICH INHERITS FROM MDP

from MDP import MDP

class Maze(MDP):
    """
    Maze is a 2D square array where each square can take different values.

    Possible squares:
        - ' ': white
        - 'G': green
        - 'O': orange
        - 'W': wall
    """
    def __init__(self, grid, reward_map, discount):
        """
        Initialises:
            - grid which will hold the states and possible actions in the maze. 
            - reward map of each state 
            - mdp (states, actions, discount)
        """
        self.grid = grid
        self.reward_map = reward_map

        states = []
        for x in range(len(grid)):
            for y in range(len(grid)):
                # ONLY NEED TO HOLD NON-WALL STATES
                if grid[x][y] != 'W':
                    states.append((x,y))

        actions = ['^', 'v', '<', '>']

        super().__init__(states, actions, discount)

    def transition_model(self, state, action, next_state) -> float:
        """
        returns transition model: P (s′ | s, a)
        """
        return self.get_next_states(state, action)[next_state]['probability']

    def reward_function(self, state):
        """
        returns reward of given state: R(s)
        """
        square = self.grid[state[0]][state[1]]
        return self.reward_map[square]

    def get_next_states(self, state, action):
        """
        Given current state and action to take, return all possible next states
        We use the intended state instead of actual state as keys to prevent situations where the same state is reached for different actions.

        """
        up_state =(state[0]-1, state[1])
        down_state = (state[0]+1, state[1])
        left_state = (state[0], state[1]-1)
        right_state = (state[0], state[1]+1)

        #CHECK If STATES ARE VALID
        if up_state in self.states:
            actual_up_state = up_state 
        else:
            actual_up_state = state  
        
        if down_state in self.states:
                actual_down_state = down_state 
        else:
            actual_down_state = state  

        if left_state in self.states:
            actual_left_state = left_state 
        else:
            actual_left_state = state 

        if right_state in self.states:
            actual_right_state = right_state 
        else:
            actual_right_state = state 

        if action == '^':
            next_states = {
                up_state:{
                    'actual': actual_up_state,
                    'probability': 0.8
                },
                right_state:{
                    'actual': actual_right_state,
                    'probability': 0.1
                },
                left_state:{
                    'actual': actual_left_state,
                    'probability': 0.1
                }
            }

        elif action  == 'v':
            next_states = {
                down_state:{
                    'actual': actual_down_state,
                    'probability': 0.8
                },
                right_state:{
                    'actual': actual_right_state,
                    'probability': 0.1
                },
                left_state:{
                    'actual': actual_left_state,
                    'probability': 0.1
                }
            }

        elif action  == '<':
            next_states = {
                up_state:{
                    'actual': actual_up_state,
                    'probability': 0.1
                },
                down_state:{
                    'actual': actual_down_state,
                    'probability': 0.1
                },
                left_state:{
                    'actual': actual_left_state,
                    'probability': 0.8
                }
            }

        else:  # action  == '>'
            next_states = {
                up_state:{
                    'actual': actual_up_state,
                    'probability': 0.1
                },
                right_state:{
                    'actual': actual_right_state,
                    'probability': 0.8
                },
                down_state:{
                    'actual': actual_down_state,
                    'probability': 0.1
                }
            }
        return next_states
