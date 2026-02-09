from typing import List

"""
A transformation sequence
from word beginWord to word endWord using a dictionary 
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words,
beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

1 <= beginWord.length <= 10

endWord.length == beginWord.length

1 <= wordList.length <= 5000

wordList[i].length == beginWord.length

beginWord, endWord, and wordList[i] consist of lowercase English letters.

beginWord != endWord

All the words in wordList are unique

["dog", "dot", "hot", "log" , "lot"]

"cog"

"""

import collections
class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        if beginWord not in words:
            wordList.append(beginWord)

        # for each word, we save the pattern after moving one character and add the word to it 
        # ex  : dog
        # _og : [] , o_g : [] , do_ : []  , all three will have dog, but will also have words with one diff in the same pattern
        # dot, pushed into do_ bucket and others 
        # complexity n m 
        # reduces complexity here, but we need to combine cleverly for combining to find neighbours 

        pattern_word = collections.defaultdict(list)

        for w in wordList:
            for index in range(0 , len(w)):
                # [.... ]
                # index : will handle empty situation for start or end
                pattern = w[:index] + "_" + w[index + 1:]
                pattern_word[pattern].append(w)
        
        # print(pattern_word)

        # graph has to be looked at, with normal bfs
        # for a word 
        # we try to take each pattern possible and find the neighbours in the list, skipping the word
        # itself since it will be added as well

        visited , q , result  = set([beginWord]) , collections.deque([(beginWord , 1)]) , 0

        # bfs will reach the shortest path, and only once and we can break from that point out 
        while q:
            element , level  = q.popleft()
            # print("element popped : " , element)
            if element == endWord:
                result = level
                break

            for index in range(0 , len(element)):

                pattern = element[:index] + '_' + element[index + 1:]
                # print("pattern : " , pattern)
                for nei in pattern_word[pattern]:
                    
                    if nei != element and (nei not in visited):
                        visited.add(nei)
                        q.append((nei ,level + 1))

        
        return result



    def helper(self, w1 , w2):
        # at least one diff else false
        # we know that all the words are of the same length
        # o(10) constant
        left, right , diff_count = 0 , 0 , 0
        while left < len(w1) and right < len(w2):
            if w1[left] != w2[right]:
                diff_count += 1
            left += 1
            right += 1

        return True if diff_count == 1 else False

    def ladderLengthTLE(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case handling 
        words = set(wordList)
        if endWord not in words:
            # return 0
            return 0
        

        # beginword does not need to be in the word list
        # make graph 
        adj = collections.defaultdict(list)

        # n*n*m
        for u in range(0 , len(wordList)):
            for v in range(1 , len(wordList)):
                s , e = wordList[u] , wordList[v]
                if self.helper(s , e):
                    adj[s].append(e)
                    adj[e].append(s)
        
        # Note that beginWord does not need to be in wordList.
        # check and add it in the graph 
        if beginWord not in words:
            for index in range(0 , len(wordList)):
                s , e = beginWord , wordList[index]
                if self.helper(s , e):
                    adj[s].append(e)
                    adj[e].append(s)

       

        visited , q , result  = set() , collections.deque([(beginWord , 1)]) , float("inf")
        # we can do bfs do get the minimal length to reach the target
        while q:
            # pop the frontier 
            element , level = q.popleft()
            if element == endWord:
                # we will reach this only once , since this is bfs
                result = level
                break
            
            for nei in adj[element]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei , level + 1))
                    
        
        return 0 if result == float("inf") else result