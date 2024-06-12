from typing import List
import collections
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we only need to return what the shortest interval is going to be
        # count the frequency of each element
        task_map = collections.defaultdict(int)
        for t in tasks:
            task_map[t] += 1

        task_freq = list(task_map.values())
        # make task freq a max heap, python only has a min heap so we can make the values negative

        task_freq = [-c for c in task_freq]
        heapq.heapify(task_freq)
        print(task_freq)
        queue = []
        interval = 0
        while task_freq or queue:
            # check if queued task can be added back into the heap
            if queue and queue[0][1] == interval:
                task = queue.pop(0)
                heapq.heappush(task_freq, task[0])
            if task_freq:
                task = heapq.heappop(task_freq)
                # NB: task is negative right now
                task += 1
                if task < 0:
                    queue.append([task, interval + n + 1])

            interval += 1

        return interval
