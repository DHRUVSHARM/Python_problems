class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st, fix = [], set()

        for index, c in enumerate(s):
            if c == '(':
                st.append(index)
            elif c == ')':
                if len(st):
                    fix.add(index)
                    fix.add(st[-1])
                    st.pop()

        ans = []
        for index, c in enumerate(s):
            if c == '(' or c == ')':
                if index in fix:
                    ans.append(c)
            else:
                ans.append(c)

        return "".join(ans)
