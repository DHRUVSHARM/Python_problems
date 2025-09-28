import collections


class Solution:

    def decode(self , pattern):
        return pattern.split("$")

    def encode(self , a , b , c):
        return "$".join([a , b , c])

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        elements = [(t , w , u) for t , w , u in zip(timestamp , website, username)]
        # sort by time
        elements.sort(key = lambda element : element[0])

        # used to determine the final patterns at least one is there
        patterns = collections.defaultdict(int)

        # map the users to the visited websites in order
        user_website_mapping = collections.defaultdict(list[int])

        for t , w , u in elements:
            user_website_mapping[u].append(w)
        
        # now we go through each of the mapped paths and get the pattern counts
        for user, website_visit_order in user_website_mapping.items():
            for i in range(0 , len(website_visit_order) - 2):
                for j in range(i + 1 , len(website_visit_order) -1):
                    for k in range(j + 1 , len(website_visit_order)):
                        visit_pattern = self.encode(website_visit_order[i] , website_visit_order[j] , website_visit_order[k])
                        patterns[visit_pattern] += 1

        count_patterns = [(count , pattern) for pattern , count in patterns.items()]
        count_patterns.sort(key = lambda element : (-1 * element[0] , element[1]))
        decoded_pattern = self.decode(count_patterns[0][1])

        return decoded_pattern

            
        