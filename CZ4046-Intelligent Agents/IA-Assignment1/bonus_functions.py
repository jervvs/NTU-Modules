# FUNCTION USED TO GENERATE MORE COMPLEX GRIDS FOR BONUS QUESTION
import random
from constants import *
from Maze import Maze
from policyiteration import policy_iteration
from valueiteration import value_iteration
from visualisations import *
import time

def generate_maze(grid_length, special = None, wall = None):
    """
    Generates a maze with given grid length
    """

    if special and wall:
        w = 1 - special - wall
        g = o = special/2
    
    elif special and wall is None:
        g = o = special/2
        wall = (0.2/0.7) * (1-special)
        w = (0.5/0.7) * (1-special)

    elif wall and special is None:
        g = (0.15/0.8) * (1-wall)
        o = g
        w = (0.5/0.8) * (1-wall)

    elif special is None and wall is None:
        g = o = 0.15
        wall = 0.2
        w = 0.5

    random.seed()
    maze = []

    for row in range(grid_length):
        maze.append([])

        # WE ITERATE THROUGH EACH CELL AND ADD A CELL VALUE
        for _ in range(grid_length):
            random_color = random.random()

            if random_color < w:
                maze[row].append(' ')
            elif random_color < w + g:
                maze[row].append('G')
            elif random_color < w + g + o:
                maze[row].append('O')
            else:
                maze[row].append('W')

    return maze

if __name__ == '__main__':
    # 3. Bonus - Larger Grid
    value_convergence_iterations = []
    value_convergence_times = []
    policy_convergence_iterations = []
    policy_convergence_times = []

    for size in range(7, 26):
        big_grid = generate_maze(size)
        big_maze = Maze(big_grid, REWARD_MAP, DISCOUNT)
        start = time.time()
        value_iteration_res = value_iteration(big_maze, EPSILON)
        end = time.time()

        value_convergence_iterations.append((size, value_iteration_res['num_iterations']))
        value_convergence_times.append((size, end-start))

        start = time.time()
        policy_iteration_res = policy_iteration(big_maze, K)
        end = time.time()

        policy_convergence_iterations.append((size, policy_iteration_res['num_iterations']))
        policy_convergence_times.append((size, end-start))

    plot_num_iterations(value_convergence_iterations, "value", "grid")
    plot_time(value_convergence_times, "value", "grid")
    plot_num_iterations(policy_convergence_iterations, "policy", "grid")
    plot_time(policy_convergence_times, "policy", "grid")

   
    # 4. Bonus - More Walls
    value_convergence_iterations = []
    value_convergence_times = []
    policy_convergence_iterations = []
    policy_convergence_times = []
    
    wall = 0.1
    
    while wall < 1.0:
        wall_grid = generate_maze(grid_length = 6, wall = wall)
        wall_maze = Maze(wall_grid, REWARD_MAP, DISCOUNT)
        start = time.time()
        value_iteration_res = value_iteration(wall_maze, EPSILON)
        end = time.time()

        value_convergence_iterations.append((wall, value_iteration_res['num_iterations']))
        value_convergence_times.append((wall, end-start))

        start = time.time()
        policy_iteration_res = policy_iteration(wall_maze, K)
        end = time.time()

        policy_convergence_iterations.append((wall, policy_iteration_res['num_iterations']))
        policy_convergence_times.append((wall, end-start))

        wall += 0.05

    plot_num_iterations(value_convergence_iterations, "value", "wall")
    plot_time(value_convergence_times, "value", "wall")
    plot_num_iterations(policy_convergence_iterations, "policy", "wall")
    plot_time(policy_convergence_times, "policy", "wall")

    #5. Bonus - More Special
    value_convergence_iterations = []
    value_convergence_times = []
    policy_convergence_iterations = []
    policy_convergence_times = []
    
    special = 0.1
    while special <= 1.0:
        special_grid = generate_maze(6, special = special)
        special_maze = Maze(special_grid, REWARD_MAP, DISCOUNT)
        start = time.time()
        value_iteration_res = value_iteration(special_maze, EPSILON)
        end = time.time()

        value_convergence_iterations.append((special, value_iteration_res['num_iterations']))
        value_convergence_times.append((special, end-start))

        start = time.time()
        policy_iteration_res = policy_iteration(special_maze, K)
        end = time.time()

        policy_convergence_iterations.append((special, policy_iteration_res['num_iterations']))
        policy_convergence_times.append((special, end-start))

        special += 0.05

    plot_num_iterations(value_convergence_iterations, "value", "special")
    plot_time(value_convergence_times, "value", "special")
    plot_num_iterations(policy_convergence_iterations, "policy", "special")
    plot_time(policy_convergence_times, "policy", "special")