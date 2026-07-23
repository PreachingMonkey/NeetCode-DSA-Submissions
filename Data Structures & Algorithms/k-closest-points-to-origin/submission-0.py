class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        
        for x, y in points:
            # Use negative distance to simulate a max-heap in Python
            dist = -(x**2 + y**2) 
            
            # Maintain a heap of size k
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
                
        # Extract just the coordinates from the heap tuples
        return [[x, y] for (dist, x, y) in heap]