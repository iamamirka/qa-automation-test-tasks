from map_generator import MapGenerator

class AppInitializer:

    def initialize(self):
        matrix = self._initialize_map()
        raft_coordinates = self._initialize_raft(matrix)
        destination = self._initialize_destination(matrix, raft_coordinates)
        print("""Application initialization was successfull!
            Map legend:
              0 - water
              1 - land
              2 - raft
              3 - place of destination
              """)

        return (matrix, raft_coordinates, destination)

    def _initialize_map(self):
        map_generator = MapGenerator()
        map_params = self._process_inserted_map_values()
        generated_matrix = map_generator.generate_map(map_params[0], map_params[1])
        print("Matrix initialized successfully!")
        self._print_matrix(generated_matrix)
        
        return generated_matrix
    
    def _initialize_raft(self, matrix):
        raft_params = self._process_inserted_raft_values(matrix)
        matrix[raft_params[0]][raft_params[1]] = 2
        print("Raft initialized successfully!")
        self._print_matrix(matrix)
        return (raft_params[0], raft_params[1])
    
    def _initialize_destination(self, matrix, raft_coordinates: (int, int)):
        destination_params = self._process_inserted_destination_values(matrix, raft_coordinates)
        matrix[destination_params[0]][destination_params[1]] = 3
        print("Destination initialized successfully!")
        self._print_matrix(matrix)
        return (destination_params[0], destination_params[1])
    
    def _process_inserted_map_values(self):
        map_width = 0
        map_height = 0
        while map_width < 2 or map_height < 2:
            try:
                map_width = int(input("Insert map width:"))
            except ValueError as error:
                print("Inserted value is not a number, insert another value")
                continue
            try:
                map_height = int(input("Insert map height:"))
            except ValueError as error:
                print("Inserted value is not a number, insert another value")
                continue
            if map_width < 2 or map_height < 2:
                print("Matrix can't be smaller than 2x2, insert another values")
        return (map_width, map_height)
    
    def _process_inserted_raft_values(self, matrix):
        spawn_x = None
        spawn_y = None
        while True:
            try:
                spawn_x = int(input("Insert raft spawn point X coordinate:")) - 1
            except ValueError as error:
                print("Inserted value is not a number, insert another value")
                continue
            try:
                spawn_y = int(input("Insert raft spawn point Y coordinate:")) - 1
            except ValueError as error:
                print("Inserted value is not a number, insert another value")
                continue
            if (spawn_y + 1 > len(matrix[0]) 
                or spawn_x + 1 > len(matrix)
                or spawn_y + 1 <= 0 
                or spawn_x + 1 <= 0):
                print("Raft is outside the map, insert another coordinates")
            elif matrix[spawn_x][spawn_y]:
                print("Raft can't be spawned on earth, insert another coordinates")
            else:
                break
        return (spawn_x, spawn_y)
    
    def _process_inserted_destination_values(self, matrix, raft_coordinates):
        destination_x = None
        destination_y = None
        while True:
            try:
                destination_x = int(input("Insert destination point X coordinate:")) - 1
            except ValueError as error:
                print("Inserted value is not a number, insert another value")
                continue
            try:
                destination_y = int(input("Insert destination point Y coordinate:")) - 1
            except ValueError as error:
                print("Inserted value is not a number, insert another value")
                continue
            if (destination_y + 1 > len(matrix[0])
                or destination_x + 1 > len(matrix) 
                or destination_y + 1 <= 0
                or destination_x + 1 <= 0):
                print("Destination is outside the map, insert another coordinates")
            elif matrix[destination_x][destination_y]:
                print("Destination can't be on earth, insert another coordinates")
            elif destination_x == raft_coordinates[0] and destination_y == raft_coordinates[1]:
                print("Destination equals raft coordinates, insert another coordinates")
            else:
                break
        return (destination_x, destination_y)
    
    def _print_matrix(self, matrix):
        for row in matrix:
            for cell in row:
                print(str(cell), end=' ')
            print()
