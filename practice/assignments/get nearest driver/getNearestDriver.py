from utils import Graph, Pair


def getNearestDrivers(client:list, matrix:list, drivers:list) -> list:
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == "d":
                distance = abs(client[0] - column) + abs(client[1] - row)
                driver = [column, row]
                pair = Pair(distance, driver)

                drivers.append(pair)

    sorted_list = sorted(drivers, key = lambda pair: pair.distance)
    return sorted_list


def getNearestDriver(nearDrivers:list) -> Pair:
    if not len(nearDrivers) == 0:
        return nearDrivers.pop(0)


def getAnotherDriver(client:list, drivers:list, previousDriver:Pair, flag) -> Pair:
    while not len(drivers) == 0 and flag == "y":
        driver = getNearestDriver(drivers).driver
        print(f"{driver} is the nearest to {client}. Should we find another driver? Type \"y\" to accept or \"n\" to reject: ", end = "")

        flag = input()
        if flag == "n":
            previousDriver = driver
            break
        
    
    if len(drivers) == 0:
        print(f"There are no more drivers near {client}.")
    else:
        print(f"{previousDriver} is the driver you have chosen")

G = Graph(9, 9)

G.addCoordinates(1, 6)
G.addCoordinates(6, 8)
G.addCoordinates(5, 3)
G.addCoordinates(2, 2)
G.addCoordinates(7, 1)
G.addCoordinates(4, 6)
G.addCoordinates(8, 8)
G.addCoordinates(2, 8)
G.addCoordinates(3, 8)

flag = None

clients = [[2,8], [3,8]]

G.markClients(clients)

drivers = getNearestDrivers(clients[0], G.matrix, [])

nearestDriver = getNearestDriver(drivers).driver
print(f"{nearestDriver} is the nearest to {clients[0]}. Should we find another driver? Type \"y\" to accept or \"n\" to reject: ", end = "")

flag = input()

getAnotherDriver(clients[0], drivers, nearestDriver, flag)