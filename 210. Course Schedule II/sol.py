from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort
        def dfs(root):
            if root in cycle:
                return False
            if root in visited:
                return True

            cycle.add(root)
            for course in graph[root]:
                if dfs(course) == False:
                    return False
            visited.add(root)
            cycle.remove(root)
            res.append(root)
            return True


        res = []

        graph = {}
        # adjacency list
        for course in range(numCourses):
            graph[course] = []

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited, cycle = set(), set()
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res
        
#Time: O(V+E)