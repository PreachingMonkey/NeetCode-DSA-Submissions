class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        max_freq = max(task_counts)
        max_freq_count = task_counts.count(max_freq)
        intervals = (max_freq - 1) * (n + 1) + max_freq_count
        return max(len(tasks), intervals)