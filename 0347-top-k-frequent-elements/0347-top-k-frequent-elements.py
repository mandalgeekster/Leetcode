from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        count  = [] 
        setof = list(set(nums))
        for i in range(len(setof)):
            cnt = nums.count(setof[i])
            lst.append(cnt)
        count.sort()
        '''
        myDict = defaultdict(int)
        for i in nums:
            myDict[i] += 1
        
       # myKeys = list(myDict.values())
       # myKeys.sort(reverse=True)
       # sorted_dict = {i: myDict[i] for i in myKeys}
       # print(myDict)
       # print(sorted_dict)
        sorted_dict = dict(sorted(myDict.items(), key=lambda item: item[1], reverse=True))
        #return sorted_dict
        print(sorted_dict)
        lst = [] 
        for i in sorted_dict.keys():
              lst.append(i)
        return lst[:k]
            
        
        