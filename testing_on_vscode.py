import heapq


def main():
    print("testing on vscode ...")
    arr = [1, 2, 3, -1, -1000, 2]
    heapq.heapify(arr)

    while arr:
        print(arr[0])
        heapq.heappop(arr)


main()
