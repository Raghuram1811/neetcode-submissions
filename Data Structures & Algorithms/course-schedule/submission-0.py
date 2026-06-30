class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for crs, prereq in prerequisites:
            graph[prereq].append(crs)
            indegree[crs]+=1
        
        queue = deque()
        for crs in range(numCourses):
            if indegree[crs]==0: # Meaning no further pre-requisites are needed for course 'crs', indegree A -> B means first finish A and then go to B.
                queue.append(crs)
            
        processed = 0
        while queue:

            course = queue.popleft()
            processed+=1

            for crs in graph[course]:
                indegree[crs]-=1
                if indegree[crs]==0:
                    queue.append(crs)
        return processed == numCourses
