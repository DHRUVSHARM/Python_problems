from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {change: 0 for change in [5, 10, 20]}

        for bill in bills:
            to_give = bill - 5

            print(changes)
            print(to_give)

            if to_give and changes[20] >= to_give // 20:
                print("here")
                changes[20] -= to_give // 20
                to_give %= 20
                print("to give : ", to_give)

            if to_give and changes[10] >= to_give // 10:
                print("here 10")
                changes[10] -= to_give // 10
                to_give %= 10
                print("to give : ", to_give)

            if to_give and changes[5] >= to_give // 5:
                print("5")
                changes[5] -= to_give // 5
                to_give %= 5
                print("to give : ", to_give)

            if to_give:
                return False

            # we have received the bill
            changes[bill] += 1

        return True
