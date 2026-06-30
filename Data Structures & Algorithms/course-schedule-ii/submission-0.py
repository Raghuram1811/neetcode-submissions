class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        graph = collections.defaultdict(list)
        return_list = []

        for crs, prereq in prerequisites:
            graph[prereq].append(crs)
            indegree[crs]+=1
        
        queue = deque()
        for crs in range(numCourses):
            if indegree[crs]==0:
                queue.append(crs)

        while queue:

            curr_course = queue.popleft()
            return_list.append(curr_course)

            for crs in graph[curr_course]:
                indegree[crs]-=1

                if indegree[crs]==0:
                    queue.append(crs)
        
        return return_list if len(return_list) == numCourses else []
