"""
You are given a string s consisting of lowercase English letters and digits.

For each character, its mirror character is defined by reversing the order of its character set:

For letters, the mirror of a character is the letter at the same position from the end of the alphabet.
For example, the mirror of 'a' is 'z', and the mirror of 'b' is 'y', and so on.
For digits, the mirror of a character is the digit at the same position from the end of the range '0' to '9'.
For example, the mirror of '0' is '9', and the mirror of '1' is '8', and so on.


For each unique character c in the string:
Let m be its mirror character.
Let freq(x) denote the number of times character x appears in the string.
Compute the absolute difference between their frequencies, defined as: |freq(c) - freq(m)|
The mirror pairs (c, m) and (m, c) are the same and must be counted only once.

Return an integer denoting the total sum of these values over all such distinct mirror pairs.



for each c:
    calc freq[c]

for each c:
    calc mirror
    if c, mirror and mirror c not in , 
        count, put in and add to sum 
    # all other cases if seen, or reverse computed skp


    0 <= ord(c) - ord(a) < 26
        a , z - (a - a)
        b . z - (b - a)
        d , z - (d - a)

        z , z - (z - a)

        25 , 25 - (25 - 0)

    
        char , z - (char - a)

        digit , 9 - (digit - 0) 

Constraints:

1 <= s.length <= 5 * 105
s consists only of lowercase English letters and digits.

"""

import collections
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = collections.defaultdict(int)

        for ch in s:
            freq[ch] += 1

        pair_count , result = set() , 0

        for ch in s:
            mirror = None
            if 0 <= (ord(ch) - ord('a')) < 26:
                # char lowercase 
                mirror = chr(ord('z') - (ord(ch) - ord('a')))
                
            else:
                # digit 
                mirror = chr(ord('9') - (ord(ch) - ord('0')))
            
            if (ch , mirror) not in pair_count and (mirror , ch) not in pair_count:
                result += abs(freq[ch] - freq[mirror])
                pair_count.add((ch , mirror))
        
        return result