import collections
import heapq
from typing import List

import sortedcontainers
from sortedcontainers import SortedSet

if __name__ == "__main__":
    a = set()
    a.add(5)
    a.add(4)
    a.add(3)

    print(a)

    x = []
    heapq.heappush(x, 3)
    heapq.heappush(x, 1)
    heapq.heappush(x, 2)

    print(x[0])

    print("sorted set container ..")
    ss = sortedcontainers.SortedSet([3, 3, 2, 1])
    print(ss)


class FoodRatings:
    __slots__ = "food_rating", "cuisine_mapping"

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = collections.defaultdict(list)
        # maps food to the rating and the cuisine it belongs to
        self.cuisine_mapping = collections.defaultdict(SortedSet)
        # maps cuisine to sorted set of tuple values (rating , food_string)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_rating[food] = [rating, cuisine]
            self.cuisine_mapping[cuisine].add((-1 * rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.food_rating[food]
        self.food_rating[food][0] = newRating
        self.cuisine_mapping[cuisine].remove((-1 * rating, food))
        self.cuisine_mapping[cuisine].add((-1 * newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_mapping[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
