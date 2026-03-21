"""

heapify algorithm implementation 

60 , 80 , 40 , 30 , 10 , 70 , 20 , 90 , 50

heap becomes 

inf , 80 , 40 , 30 , 10 , 70 , 20 , 90 , 50 , 60


"""



def heapify(arr):
    if len(arr) < 1:
        return arr

    heap = arr[:]
    heap.append(arr[0])
    heap[0] = float("-inf")

    def bubble_down(index):
        curr = index
        while curr < len(heap):
            # check if left child 
            if 2*curr >= len(heap):
                # no child stop here
                break
            else:
                # left child exist
                if 2*curr + 1 < len(heap) and (heap[2*curr + 1] < heap[2*curr]) and (heap[curr] > heap[2*curr + 1]):
                    # right child exist can swap
                    heap[curr] , heap[2*curr + 1] = heap[2*curr + 1] , heap[curr]
                    curr = 2*curr + 1
                
                
                # can move left check if swap possible 
                elif heap[curr] > heap[2*curr]:
                    heap[curr] , heap[2*curr] = heap[2*curr] , heap[curr]
                    curr = 2*curr

                # no swap possible
                else:
                    break


    for index in range(len(heap) - 1 , 0 , -1):
        bubble_down(index)
        print("intermediate : " , heap)

    arr = heap
    return arr


if __name__ == '__main__':
    arr =[90, 40, 30, 10, 50, 20, 25, 5, 60, 70, 35, 15, 45, 55, 65]
    result = heapify(arr)
    print(result)