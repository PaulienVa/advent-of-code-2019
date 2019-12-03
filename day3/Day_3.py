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

def crossing(wire_lines):
    crossing_points = set(wire_lines[0]) & set(wire_lines[1])
    crossing_points.remove((0,0))
    print('What are the crossing points ' + str(crossing_points))
    return min(map(lambda point: abs(point[0]) + abs(point[1]), crossing_points))

if __name__ == '__main__':
    minimal_distance = crossing(wires())
    print('What is the minimal distance ' + str(minimal_distance))

