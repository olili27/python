class Graph:
    def __init__(self, rows:int, columns:int) -> None:
        self.rows = rows
        self.columns = columns

        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    def addCoordinates(self, x:int, y:int):
        row = y
        column = x
        self.matrix[row][column] = "d"

    def markClients(self, clients:list):
        for client in clients:
            column, row = client;
            self.matrix[row][column] = "c"


class Pair:
    def __init__(self, distance:int, driver:list) -> None:
        self.distance = distance
        self.driver = driver