class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for each_value in nums:
            seen[each_value] = seen.get(each_value,0)+1
        print("seen[value]=",seen.values())

        sorted_numbers = sorted(
            seen,
            key = seen.get,
            reverse = True
        )
        #print(sorted_numbers)
        return sorted_numbers[:k]
        