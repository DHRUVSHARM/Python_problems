class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st , balance , diff = [] , 0 , {'(' : 1 , ')' : -1}
        for element in s:
            if element == '(' or element == ')':
                if balance + diff[element] < 0:
                    pass
                else:
                    balance += diff[element]
                    st.append(element)
            else:
                st.append(element)
            
        # we know that the balance has to be >= 0
        index = len(st) - 1
        while index >= 0 and balance > 0:
            element = st[index]
            if element == '(':
                balance -= diff[element]
                st[index] = ""
            index -= 1
            
        return "".join(st)