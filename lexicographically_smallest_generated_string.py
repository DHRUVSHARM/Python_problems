import collections
class Solution:

    def generateString(self, str1: str, str2: str) -> str:
        n , m = len(str1) , len(str2)
        fixed = [None for _ in range(0 , m + n - 1)] # contains the fixed letter if fixed else None 
        
        # will be using the idea of intervals 

        # first is simple to mark the T posiitons correctly and verify no overlaps 
        for index in range(n - 1 , -1 , -1):
            if str1[index] == 'T':
                # need to check at this point 
                if index == (n - 1):
                    # just mark no check
                    for j in range(0 , m):
                        fixed_index = index + j
                        fixed[fixed_index] = str2[j] # mark simple 
                else:
                    # mark the first and check the rest, return "" if diff found 
                    fixed[index + 0] = str2[0] # size is atleast one and this is the first time the index is being filled 
                    for j in range(1 , m):
                        fixed_index = index + j
                        if fixed[fixed_index] is not None and fixed[fixed_index] != str2[j]:
                            # mismatch
                            return ""
                        fixed[fixed_index] = str2[j] # overwrite if possible, or already matching 
        
        # at this point we have all the fixed parts, and the non fixed ones are as None 
        # the idea is to start with the windows as intervals from left to right 
        prev_pos = -1
        for start in range(0 , n):
            if str1[start] == 'F':
                # need to consider unfixed interval
                # [start , end]
                end = start + m - 1
                if start <= prev_pos <= end and fixed[prev_pos] != str2[prev_pos - start]:
                    continue
                else:
                    # not here the prev_pos is always less than start cannot be greater than the end since fixed size intervals
                    # need to get new fixed point, or return if invalid 
                    # if get fixed equal first mark diff and break
                    # if keep recording last empty position 
                    # if diff, put as new prev_pos continue
                    # if last empty position , mark new fixed letter, make as new_prev_pos
                    # else ""

                    # mark all non fixed position in the interval as 

                    diff , force_change_candidate , prev_pos = False , -1 , -1
                    for j in range(0 , m):
                        fixed_index = start + j
                        if fixed[fixed_index] is not None and fixed[fixed_index] != str2[j]:
                            # mismatch by fixed value
                            prev_pos = fixed_index
                            diff = True
                            break

                        if fixed[fixed_index] is None:
                            # can be used definitely if not equal to a 
                            diff = True
                            if str2[j] != 'a':
                                # we can use this further candidate and assign showing we can use this 
                                prev_pos = fixed_index
                            else:
                                force_change_candidate = fixed_index # worst case if not found a 
                    
                    if not diff:
                        return ""
                    
                    if prev_pos != -1:
                        if fixed[prev_pos] is not None:
                            # already done
                            pass
                        else:
                            # can put a 
                            fixed[prev_pos] = 'a'
                    
                    elif force_change_candidate != -1:
                        # need to change the value, keep rightmost a and make it b  
                        fixed[force_change_candidate] = 'b'
                        prev_pos = force_change_candidate



        # any non fixed can be safely marked as a
        for fixed_index in range(len(fixed)):
            if fixed[fixed_index] is None:
                fixed[fixed_index] = 'a'
    
        # at this point each posiiton is fixed 
        return "".join(fixed)