import heapq

def min_parking_spots(intervals):
    # No cars — no parking spots needed
    if not intervals:
        return 0

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track the earliest end time
    heap = []
    max_spots = 0

    for start, end in intervals:
        # Remove cars that have left before this car arrives
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        # Add this car’s leaving time
        heapq.heappush(heap, end)
        # Track the max number of concurrent cars
        max_spots = max(max_spots, len(heap))

    return max_spots