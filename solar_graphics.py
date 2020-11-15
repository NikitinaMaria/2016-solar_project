"""
Graphs of the speed module of the planet from time, of the distance of the satellite to the star from time,
of the speed module from the distance to the star
"""

import numpy as np
import matplotlib.pyplot as plt


def speed_time_graph(time, speed):
    fig = plt.figure()
    plt.xlabel('Time, s')
    plt.ylabel('Speed, m/s')
    plt.title('Graph of the speed module from time')
    plt.plot(time, speed)
    plt.savefig('Speed_time_graph')


def distance_time_graph(time, distance):
    fig = plt.figure()
    plt.xlabel('Time, s')
    plt.ylabel('Distance, m/s')
    plt.title('Graph of the distance to the star from time')
    plt.plot(time, distance)
    plt.savefig('Distance_time_graph')


def speed_distance_graph(distance, speed):
    fig = plt.figure()
    plt.xlabel('Distance, s')
    plt.ylabel('Speed, m/s')
    plt.title('Graph of the speed module from the distance to the star')
    plt.plot(distance, speed)
    plt.savefig('Speed_distance_graph')


def all_graphs():
    stats = open('stats.txt', 'r')
    time = []
    speed = []
    distance = []
    star_x = 0
    star_y = 0
    for line in stats:
        if len(line.strip()) == 0:
            continue  # Skip empty lines and comment lines
        object_type = line.split()[1].lower()
        if object_type == "star":
            star_x = float(line.split()[5])
            star_y = float(line.split()[6])
        elif object_type == "planet":
            planet_x = float(line.split()[5])
            planet_y = float(line.split()[6])
            distance.append(
                np.sqrt((planet_x - star_x) * (planet_x - star_x) + (planet_y - star_y) * (planet_y - star_y)))
            speed_x = float(line.split()[7])
            speed_y = float(line.split()[8])
            speed.append(np.sqrt(speed_x * speed_x + speed_y * speed_y))
            time.append(float(line.split()[0]))
        else:
            continue
    speed_time_graph(time, speed)
    distance_time_graph(time, distance)
    speed_distance_graph(distance, speed)
    stats.close()

if __name__ == "__main__":
    print("This module is not for direct call!")
