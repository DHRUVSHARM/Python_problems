class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        for this problem we will use the concept of clamping 
        the shoretest distance for a circle can be got by connecting circle to the side 

        if the distance is greater than r then that means that they do not overlap 

        """

        clamp_x , clamp_y = min(x2 , max(x1 , xCenter)) , min(y2 , max(y1 ,yCenter))

        # print(clamp_x , " : " , clamp_y)

        return ((clamp_x - xCenter) ** 2 + (clamp_y - yCenter) ** 2) <= (radius ** 2)