class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        lists = []
        for n in nums:
            res[n] += 1
        for key, value in res.items():
            lists.append([value, key])
        lists.sort()

        r = []
        while len(r) < k:
            r.append(lists.pop()[1])
        return r



        
                
