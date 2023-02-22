# Programming Project 3
# CSC 170 - Ha Linh

from typing import List
import random
from graphics import *
import math

class Tree:
    '''
    A class to represent a tree burning

    Attributes:
        burn_level: [int] burn level of tree from 0 -> 3

    Methods:
        __repr__(): return burning level of tree object
        get_image_file(): get image that matches with burn level
    '''
    
    def __init__(self):
        '''
        Constructs necessary attribute for the tree object
        Set burn level of tree object = 3
        
        Parameters: None

        Return: None
        '''
        
        self.burn_level = 3
        # 3 -> 2 -> 1 -> 0

    def __repr__(self) -> str:
        '''
        Return burning level of tree object
        
        Parameters:
            burn_level: [int] burn level of tree from 0 -> 3

        Return: None
        '''
        
        return f"{self.burn_level}"

    def get_image_file(self):
        '''
        Get image that matches with burn level
        
        Parameters: None

        Return: None
        '''
        
        if self.burn_level == 3:
            return "0_tree.png"
        if self.burn_level == 2:
            return "1_little_burn.png"
        if self.burn_level == 1:
            return "2_lot_burn.png"
        if self.burn_level == 0:
            return "3_charcoal.png"


class Forest:
    '''
    A class to represent the forest

    Attributes:
        burn_probability: [float] burn probabillity of tree objects in forest
        window: [Graphwin] display forest
        tree_w: [int] number of trees in a row
        tree_h: [int] number of rows of trees in forest
        
    Methods:
        set_burn_probability(burn_probability: float): set burn probability
                                                       of tree object
        reset(): reset to unburnt forest
        print_state(): print burn step
        graph_forest(): graph forest
        start_fire(x, y): start fire randomly
        start_fire_at_click(): start fire at a tree object clicked
        get_trees_to_burn(): selecting trees to burn
        run_simulation(): run the simulation
    '''
    
    def __init__(self, burn_probability: float, window, tree_w, tree_h):
        '''
        Constructs necessary attributes for the forest class

        Parameters:
            burn_probability: [float] burn probabillity of tree objects in forest
            window: [window] display forest
            tree_w: [int] number of trees in a row
            tree_h: [int] number of rows of trees in forest

        Return: None
        '''
        
        self.tree_w = tree_w
        self.tree_h = tree_h
        self.window = window
        self.step_counter = 0
        self.burn_probability = burn_probability
        
        self.tree_images: List[List[Tree]] = []
        self.trees: List[List[Tree]] = []
        self.result_banner = None
        self.result_text = None
        
        self.reset()
    
    def set_burn_probability(self, burn_probability: float):
        '''
        Set burn probability of tree object

        Parameters:
            burn_probability: [float] burn probabillity of tree objects in forest

        Return: None
        '''
        
        self.burn_probability = burn_probability
    
    def reset(self):
        '''
        Reset to unburnt forest
        
        Parameters: None

        Return: None
        '''
        
        if self.result_banner:
            self.result_banner.undraw()
            self.result_text.undraw()
            
        self.step_counter = 0
        self.tree_images: List[List[Tree]] = []
        self.trees: List[List[Tree]] = []
        
        for i in range(10):
            self.trees.append([])
            self.tree_images.append([])
            
        for i in range(10):
            for j in range(15):
                self.trees[i].append(Tree())
                self.tree_images[i].append(None)

    def print_state(self):
        '''
        Print burn step
        
        Parameters: None

        Return: None
        '''
        
        print(f"Step: {self.step_counter}")
        
        for row in self.trees:
            print(row)
    
    def graph_forest(self):
        '''
        Graph forest

        Parameters: None

        Return: None
        '''
        
        for i in range(len(self.trees)):
            for j in range(len(self.trees[i])):
                image_file = self.trees[i][j].get_image_file()
                tree_state = Image(Point(self.tree_w / 2 + self.tree_w * j,
                                         self.tree_h / 2 + self.tree_h * i), image_file)
                
                if self.tree_images[i][j]:
                    self.tree_images[i][j].undraw()
                    
                tree_state.draw(self.window)
                self.tree_images[i][j] = tree_state

    # start the fire from the first burnt tree
    def start_fire(self, x, y):
        '''
        Start fire randomly

        Parameters:
            x: [Point] x of tree object
            y: [Point] y of tree object

        Return: None
        '''
        
        self.trees[x][y].burn_level = 2

    def start_fire_at_click(self):
        '''
        Start fire at a tree object clicked

        Parameters: None

        Return: None
        '''
        
        while True:
            click = self.window.getMouse()
            
            i = math.floor(click.getY() / self.tree_w)
            j = math.floor(click.getX() / self.tree_h)
            
            if i < 10 and j < 15:
                self.start_fire(i, j)
                break

    #selecting the suround trees
    def get_trees_to_burn(self) -> List[Tree]:
        '''
        Selecting trees to burn

        Parameters: None

        Return:
            result: [list] list of trees to burn
        '''
        
        result = []
        for i in range(len(self.trees)):
            row = self.trees[i]
            for j in range(len(row)):
                tree = row[j]
                # check if tree can spread fire
                if 3 > tree.burn_level > 0:
                    for x in range(i-1, i+2):
                        for y in range(j-1, j+2):                            
                            # check whether position is valid
                            if len(self.trees) > x >= 0 and len(self.trees[0]) > y >= 0:
                                # check whether tree is already in list or tree is already burnt
                                if self.trees[x][y] not in result and self.trees[x][y].burn_level != 0:
                                    # spread chance when tree is starting to burn
                                    if self.trees[x][y].burn_level == 3:
                                        chance = random.random()
                                        if chance <= self.burn_probability:
                                            result.append(self.trees[x][y])
                                    # when tree is already burning
                                    else:
                                        result.append(self.trees[x][y])
        return result
    
    def run_simulation(self):
        '''
        Run the simulation

        Parameters: None

        Return: None
        '''
        
        trees_to_burn = self.get_trees_to_burn()
        
        while trees_to_burn:
            for tree in trees_to_burn:
                tree.burn_level -= 1

            self.step_counter += 1
            
            # self.print_state()
            self.graph_forest()
            trees_to_burn = self.get_trees_to_burn()

        self.result_banner = Rectangle(Point(self.tree_w * 2, self.tree_h * 4), Point(self.tree_w * 13, self.tree_h * 6))
        self.result_banner.setFill("yellow")
        self.result_banner.draw(self.window)
        self.result_text = Text(Point(self.tree_w * 7.5, self.tree_h * 5), f"The fire subsided after {self.step_counter} steps.")
        self.result_text.draw(self.window)

# see if click point is in side the button or not
def is_button_click(button: Rectangle, click: Point):
    '''
    Check if button is clicked

    Parameters:
        button: [Rectangle] button to click
        click: [Point] where clicked
    '''
    
    if button.getP1().getX() <= click.getX() <= button.getP2().getX():
        if button.getP1().getY() <= click.getY() <= button.getP2().getY():
            return True
        
    return False


def main():
    win_x = 900
    win_y = 500
    button_height = 50
    button_width = 200
    button_space = 25
    tree_w = 40
    tree_h = 40

    win = GraphWin("Forest", win_x, win_y)

    ## Exit button
    exit_btn_width = 50
    exit_button = Rectangle(Point(win_x - exit_btn_width, 0), Point(win_x, button_height))
    exit_button.setFill("red")
    exit_button.draw(win)
    x_sign = Text(Point(win_x - exit_btn_width / 2, button_height / 2), "X")
    x_sign.draw(win)

    # the line of buttons
    button_x = win_x - button_width - button_space

    ## Burn probability box
    question = Text(Point(button_x + button_width / 2, button_height * 2 + button_space), "Burn Probability:")
    question.draw(win)
    input_box = Entry(Point(button_x + button_width / 2, button_height * 3 + button_space), 20)
    input_box.setFill("grey")
    input_box.setText("0.18")
    input_box.draw(win)

    # buttons to start the simulation        
    ## button 1: randomly start
    rand_start_button = Rectangle(Point(button_x, button_height * 4), Point(button_x + button_width, button_height * 5))
    rand_start_button.draw(win)
    rand_start_text = Text(Point(button_x + button_width / 2, button_height * 4.5), "Random start")
    rand_start_text.draw(win)

    ## button 2: click to start
    click_start_button = Rectangle(Point(button_x, button_height * 5 + button_space), Point(button_x + button_width, button_height * 6 + button_space))
    click_start_button.draw(win)
    click_start_text = Text(Point(button_x + button_width / 2, button_height * 5.5 + button_space), "Click to start")
    click_start_text.draw(win)

    ## button 3: reset simulation
    click_reset_button = Rectangle(Point(button_x, button_height * 6 + button_space * 2), Point(button_x + button_width, button_height * 7 + button_space * 2))
    click_reset_button.draw(win)
    click_reset_text = Text(Point(button_x + button_width / 2, button_height * 6.5 + button_space * 2), "Click to Reset")
    click_reset_text.draw(win)

    # initialize
    forest = Forest(0, win, tree_w, tree_h)
    forest.graph_forest()

    ## decide whether start fire randomly or by user's selection by getting a click point
    while True:
        click_point = win.getMouse()
        
        if is_button_click(rand_start_button, click_point):
            # random start
            start_i = random.randint(0, 9)
            start_j = random.randint(0, 14)
            probability = float(input_box.getText())
            forest.set_burn_probability(probability)
            forest.start_fire(start_i, start_j)
            forest.run_simulation()
            
        elif is_button_click(click_start_button, click_point):
            # click to start
            probability = float(input_box.getText())
            forest.set_burn_probability(probability)
            forest.start_fire_at_click()
            forest.run_simulation()
            
        elif is_button_click(click_reset_button, click_point):
            # click to reset
            forest.reset()
            forest.graph_forest()
            
        elif is_button_click(exit_button, click_point):
            # click to exit
            win.close()
            break
    
    return

if __name__ == "__main__":
    main()


