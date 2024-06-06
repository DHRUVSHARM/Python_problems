if __name__ == "__main__":
    pass


class ParkingSystem:
    __slots__ = "parking_spaces"

    def __init__(self, big: int, medium: int, small: int):
        self.parking_spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking_spaces[carType - 1] == 0:
            return False
        self.parking_spaces[carType - 1] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
