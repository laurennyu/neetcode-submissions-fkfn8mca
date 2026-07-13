class TimeMap:

    def __init__(self):
        # mapping of key to [(timestamp, value)]
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapping:
            self.mapping[key].append((timestamp, value))
        else:
            # Add this key to the mapping
            self.mapping[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        
        tups = self.mapping[key]
        # binary searches for timestamp for O(logn) runtime
        i = 0
        j = len(tups) - 1
        while i <= j:
            mid = (i + j) // 2
            if tups[mid][0] == timestamp:
                return tups[mid][1]
            elif tups[mid][0] > timestamp:
                j = mid - 1
            else:
                i = mid + 1

        if i < len(tups) and tups[i][0] < timestamp:
            return tups[i][1]
        elif i > 0 and tups[i-1][0] < timestamp:
            return tups[i-1][1]

        return ""