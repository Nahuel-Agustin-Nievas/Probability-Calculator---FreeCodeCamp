import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, red=0, orange=0, black=0, blue=0, pink=0, striped=0, green=0):
        self.red = red
        self.orange = orange
        self.black = black
        self.blue = blue
        self.pink = pink
        self.striped = striped
        self.green = green
        self.contents = list()
        self.contentsAll = {"red": self.red, "orange" : orange, "black" : black, "pink": pink, "striped": striped, "green" : green}
        for key, value in self.contentsAll.items():
            if value > 0 :
               for i in range(value):
                self.contents.append(key)
 
    
# class Hat:
#     def __init__(self, name):
#         self.name = name
#         self.contents = list()

      


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):


hat1 = Hat(black=6, red=4, green=3)

print(hat1.contentsAll)  
print(hat1.contents)

