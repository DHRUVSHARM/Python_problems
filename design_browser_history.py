"""
You have a browser 
of one tab where you start 
on the homepage and you 
can visit another url, 
get back in the history number 
of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
homepage, so we can
start - hp - end

[
    hp: ref
]


void visit(string url) Visits url from the current page. It clears up all the forward history.

# visit url from the current page 



string back(int steps) Move steps back in history.
If you can only return x steps in the history and steps > x, 
you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. 
If you can only forward x steps in the history and steps > x, 
you will forward only x steps. Return the current url after forwarding in history at most steps.
 

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]


    "leetcode.com" - "google.com" - "facebook.com - linkedin

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
 

Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.

ll is good idea 

front   <>    back

b        curr           f
None    leetcode.com  None 

insert
node.prev = curr
node.next = f

# decouple step

curr.next 
d - v - c - a - NULL

curr.next.prev = None if curr.next 
front.prev.next = nONE IF FRONT.PREV

curr.next = node
f.prev = node if f.prev

curr = curr.next 



insert (back , curr, front):
will put bw curr and front , and and skip remaining if front out 

"""

# optimized solution with dll and O(1) time complexity for all operations 
class DLL:
    def __init__(self , val , prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = DLL(homepage)
        self.size = 1 # the indices will be from 0 to size - 1
        self.index_map = {0 : self.curr}
        self.curr_index = self.size - 1


    def insert(self, curr , front , node):
        
        if not node:
            return

        node.prev = curr
        node.next = front 

        if curr and curr.next:
            curr.next.prev = None
        
        if front and front.prev:
            front.prev.next = None
        
        curr.next = node
        
        if front and front.prev:
            front.prev = node

    def visit(self, url: str) -> None:
        node = DLL(url)

        self.insert(self.curr, None , node) # skip all forward 

        # new next to self.curr will be node, so safe to do this 
        self.curr = self.curr.next

        # remove old values, adjust size 
        self.size = self.size - (self.size - (self.curr_index + 1))

        # assing to index
        self.size += 1
        if (self.size - 1) not in self.index_map:
            self.index_map[self.size -1] = None
        
        # note indices do not change, only overwrite 
        self.index_map[self.size - 1] = self.curr # replace with current 
        self.curr_index = self.size - 1

        
    def back(self, steps: int) -> str:
        # constant op 
        self.curr_index = max(self.curr_index - steps , 0) 
        self.curr = self.index_map[self.curr_index] # move 

        return self.curr.val 

    def forward(self, steps: int) -> str:
        # constant op 
        self.curr_index = min(self.curr_index + steps, self.size - 1)
        self.curr = self.index_map[self.curr_index] # move
        
        return self.curr.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)