from collections import deque

class Station:
    """
    Represents Station in the rail network. Each station is identified by
    a unique name. Station is connected with other stations - this information
    is stored in the 'neighbours' field. Two station objects with the same name are
    considered equal.
    """
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, station):
        self.neighbours.append(station)

    def __eq__(self, other):
        return isinstance(other, Station) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class TrainMap:
    """
    Represents the rail network, consisting of multiple Station objects.
    Stations in the map are bi-directionally connected.
    """
    def __init__(self):
        self.stations = {}

    def add_station(self, name):
        if name not in self.stations:
            self.stations[name] = Station(name)
        return self

    def get_station(self, name):
        return self.stations.get(name)

    def connect_stations(self, from_station, to_station):
        if not from_station or not to_station:
            raise ValueError("Station cannot be null")
        from_station.add_neighbour(to_station)
        to_station.add_neighbour(from_station)
        return self

    def shortest_path(self, from_name, to_name):
        start = self.get_station(from_name)
        end = self.get_station(to_name)

        if not start or not end:
            return []

        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current_station, path = queue.popleft()

            if current_station in visited:
                continue

            visited.add(current_station)

            if current_station == end:
                return path

            for neighbour in current_station.neighbours:
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour]))

        return []

    @staticmethod
    def convert_path_to_string_representation(path):
        return "->".join(station.name for station in path) if path else ""


def do_tests_pass():
    train_map = TrainMap()

    train_map.add_station("King's Cross St Pancras").add_station("Angel").add_station("Old Street")\
        .add_station("Moorgate").add_station("Farringdon").add_station("Barbican")\
        .add_station("Russel Square").add_station("Holborn").add_station("Chancery Lane")\
        .add_station("St Paul's").add_station("Bank")

    train_map.connect_stations(train_map.get_station("King's Cross St Pancras"), train_map.get_station("Angel"))\
        .connect_stations(train_map.get_station("King's Cross St Pancras"), train_map.get_station("Farringdon"))\
        .connect_stations(train_map.get_station("King's Cross St Pancras"), train_map.get_station("Russel Square"))\
        .connect_stations(train_map.get_station("Russel Square"), train_map.get_station("Holborn"))\
        .connect_stations(train_map.get_station("Holborn"), train_map.get_station("Chancery Lane"))\
        .connect_stations(train_map.get_station("Chancery Lane"), train_map.get_station("St Paul's"))\
        .connect_stations(train_map.get_station("St Paul's"), train_map.get_station("Bank"))\
        .connect_stations(train_map.get_station("Angel"), train_map.get_station("Old Street"))\
        .connect_stations(train_map.get_station("Old Street"), train_map.get_station("Moorgate"))\
        .connect_stations(train_map.get_station("Moorgate"), train_map.get_station("Bank"))\
        .connect_stations(train_map.get_station("Farringdon"), train_map.get_station("Barbican"))\
        .connect_stations(train_map.get_station("Barbican"), train_map.get_station("Moorgate"))

    solution = "King's Cross St Pancras->Russel Square->Holborn->Chancery Lane->St Paul's"
    print(TrainMap.convert_path_to_string_representation(
        train_map.shortest_path("King's Cross St Pancras", "St Paul's")
    ))
    return solution == TrainMap.convert_path_to_string_representation(
        train_map.shortest_path("King's Cross St Pancras", "St Paul's")
    )


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail.")
