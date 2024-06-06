import heapq


def main():
    # Open the input file
    with open("input.txt", "r") as file:
        # Read the number of cracks
        n = int(file.readline().strip())

        # Read the threshold for flooding
        threshold = int(file.readline().strip())

        # Read the amount of water that drains out each time unit
        drain_rate = int(file.readline().strip())

        # Initialize a list to store crack information
        cracks = []

        # Read input for each crack
        for _ in range(n):
            crack_info = file.readline().strip()
            # Split the input and convert each part to int
            time_unit, size = map(int, crack_info.split())
            # Store the converted values
            cracks.append((time_unit, size))

        cracks.append((10**7, -1))

    # Store inputs in a dictionary for easy access or manipulation
    dam_data = {
        "n": n,
        "threshold": threshold,
        "drain_rate": drain_rate,
        "cracks": cracks,
    }

    # For demonstration: print the collected data
    # print("Collected input data from file:")
    print(dam_data)

    """
    maxHeap = []
    heapq.heapify(maxHeap)

    for t, s in cracks:
        heapq.heappush(maxHeap, (-1 * s, -1 * t))

    while len(maxHeap):
        s, t = heapq.heappop(maxHeap)
        element = (-1 * t, -1 * s)
        print(element)
         
    """

    print("*******************************************************")

    # this keeps track of the previous time
    max_flood_level_reached = float("-inf")
    prev_time = -1
    # this is the current time
    current_time = prev_time
    flood_level = 0
    inflow = 0
    crack_increase = 0
    maxHeap = []
    heapq.heapify(maxHeap)

    for index, val in enumerate(cracks):

        appear_time, appear_size = val
        print("appear time : ", appear_time, " ", "appear_size : ", appear_size)
        print("prev_time : ", prev_time)

        if appear_time != prev_time:
            print("popping , and calculating , new time bucket .... ")
            while len(maxHeap) and current_time < appear_time:

                biggest_crack, insert_time = heapq.heappop(maxHeap)
                crack_increase = (len(maxHeap) + 1) * (current_time - insert_time)
                biggest_crack *= -1
                adjusted_biggest_crack = biggest_crack + (current_time - insert_time)
                # size of the biggest crack after increase

                flood_level = max(
                    flood_level
                    + inflow
                    + crack_increase
                    - drain_rate
                    - adjusted_biggest_crack,
                    0,
                )
                max_flood_level_reached = max(max_flood_level_reached, flood_level)

                print(
                    f"Biggest crack before adjustment: {-biggest_crack}, Insert time: {insert_time}, "
                    f"Current time: {current_time}, Adjusted biggest crack size: {adjusted_biggest_crack}, "
                    f"New flood level: {flood_level}, with components - Inflow: {inflow}, Crack increase: {crack_increase}, "
                    f"Drain rate: {drain_rate}"
                )

                if flood_level >= threshold:
                    print("FLOOD !!!!")
                    print(
                        " flood_level , current_time : ",
                        flood_level,
                        " , ",
                        current_time,
                    )
                    return

                inflow -= biggest_crack
                current_time += 1

                print(
                    "current_time : ",
                    current_time,
                    " ",
                    "crack_increase : ",
                    crack_increase,
                )

            print("done popping and all .....\n")

            if not len(maxHeap):
                print("discontinuity ...")
            else:
                print("overlapping , we need to reset ...")
                elements = []
                while len(maxHeap):
                    cs, ct = heapq.heappop(maxHeap)
                    cs *= -1
                    inflow -= cs
                    adjusted_size = cs + (current_time - ct)
                    inflow += adjusted_size
                    elements.append((-1 * adjusted_size, current_time))

                print("the elements are : ", elements)
                # empty heap , but some overlapping intervals
                # o(n)
                maxHeap = elements
                heapq.heapify(maxHeap)
                print("the heap now is as : ")
                print(maxHeap)

            # deal with overlaps and all
            prev_time = appear_time
            # fast-forward
            print("fast forwarding .. ", current_time)

            flood_level = max(
                flood_level - drain_rate * (appear_time - current_time), 0
            )
            print("flood level as a result of fast-forwarding : ", flood_level)
            current_time = prev_time
            print(
                "new prev , and current time forwarded ... ",
                prev_time,
                " , ",
                current_time,
            )

        # keep pushing
        print("simple push ..")
        heapq.heappush(maxHeap, (-1 * appear_size, appear_time))
        print("state of heap : ", maxHeap)

        inflow += appear_size

    print("*******************************************************")
    print("reaching here means that the village is safe ...")
    print("SAFE")
    print(max_flood_level_reached)


if __name__ == "__main__":
    main()
