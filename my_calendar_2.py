class MyCalendarTwo:

    def __init__(self):
        # first we initalize the lists for accepted intervals and double overlaps
        self.accepted = []
        self.double_cross = []


    def book(self, start: int, end: int) -> bool:
        # print("(" , start , "," , end , ")")


        if not self.accepted:
            # first time here ...
            
            self.accepted.append((start , end))
            return True
        else:
            
            # first check if we can add this or not
            for s , e in self.double_cross:
                if not (end <= s or start >= e):
                    
                    return False
            
            for s , e in self.accepted:
                if end <= s or start >= e:
                    # we can add this without any issues for this case 
                    pass
                else:
                    # there is an overlap , need to add it
                    # print("here : " , start , " , " ,  end , " : " , s , " , " , e)
                    self.double_cross.append((
                        max(s , start),
                        min(e , end)
                    ))
                

            self.accepted.append((start , end))
            return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)