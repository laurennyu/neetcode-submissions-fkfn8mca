class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create mapping of prereq to course
        edges = {}
        for prereq in prerequisites:
            if prereq[1] in edges.keys():
                edges[prereq[1]].append(prereq[0])
            else:
                edges[prereq[1]] = [prereq[0]]
        
        # Find if there are any cycles
        visited_nodes = set()
        for course in list(range(numCourses)):
            if course not in visited_nodes and course in edges:
                # Start DFS on unvisited node to see if there is a cycle
                seen = set()
                courses_to_visit = [course] # should only have unvisited & unseen nodes
                while len(courses_to_visit) > 0:
                    curr = courses_to_visit.pop()
                    seen.add(curr)
                    for nbr in edges[curr]:
                        if nbr in seen:
                            # Cycle!
                            return False
                        if nbr not in visited_nodes and nbr in edges:
                            courses_to_visit.append(nbr)


                        visited_nodes.add(nbr)

            visited_nodes.add(course)
        return True
    