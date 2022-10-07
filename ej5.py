import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, red=0, orange=0, black=0, blue=0, pink=0, striped=0, green=0, yellow=0, test= 0):
        self.red = red
        self.orange = orange
        self.black = black
        self.blue = blue
        self.pink = pink
        self.striped = striped
        self.green = green
        self.yellow = yellow
        self.test = test
        self.contents = list()
        self.contentsAll = {"red": self.red, "orange" : orange, "black" : black, "blue" : blue, "pink": pink, "striped": striped, "green" : green, "yellow": yellow, "test": test}


    def draw(self, num):
        all_removed = []
        if(num > len(self.contents)):
            return self.contents
        for i in range(num):
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            all_removed.append(removed)
        print(all_removed)
        return all_removed

      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)

        for color in colors_gotten:
            if(color in expected_copy):
                expected_copy[color]-=1

        if(all(x <= 0 for x in expected_copy.values())):
            count += 1

    return count / num_experiments


# hat1 = Hat(red=4, green=3)
# hat2 = Hat(red=3, blue=2)

# print(hat1.contentsAll)  
# print(hat1.contents)

# print(hat2.contentsAll)  
# print(hat2.contents)
