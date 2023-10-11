class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        total_alice=sum(aliceSizes)
        total_bob=sum(bobSizes)
        total_target=(total_alice-total_bob)//2
        alice_count=set(aliceSizes)
        for b in bobSizes:
            alice_req=b+total_target
            if alice_req in alice_count:
                return [alice_req,b]
        return []
        