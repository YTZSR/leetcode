class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:      
        arr.sort()
        return arr[:k]