import heapq

heap = []

heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)

result = heapq.heappop(heap)
print(result)
print(heap)