"""
A part of the UWCS programming competition.

Place points in an initially empty NxN grid, such that the total distance
between all placed points is minimised. Need to place incrementally adjacent.
"""

from sys import argv
from typing import List, Tuple

Position = Tuple[int, int]


def manhattan_distance(pos_from: Position, pos_to: Position) -> int:
    """Get the manhattan distance between two position."""
    return abs(pos_from[0] - pos_to[0]) + abs(pos_from[1] - pos_to[1])


class Grid:
    def __init__(self, size: int):
        """Create a grid of the specified size."""
        if size < 1:
            raise ValueError("Grid size must be a positive integer")
        self.size = size
        self.data: List[List[int]] = [
            [0 for _ in range(size)]
            for _ in range(size)
        ]

    def positions_at_distance(self, position: Position, distance: int) -> List[Position]:
        """Get the list of unoccupied positions at a distance from a center point."""
        positions: List[Position] = []
        for y in range(self.size):
            for x in range(self.size):
                if manhattan_distance(position, (x, y)) == distance and not self.data[y][x]:
                    positions.append((x, y))
        return positions

    def place_agents(self, num_agents: int) -> List[Position]:
        """Return a list of agents placed in the grid."""
        agents: List[Position] = []

        if self.size ** 2 < num_agents:
            raise ValueError("Board too small to contain all agents")

        for agent_num in range(num_agents):
            if agent_num == 0:
                mid = self.size // 2
                agents.append((mid, mid))
                self.data[mid][mid] = 1
                continue

            count = 1
            place = None
            while count < self.size and not place:
                positions = self.positions_at_distance(agents[0], count)
                min_distance = None

                for pos in positions:
                    distance = 0
                    for agent in agents:
                        distance += manhattan_distance(pos, agent)

                    if min_distance is None or distance < min_distance:
                        place = pos
                        min_distance = distance

                count += 1

            if place:
                agents.append(place)
                self.data[place[1]][place[0]] = 1

        return agents

    def fibonaccify_grid(self) -> None:
        """Turn active cells in the grid into fibonacci numbers."""
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                if cell != 0:
                    self.data[y][x] = fibonacci(x * y)
                    print(f"{x} {y} {x * y}")

    def __str__(self) -> str:
        """Get a string representation of the grid."""
        result = ""
        for row in self.data:
            for element in row:
                result += f"{element} "
            result += "\n"
        return result


def fibonacci(n: int) -> int:
    """Get the nth fibonacci number."""
    if n < 2:
        return n
    fib_prev = 1
    fib = 1
    for _ in range(2, n):
        tmp = fib_prev
        fib_prev = fib
        fib = (fib + tmp) % 997
    return fib


if __name__ == "__main__":
    if len(argv) != 3:
        raise RuntimeError("Numeric arguments for the grid size and number of agents must be provided!")
    try:
        grid_size, num_agents = int(argv[1]), int(argv[2])
    except ValueError as err:
        raise RuntimeError("Arguments must be integers!") from err
    grid = Grid(grid_size)
    grid.place_agents(num_agents)
    grid.fibonaccify_grid()
    print(grid)
