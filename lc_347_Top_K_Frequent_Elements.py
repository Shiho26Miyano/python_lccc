class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        heap = []
        result = []

        for n in nums:
            map[n] += 1
        for ky,v in map.items():
            heappush(heap,[-v, ky])
        while k > 0:
            pair = heappop(heap)
            result.append(pair[1])
            k-=1

        return result