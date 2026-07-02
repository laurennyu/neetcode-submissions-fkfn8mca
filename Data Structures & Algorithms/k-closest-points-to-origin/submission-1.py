class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        closest_points = [] # max heap
        for point in points:
            dist = point[0]**2 + point[1]**2
            if len(closest_points) < k:
                heapq.heappush(closest_points, (-dist, tuple(point)))
            elif dist < -closest_points[0][0]:
                heapq.heappop(closest_points)
                heapq.heappush(closest_points, (-dist, tuple(point)))

        return [list(point[1]) for point in closest_points]