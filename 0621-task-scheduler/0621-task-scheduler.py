class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = {}

        for task in tasks:
            if task not in counts:
                counts[task] = 0
            counts[task] += 1

        max_count = max(counts.values())
        max_tasks = 0

        for count in counts.values():
            if count == max_count:
                max_tasks += 1

        part_count = max_count - 1
        part_length = n + 1
        empty_slots = part_count * (part_length - max_tasks + 1)

        return max(len(tasks),(max_count - 1) * (n + 1) + max_tasks)