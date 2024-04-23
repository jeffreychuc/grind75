class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {i: [] for i in range(numCourses)}  # aka adjacency list?
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # the above loop will give you a map like so
        # numCourses = 2, prerequisites = [[1,0],[0,1]]

        # {
        #     1: [0],
        #     0: [1]
        # }

        # visited = all courses along the path
        visited = set()

        def dfs(course):
            # if the course is in the visited set, it means that we have a loop
            if course in visited:
                return False
            # if the prereq for the course is empty then we can finish the class
            if prereq_map[course] == []:
                return True

            # add the course to visited for this cycle
            visited.add(course)
            # for each prereq in the list, dfs that pre
            for pre in prereq_map[course]:
                # if it had return false, return false
                if not dfs(pre):
                    return False
            # remove the course once we've done visiting
            visited.remove(course)
            # set the prereq map for that course to []
            prereq_map[course] = []
            return True

        # check all courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

