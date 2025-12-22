import collections

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st , prefix_count ,  freq = [] , [] ,  collections.defaultdict(int)

        for element in s:
            if not st or st[-1] != element:
                st.append(element)
                prefix_count.append(1)
            else:
                st.append(element)
                prefix_count.append(prefix_count[-1] + 1)
            
            # print(st)
            # print(prefix_count)

            if prefix_count[-1] == k:
                for _ in range(k):
                    st.pop()
                    prefix_count.pop()

        return "".join(st)
    
