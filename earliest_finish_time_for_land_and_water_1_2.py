from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        """
        we have land rides and water rides
        we have start + duration for each giving end times, 
        calculate all end times, pick min end time


        sorted by start time and <= end time  
        check for the lowest end time how many rides can be opened and keep track of one with lowest duration 
        if none found then the next one can be the one we take which will take up end time 

        """
        
        min_land_end_time = min(sorted([(s + d) for s , d in zip(landStartTime , landDuration)]))
        min_water_end_time = min(sorted([(s + d) for s , d in zip(waterStartTime , waterDuration)]))

        # sorted by start time 
        land_details = sorted((s , d) for s , d in zip(landStartTime , landDuration))
        water_details = sorted((s , d) for s , d in zip(waterStartTime , waterDuration))

        ans = float("inf")
        # first take land
        
        res = min_land_end_time
        other = float("inf")
        index = 0

        while index < len(water_details):
            water_s , water_d = water_details[index]
            if water_s <= res:
                # can open consider duration
                other = min(other, water_d) # simple add duration 
                index += 1 
            else:
                # no need to move forward 
                break
            
        # continue checking and adding the min end time for this point on for start > index we broke off 
        while index < len(water_details):
            water_s , water_d = water_details[index]
            other = min(other , (water_s - res + water_d))
            index += 1
        
        ans = min(ans , res + other)

        # now same for first take water 

        res = min_water_end_time
        other = float("inf")
        index = 0

        while index < len(land_details):
            land_s , land_d = land_details[index]
            if land_s <= res:
                # can open
                other = min(other, land_d) # simple add duration instant start after finishing this 
                index += 1
            else:
                # stop here
                break
        
        # remaining land_s > min water end time 
        while index < len(land_details):
            land_s , land_d = land_details[index]
            other = min(other , land_s - res + land_d)
            index += 1
        
        ans = min(ans , res + other)

        return ans


