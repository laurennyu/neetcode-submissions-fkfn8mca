class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # We can scan the grid row by row to determine the local # of
        # islands, and merge if we discover that two landmasses are connected
        num_islands = 0
        # Unique island ID; this will only increase, whereas num_islands can decrease
        island_id = 0
        previous_row = [0] * len(grid[0])
        for row in grid:
            current_row = [0] * len(row)
            j = 0
            while j < len(row):
                # Check if land
                if row[j] == '1':
                    # Add land to existing island above, if present
                    if previous_row[j] != 0:
                        island_num = previous_row[j]

                    # Otherwise, create a new island
                    else:
                        num_islands += 1
                        print(j, num_islands)
                        island_id += 1
                        island_num = island_id

                    # Assign all consecutive 1s to the same island; check if any merging is needed
                    merged = set()
                    while j < len(row) and row[j] == '1':
                        other = previous_row[j]
                        if other != 0 and other != island_num:
                            # Merging
                            merge_key = tuple(sorted((island_num, other)))

                            if merge_key not in merged:
                                merged.add(merge_key)
                                num_islands -= 1

                            previous_row = [
                                elem if elem != other else island_num
                                for elem in previous_row
                            ]

                            current_row = [
                                elem if elem != other else island_num
                                for elem in current_row
                            ]
                        
                        current_row[j] = island_num
                        j += 1
                else:
                    j += 1

            previous_row = current_row

        return num_islands