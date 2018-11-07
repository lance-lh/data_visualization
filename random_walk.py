from random import choice

class RandomWalk():
    '''a class which generates random walk datas'''

    def __init__(self,num_points=5000):
        '''initialize the property of random walk'''
        self.num_points = num_points

        # all random walk starts with (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''calculate all points in random walk'''

        # walk till list reach the specific length
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # deny walk in place
            if x_step == 0 and y_step == 0:
                continue

            # calculate next value of x and y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)