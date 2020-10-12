import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self,**kwargs):
        self.contents=[]
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self,number):
        drawn = []
        if number <= len(self.contents):
            for i in range(number):
                rand = random.choice(self.contents)
                self.contents.remove(rand)
                drawn.append(rand)
            return drawn
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M=0
    istrue = False
    for i in range (num_experiments):
        hatexp = copy.deepcopy(hat)
        drawn = hatexp.draw(num_balls_drawn)
        drawn_dict = {i:drawn.count(i) for i in drawn}
        for k,v in expected_balls.items():
            if k in drawn_dict and expected_balls[k] <= drawn_dict[k]:
                istrue = True
            else:
                istrue = False
                break
        if istrue:
            M+=1
    return(M/num_experiments)