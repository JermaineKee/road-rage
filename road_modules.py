import random
import math
import statistics as st
import numpy as np
import matplotlib.pyplot as plt



class Car:

    """
    Responsibilities:
    set car size,
    set max speed,
    set acceleration,
    set distance between next car,
    """
    def __init__(self, name, position, acc_rate = 2, car_size = 5, max_speed = 120, min_speed = 0, distance_between = 1):
        self.name = name
        self.car_size = car_size
        self.position = position
        self.acc_rate = acc_rate
        self.max_speed = max_speed*1000/3600
        self.min_speed = min_speed
        self.pres_speed = self.max_speed
        self.distance_between = distance_between

    def __str__(self):
        return "Car(car_size={}, acc_rate={}, max_speed={}, pres_speed={}, position={}  )".format(self.car_size, self.acc_rate, self.max_speed, self.pres_speed, self.position)

    def go(self):
        self.position += self.pres_speed


    def __repr__(self):
        return self.__str__()




class Road:

    """
    Responsibilities:
    hold cars
    determine length of Road
    determine number of cars

    Collaborators:
    Car

    """

    def __init__(self, max_speed = 120, num_of_cars = 30, road_length = 1000, ):
        self.max_speed = max_speed
        self.racecar = [self.move(position*road_length//num_of_cars) for position in range(num_of_cars*road_length//1000)]
        self.road_length = road_length

    def move(self, position):
        return Car(position, self.max_speed)



class Simulation:

    """
    Responsibilities:
    places car on the road,
    moves car,
    randomly changes speed of cars 10percent each second

    """
    def __init__(self, max_speed, total_ticks = 60 ):
        self.road = Road(max_speed)
        self.total_ticks = total_ticks
        self.ticks = 0
        self.positions = np.array([])
        self.speeds = np.array([])


    

    def tick(self):
        for x in range(len(self.road.racecar) -1, -1, -1):
            self.road.racecar[x].go()




    def run(self):
        while self.ticks < self.total_ticks:
            self.tick()
            self.speeds[self.ticks+1] ++ [x.pres_speed for x in self.road.racecar]
            self.ticks += 1
        return self.speeds

class PosSim(Simulation):
    def __init__(self, max_speed):
        super().__init__(max_speed)

    def run(self):
        while self.ticks < self.total_ticks:
            self.tick()
            self.positions[self.ticks+1] += [x.position for x in self.road.racecar]
        return self.positions
