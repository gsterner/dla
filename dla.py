import numpy as np
import pylab as pl

def get_direction(r_number):
    if r_number < 0.25:
        return [1, 0]
    if r_number < 0.5:
        return [0, 1]
    if r_number < 0.75:
        return [-1, 0]
    else:
        return [0, -1]

def do_step(point, step):
    return [point[0] + step[0], point[1] + step[1]]

def perif_vals_from_cluster(cluster):
    perif_vals = set()
    for point in cluster:
        perif_vals.add((point[0] - 1, point[1] - 1))
        perif_vals.add((point[0] - 1, point[1]))
        perif_vals.add((point[0] - 1, point[1] + 1))
        perif_vals.add((point[0], point[1] + 1))
        perif_vals.add((point[0] + 1, point[1] + 1))
        perif_vals.add((point[0] + 1, point[1]))
        perif_vals.add((point[0] + 1, point[1] - 1))
        perif_vals.add((point[0], point[1] - 1 ))
    return list(perif_vals)

def do_diffuse(start_point, perif_vals):
    random_numbers = np.random.uniform(0, 1, 1000000)
    path = [start_point]
    n_steps = 0
    for r in random_numbers:
        step = get_direction(r)
        current = path[-1]
        next_point = do_step(current, step)
        if next_point in perif_vals:
            print("FOUND", n_steps)
            break
        path.append(next_point)
        n_steps = n_steps + 1

    x, y = zip(*path)
    pl.plot(x, y)
    pl.show()

start_point_in = [10, 10]
grid_point = [0, 0]
#perif_vals_in = [grid_point]
#do_diffuse(start_point_in, perif_vals_in)

lot = perif_vals_from_cluster([grid_point])
mult_list = list(zip(*lot))
x = list(mult_list[0])
y = list(mult_list[1])
pl.plot(x, y,'o')
pl.show()
#TODO check that perif_vals_from_cluster works with more points
