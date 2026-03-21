from typing import List

"""

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]


pack as many words as possible in each line 
' ' to maintain characters
distribute evenly 
if more, than start from left 
last line has to be left justified 





"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines , index , line_index = [] , 0 , 0

        while index < len(words):
            # need to include [index ... ] onwards
            line , line_index = [] , index
            space_count , char_count = -1 , 0

            while line_index < len(words):
                space_count += 1
                limit = len(words[line_index]) + space_count + char_count
                if limit <= maxWidth:
                    # include
                    if space_count:
                        line.append(' ')
                    
                    line.append(words[line_index])
                    char_count += len(words[line_index])
                else:
                    # stop considering
                    space_count -= 1 
                    break
                # considered, move to next word
                line_index += 1


            # we have considered till line_index - 1
            remainder_spaces = maxWidth - (char_count + space_count)
            # print("remainder spaces : " , remainder_spaces)
            # process line
            if line_index == len(words) or len(line) == 1:
                # last line, needs to be left justified
                # "shall be        "
                # case 2 single word , "acknowledgment  ",
                # can handle both here 
                # we already have so all we need we have to do is add the remaining in the end
                line.append(' ' * remainder_spaces)
            else:
                # normal justify logic
                # case 1 "What   must   be",                
                # pass one take the remainder spaces and buckets, and put as many equally
                initial_spaces = remainder_spaces // space_count
                # print("inital spaces " , space_count)
                for index in range(1 , len(line) , 2):
                    line[index] += (initial_spaces * ' ')
                
                next_spaces = remainder_spaces % space_count
                # print("next spaces " , next_spaces)
                # we can distribute at least one at each count 
                for index in range(1 , len(line) , 2):
                    if not next_spaces:
                        break
                    line[index] += ' '
                    next_spaces -= 1


            
            line_str = ''.join(line)
            lines.append(line_str)
            # we stop if line_index has reached len(words) or cannot put line_index word
            index = line_index

        return lines
            

                
        
        
