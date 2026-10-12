class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """DFS"""
        
        con_map = { i: [] for i in range(numCourses)}

        for i in range(len(prerequisites)):
            f, s = prerequisites[i][0], prerequisites[i][1]
            con_map[f].append(s)

        
        visited = set()

        def dfs(crs):
            
            # if course was visited already Meaning its a cycle
            if crs in visited:
                return False

            # if course has no pre-req then we can complete it
            if con_map[crs] == []:
                return True

            # Add the current course to visited
            visited.add(crs)

            # go though its pre-req
            for pre in con_map[crs]:
                if not dfs(pre): 
                    return False
            
            # we chekced it pre_req for cycle and its own pre-req
            visited.remove(crs)
            con_map[crs] = [] # So next time we dont run DFS on this course if it is memeber of some other course pre-req
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        