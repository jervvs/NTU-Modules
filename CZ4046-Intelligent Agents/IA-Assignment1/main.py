from constants import *
from Maze import Maze
from policyiteration import policy_iteration
from valueiteration import value_iteration
from visualisations import *
import time

if __name__ == '__main__':
    print("What algorithm would you like to try?")
    print("Enter 'value' for value iteration")
    print("Enter 'policy' for policy iteration")
    algorithm = input("Your input: ")

    maze = Maze(GRID, REWARD_MAP, DISCOUNT)

    if algorithm == 'value':
        value_iteration_res = value_iteration(maze, 60)
        plot_utility(value_iteration_res['U_iterations'], "Value Iteration")
        print_utilities(value_iteration_res['U_current'], value_iteration_res['num_iterations'], "value")
        # grid_visualisation(value_iteration_res['U_current'], maze, "utility")
        # grid_visualisation(value_iteration_res['optimal_policy'],maze,"policy")
    elif algorithm == 'policy':
        policy_iteration_res = policy_iteration(maze, K)
        plot_utility(policy_iteration_res['U_iterations'], "Policy Iteration")
        print_utilities(policy_iteration_res['U_current'], policy_iteration_res['num_iterations'], "policy")
        # grid_visualisation(policy_iteration_res['U_current'], maze, "utility")
        # grid_visualisation(policy_iteration_res['optimal_policy'], maze, "policy")
    else:
        print("Your input is: " + algorithm + ", which is not an acceptable input. Please try again")

    











