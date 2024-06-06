import collections

if __name__ == "__main__":
    pass


class UndergroundSystem:
    __slots__ = "checkInTime", "checkOutTime", "tripInformation"

    def __init__(self):
        self.checkInTime = collections.defaultdict(list)
        self.tripInformation = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # there is a single checkin by a person at a time
        if id in self.checkInTime:
            # cannot check in already checked in person
            return
        # we can check in this person
        self.checkInTime[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # only checked in people can be checked out
        if id not in self.checkInTime:
            # can't check out if not checked in
            return
        # checking out a person
        srcStation, inTime = self.checkInTime.pop(id)
        # print(srcStation , inTime)
        # print(self.tripInformation[(srcStation , stationName)])
        if (srcStation, stationName) not in self.tripInformation:
            self.tripInformation[(srcStation, stationName)] = [0, 0]

        self.tripInformation[(srcStation, stationName)][0] += t - inTime
        self.tripInformation[(srcStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.tripInformation:
            return -1
        total_time, number_of_trips = self.tripInformation[(startStation, endStation)]
        return total_time / number_of_trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
