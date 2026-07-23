#Max Heap Solution

# class Solution:
#     def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
#         heap = []
        
#         for x, y in points:
#             # Use negative distance to simulate a max-heap in Python
#             dist = -(x**2 + y**2) 
            
#             # Maintain a heap of size k
#             if len(heap) == k:
#                 heapq.heappushpop(heap, (dist, x, y))
#             else:
#                 heapq.heappush(heap, (dist, x, y))
                
#         # Extract just the coordinates from the heap tuples
#         return [[x, y] for (dist, x, y) in heap]



# Min Heap

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # 1. Create a list of tuples with positive distances: (distance, x, y)
        heap = [((x**2 + y**2), x, y) for x, y in points]
        
        # 2. Transform the entire list into a min-heap (takes O(N) time)
        heapq.heapify(heap)
        
        # 3. Pop the smallest elements k times
        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
            
        return result