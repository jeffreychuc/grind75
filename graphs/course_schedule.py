# 207. Course Schedule
# Medium
# Topics
# Companies
# Hint
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and
# to take course 0 you should also have finished course 1. So it is impossible.
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

from typing import List


# def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
#     # init empty arrays into prereq map
#     # can also do it pythonic like so
#     # prerequisites_map = {i: [] for i in range(numCourses)}
#     prerequisites_map = {}
#     for i in range(numCourses):
#         prerequisites_map[i] = []
#
#     for course, prereq in prerequisites:
#         prerequisites_map[course].append(prereq)
#
#     visit_set = set()
#
#     def dfs(course: int):
#         # if the course was already visited we can't finish the schedule
#         # because we've visited a course twice so the DAG is looping
#         if course in visit_set:
#             return False
#         if prerequisites_map[course] == []:
#             return True
#         visit_set.add(course)
#         print(visit_set)
#         for pre in prerequisites_map[course]:
#             # if one course returns false, we can return false for all the prereqs
#             # why cant you just return dfs(pre)?
#             if not dfs(pre):
#                 return False
#         visit_set.remove(course)
#         prerequisites_map[course] = []
#         return True
#
#     for course in range(numCourses):
#         if not dfs(course):
#             return False
#     return True

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    prereq_map = {i: [] for i in range(numCourses)}  # aka adjacency list?
    indegree_map = {i: 0 for i in range(numCourses)}

    for course, pre in prerequisites:
        prereq_map[course].append(pre)
        # prereq_map_back[pre].append(course)
        indegree_map[course] += 1

    print(prereq_map)
    print(indegree_map)


print(canFinish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))
