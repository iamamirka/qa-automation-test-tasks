import random

class MapGenerator:

    def generate_map(self, width: int, height: int):
        land_ratio = 0.3
        matrix = []
        for row_item in range(height):
            row = []
            for column_item in range(width):
                if random.random() <= land_ratio:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix