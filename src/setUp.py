import random

#machines name, id, capacity pcs, time in hours
machines = [
    { "name": "A", "id": 0, "capacity":50, "time": 1},
    { "name": "B", "id": 1, "capacity": 150, "time": 4},
    { "name": "C", "id": 2, "capacity": 1, "time": 0.25},
    { "name": "D", "id": 3, "capacity": 1, "time": 0.3},
    { "name": "E", "id": 4, "capacity": 1, "time": 0.5},
    { "name": "F", "id": 5, "capacity": 2, "time": 0.75},
    { "name": "G", "id": 6, "capacity": 1, "time": 0.5},
    { "name": "H", "id": 7, "capacity": 2, "time": 0.75}
]

waferCount = 100
failureRate = 0.05
flow = [0, 1, 2, 3, 4, 5, 4, 0, 6, 1, 7, 2]

def generateWafers(count, flow):
    wafers = []
    for i in range(count):
        #init random wafers for opt
        layerCount = random.randrange(30, 80)
        new = {"id": i, "layerCount": layerCount, "flow": layerCount * flow}
        wafers.append(new)
    return wafers

def main():
    pass

if __name__ == "__main__":
    main()