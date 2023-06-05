class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lst = [] 
        lst1 = list(set(tasks))
        lst1.sort()
        for i in range(len(lst1)):
            cnt = tasks.count(lst1[i])
            lst.append(cnt)
        print(lst) 
        lst.sort(reverse=True)
        ttl = (lst[0] - 1) * n 
        for i in range(1, len(lst)):
            ttl  -= min(lst[0]-1, lst[i])
            
        ttl = max(0, ttl) 

        return ttl + len(tasks)