# --- Day 6: Universal Orbit Map ---

def count_orbits():
    lines = []
    nr = 0
    with open('input1.txt') as file:
        for line in file:
            center, orbitting_object = line.strip('\n').split(')')
            lines.append((center, orbitting_object))
    for line in lines:
        nr += 1
        # object = line[1]
        center = line[0]
        print(f"Investigating object {line[1]} with center {center}")
        while center != 'COM':
            new_pair = list(filter(lambda x: x[1] == center, lines))
            if len(new_pair) == 0:
                break
            else:
              nr += 1
              # print(f"New pair {new_pair}")
              object = new_pair[0][1]
              center = new_pair[0][0]

    return nr


def transfer_between_object_of_sam_and_object_of_you():
    lines = []
    with open('input1.txt') as file:
        for line in file:
            center, orbitting_object = line.strip('\n').split(')')
            lines.append((center, orbitting_object))
    


if __name__ == '__main__':
    # direct_orbits, indirect_orbits = count_orbits()
    nr_lines = count_orbits()
    print(f"Number of lines {nr_lines}")
