class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum , n , minimal_element , negative_count = 0 , len(matrix) , float("inf") , 0
        for i in range(0 , n):
            for j in range(0 , n):
                if matrix[i][j] < 0:
                    negative_count += 1
                sum += abs(matrix[i][j])
                minimal_element = min(minimal_element , abs(matrix[i][j]))
        
        if minimal_element == 0 or negative_count % 2 == 0:
            return sum
        else:
            return sum - 2 * minimal_element
