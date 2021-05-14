# IMPLEMENTATION OF VALUE ITERATION FROM FIG 17.4 OF ARTIFICIAL INTELLIGENCE: A MODERN APPROACH

from MDP import MDP

def value_iteration(mdp, EPSILON):
    """
    inputs: 
        mdp - an MDP with states S , actions A(s), transition model P (s′ | s, a), rewards R(s), discount γ
        EPSILON - maximum error allowed in the utility of any state
    returns: 
        U_current - current utility of each state
        U_iterations - list of utilities of each state at each iteration
        optimal_policy - best action at each state
        num_iterations - total number of iterations till convergence
    """

    # LOCAL VARIRABLES 
    U_current, U_next = {}, {}  # U, U' dictionary of utilities for states
    max_utility_change = 0 # δ maximum change in utility at any iteration
    convergence_threshold = (EPSILON * (1 - mdp.discount))/mdp.discount
    
    # Supplementary dictionaries for visualisation
    U_iterations, optimal_policy, policy_loss= {}, {}, []
    
    for state in mdp.states:
        #initialise utility value of all states in U_current and U_next to be 0
        U_current[state] = 0
        U_next[state] = 0
        U_iterations[state] = [] 
        optimal_policy[state] = None

    num_iterations = 0
    converged = False

    while not converged:
        # U ← U′; δ ← 0
        for state in mdp.states:
            U_current[state] = U_next[state] # U ← U′
            U_iterations[state].append(U_current[state])
            
        max_utility_change = 0 # δ

        for state in mdp.states:
            updated_utility, best_action = bellman_update(mdp, state, U_current)
            U_next[state] = updated_utility
            optimal_policy[state] = best_action

            abs_utility_change = abs(U_next[state] - U_current[state])
            if abs_utility_change > max_utility_change:
                max_utility_change = abs_utility_change

        num_iterations += 1

        policy_loss.append(max_utility_change)

        print("Iteration: " + str(num_iterations))
        print("Maximum Utility Change: " + str(max_utility_change))

        if max_utility_change < convergence_threshold:
            converged = True
    
    return {
        'U_current': U_current,
        'U_iterations': U_iterations,
        'optimal_policy': optimal_policy,
        'num_iterations' : num_iterations,
        'policy_loss': policy_loss
    }

def bellman_update(mdp, state, U_current):
    """
    Bellman Update:  Ui+1(s)←R(s)+γ max ∑ P(s′|s,a)Ui(s′)

    inputs: 
        mdp - an MDP with states S , actions A(s), transition model P (s′ | s, a), rewards R(s), discount γ
        state - the given state
        U_current - current utility of each state
    returns:
        utility - updated utility
        best_action - best action to take in the given state
    """

    max_expected_utility = float('-inf')
    best_action = None

    for action in mdp.actions:
        expected_utility = get_expected_utility(mdp, state, action, U_current)
        if expected_utility > max_expected_utility:
            max_expected_utility = expected_utility
            best_action = action

    utility = mdp.reward_function(state) + mdp.discount * max_expected_utility
    return (utility, best_action)


def get_expected_utility(mdp, state, action, U_current):
    """
    Calculates sum of expected utility: ∑s′P(s′|s, a)U[s′]
    inputs: 
        mdp - an MDP with states S , actions A(s), transition model P (s′ | s, a), rewards R(s), discount γ
        state - the given state
        action - action to take at given state
        U_current - current utility of each state
    
    returns: sum_expected_utility
    """
    sum_expected_utility = 0
    next_states = mdp.get_next_states(state, action)

    for next_state in next_states:
        probability = mdp.transition_model(state, action, next_state)
        actual_next_state = next_states[next_state]["actual"]
        sum_expected_utility += probability * U_current[actual_next_state]

    return sum_expected_utility
