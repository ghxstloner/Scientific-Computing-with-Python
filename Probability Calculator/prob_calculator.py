import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)
    def draw(hat, num_balls_drawn):
        if num_balls_drawn > len(hat.contents):
            return hat.contents
        balls_drawn = random.sample(hat.contents, num_balls_drawn)
        for ball in balls_drawn:
            hat.contents.remove(ball)
        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = Hat.draw(hat_copy, num_balls_drawn)
        balls_dict = {}
        for ball in balls_drawn:
            balls_dict[ball] = balls_dict.get(ball, 0) + 1
        match = True
        for color, count in expected_balls.items():
            if balls_dict.get(color, 0) < count:
                match = False
                break
        if match:
            success += 1
    return success / num_experiments
