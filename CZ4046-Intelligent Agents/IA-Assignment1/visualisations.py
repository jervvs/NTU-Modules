import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from constants import *

def plot_utility(U_iterations, policy):
    """
    inputs: 
        Takes in dictionary of utilities for each state
        policy - use Value Iteration or Policy Iteration. Will be the title of the plot.

    """
    fname = ''.join(policy.split()).lower()
    plt.figure(figsize=(16, 8))

    for state in U_iterations:
        plt.plot(U_iterations[state])

    plt.legend(U_iterations, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title(policy,fontsize= 20)
    plt.xlabel('Number of Iterations', fontsize= 20)
    plt.ylabel('Utility Estimates', fontsize= 20)
    plt.savefig('output/'+fname+'.png')

def plot_num_iterations(num_iterations_list, algorithm, policy):
    """
    inputs: 
        num_iterations_list - list of tuples (metric, num_iterations)
        algorithm - can be "policy" or "value"
        policy - can be "grid", "wall", "special"
    """
    plt.figure(figsize=(10, 8))
    plt.plot(*zip(*num_iterations_list))
    plt.ylabel('Number of Iterations', fontsize= 10)

    if policy == 'grid':
        plt.xlabel('Size', fontsize= 10)
        plt.title('Convergence Iterations Against Grid Size',fontsize= 20)
        plt.savefig('output/' + algorithm + 'GridSizeConvergence.png')
    elif policy == 'wall': 
        plt.xlabel('Wall Probability', fontsize= 10)
        plt.title('Number of Iterations Against Wall Probability',fontsize= 20)
        plt.savefig('output/'+ algorithm + 'WallProbConvergence.png')
    elif policy == 'special': 
        plt.xlabel('Special Probability', fontsize= 10)
        plt.title('Number of Iterations Against Special Probability',fontsize= 20)
        plt.savefig('output/'+ algorithm + 'SpecialProbConvergence.png')
    
def plot_time(time_list, algorithm, policy):
    """
    inputs: 
        num_iterations_list - list of tuples (metric, time)
        algorithm - can be "policy" or "value"
        policy - can be "grid", "wall", "special"
    """
    plt.figure(figsize=(10, 8))
    plt.plot(*zip(*time_list))
    plt.ylabel('Time', fontsize= 10)

    if policy == 'grid':
        plt.xlabel('Size', fontsize= 10)
        plt.title('Convergence Time Against Grid Size',fontsize= 20)
        plt.savefig('output/' + algorithm + 'GridSizeTime.png')
    elif policy == 'wall': 
        plt.xlabel('Wall Probability', fontsize= 10)
        plt.title('Convergence Time Against Wall Probability',fontsize= 20)
        plt.savefig('output/'+ algorithm + 'WallProbTime.png')
    elif policy == 'special': 
        plt.xlabel('Special Probability', fontsize= 10)
        plt.title('Convergence Time Against Special Probability',fontsize= 20)
        plt.savefig('output/'+ algorithm + 'SpecialProbTime.png')

def print_utilities(U_current, num_iterations, algorithm):
    if (algorithm == "value"):
        print("---------------------------------------------------------")
        print("Value Iteration Algorithm")
        print("Values of Parameters")
        print("---------------------------------------------------------")
        print("Discount Factor", "\t\t", ":", DISCOUNT)
        print("Epilson Value", "\t\t\t", ":",EPSILON)
        print("Number of Iterations","\t",":", num_iterations)

    elif (algorithm =="policy"):
        print("---------------------------------------------------------")
        print("Policy Iteration Algorithm")
        print("Values of Parameters")
        print("---------------------------------------------------------")
        print("Discount Factor", "\t\t", ":",DISCOUNT)
        print("K","\t\t\t\t\t\t",":", K)
        print("Number of Iterations","\t",":", num_iterations)


    print("---------------------------------------------------------")
    print("Utility Values of all States")
    print("---------------------------------------------------------")
    print(" State : Value")
    for state in U_current:
        print(state,":",U_current.get(state))
    print("---------------------------------------------------------")


def grid_visualisation(res_dict,maze,policy):
    """
    inputs: 
        res_dict - the results dictionary which will hold the optimal policy or final utility for each state
        maze - the maze used
        policy - can be 'utility' or 'policy' 
    returns: 
        provides the grid visualisation of the final utility value or policy
    """
    class Cell():
        EMPTY_COLOR_BG = "white"
        WALL_COLOR="grey"
        FILLED_COLOR_BORDER = "black"
        EMPTY_COLOR_BORDER = "black"

        def __init__(self, master, x, y, size, text):
            """ Constructor of the object called by Cell(...) """
            self.master = master
            self.abs = x
            self.ord = y
            self.size = size
            self.fill = False
            self.text = text

        def draw(self):
            """ order to the cell to draw its representation on the canvas """
            if self.master != None:
                if (self.text=="W"):
                    fill=Cell.WALL_COLOR
                else:
                    fill = Cell.EMPTY_COLOR_BG

                outline = Cell.EMPTY_COLOR_BORDER

                xmin = self.abs * self.size
                xmax = xmin + self.size
                ymin = self.ord * self.size
                ymax = ymin + self.size

                self.master.create_rectangle(xmin, ymin, xmax, ymax, fill=fill, outline=outline)
                self.master.create_text((xmax - self.size / 2, ymax - self.size / 2), text=self.text)


    class CellGrid(Canvas):
        def __init__(self, master, grid, cell_size, *args, **kwargs):
            np_array=grid
            row_number = len(np_array)
            column_number = len(np_array[0])
            Canvas.__init__(self,
                            master,
                            width=cell_size * column_number,
                            height=cell_size * row_number,
                            *args,
                            **kwargs)

            self.cell_size = cell_size

            self.grid = []
            for row in range(row_number):
                line = []
                for column in range(column_number):
                    line.append(Cell(self,column,row,cell_size,np_array[row][column],))
                self.grid.append(line)
            self.draw()

        def draw(self):
            for row in self.grid:
                for cell in row:
                    cell.draw()

    app = Tk("Grid")
    grid = maze.grid
    if (policy=="policy"):
        for key in res_dict:
            grid[key[0]][key[1]] = res_dict[key]
    elif (policy=="utility"):
        for key in res_dict:
            grid[key[0]][key[1]] = format(round(res_dict[key],3))

    grid = CellGrid(app, grid, 80)
    grid.pack()
    app.mainloop()