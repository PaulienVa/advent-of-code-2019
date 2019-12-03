# --- Day 3: Crossed Wires ---

vertical_factors = {'D': -1, 'U': 1}
horizontal_factors = {'R': 1, 'L': -1}

def wires():
    with open('input1.txt') as file:
        wire_lines = []
        for line in file:
            commands = line.split(',')
            points = [(0, 0)]
            for cmd in commands:
                direction = cmd[0]
                steps = int(cmd[1:])
                assert direction in ['D', 'U', 'L', 'R']
                if direction in vertical_factors.keys():
                    for i in range(steps):
                        previous_point = points[len(points) - 1]
                        vertical_delta = previous_point[1] + 1 * vertical_factors.get(direction)
                        points.append((previous_point[0], vertical_delta))
                if direction in horizontal_factors.keys():
                    for i in range(steps):
                        previous_point = points[len(points) - 1]
                        horizontal_delta = previous_point[0] + 1 * horizontal_factors.get(direction)
                        points.append((horizontal_delta, previous_point[1]))
            wire_lines.append(points)
        return wire_lines

def crossing_manhattan(wire_lines):
    crossing_points = set(wire_lines[0]) & set(wire_lines[1])
    crossing_points.remove((0,0))
    print('What are the crossing points ' + str(crossing_points))
    return min(map(lambda point: abs(point[0]) + abs(point[1]), crossing_points))


def minimal_combined_steps(wire_lines):
    crossing_points = set(wire_lines[0]) & set(wire_lines[1])
    crossing_points.remove((0,0))
    steps = []
    for cp in crossing_points:
        (index_cp1, index_cp2) = (wire_lines[0].index(cp), wire_lines[1].index(cp))
        (sub_wire1, sub_wire2) = (wire_lines[0][:index_cp1], wire_lines[1][:index_cp2])
        stepsA = sum([ nr_steps(sub_wire1[x], sub_wire1[x-1]) for x in range(1, len(sub_wire1))])
        stepsB = sum([ nr_steps(sub_wire2[x], sub_wire2[x-1]) for x in range(1, len(sub_wire2))])
        steps.append(stepsA + stepsB)
    return min(steps)


def nr_steps(pointA, pointB):
    st = pointA[0] - pointB[0] + pointA[1] - pointB[1]
    return abs(st)

if __name__ == '__main__':
    minimal_distance = crossing_manhattan(wires())
    print('What is the manhattan distance to the closest intersection point ' + str(minimal_distance))
    min_st = minimal_combined_steps(wires())
    print("What are the minimal steps to the closest intersection point: " + str(min_st  + 2 )) # steps from origin and to point are missing

