def sent_times():
    number_of_ports = 3
    transmission_time = 2
    packet_id = [4, 7, 10, 6]

    packet_id, time = (
        [element % number_of_ports for element in packet_id],
        [0 for _ in range(number_of_ports)],
    )
    ans = [0 for _ in range(len(packet_id))]

    for index, p_id in enumerate(packet_id):
        c_time, slot = index + 1, p_id
        # print("time : " , time)
        while not (time[slot] <= c_time):
            slot = (slot + 1) % len(time)
            c_time += 1
        # found the correct slot
        time[slot] = c_time + transmission_time
        ans[index] = slot

    print(ans)


if __name__ == "__main__":
    sent_times()
