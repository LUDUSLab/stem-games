
class Node:
    def __init__(self, rel=None, pos=None):
        self.rel = rel
        self.pos = pos

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos

    def reset(self):
        self.g = self.h = self.f = 0


class Astar:
    open_list = []
    closed_list = []
    map = [[0 for i in range(30)] for j in range(14)]

    def __init__(self, start, end):
        self.start_node = Node(None, start)
        self.end_node = Node(None, end)

    def reset(self):
        self.start_node.reset()
        self.end_node.reset()

    def run(self):
        self.reset()
        self.open_list.append(self.start_node)
        while len(self.open_list) > 0:
            actual_node = self.open_list[0]
            actual_index = 0
            for index, item in enumerate(self.open_list):
                if item.f < actual_node.f:
                    actual_node = item
                    actual_index = index

            self.open_list.pop(actual_index)
            self.closed_list.append(actual_node)

            if actual_node == self.end_node:
                path = []
                current = actual_node
                while current is not None:
                    path.append(current.pos)
                    current = current.rel
                return path[::-1]

            successors = []
            for pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # adyacentes
                node_position = (actual_node.pos[0] + pos[0], actual_node.pos[1] + pos[1])
                if node_position[0] > (len(self.map) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(self.map[len(self.map) - 1]) - 1) or node_position[1] < 0:
                    continue

                if self.map[node_position[0]][node_position[1]] != 0:
                    continue

                new_node = Node(actual_node, node_position)
                successors.append(new_node)

            for successor in successors:
                for closed_child in self.closed_list:
                    if successor == closed_child:
                        continue

                successor.g = actual_node.g + 1
                successor.h = ((successor.pos[0] - self.end_node.pos[0]) ** 2) + (
                            (successor.pos[1] - self.end_node.pos[1]) ** 2)
                successor.f = successor.g + successor.h

                for open_node in self.open_list:
                    if successor == open_node and successor.g > open_node.g:
                        continue

                self.open_list.append(successor)