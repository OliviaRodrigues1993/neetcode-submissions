class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} #making a empty dict
        for word in strs: #for each words
            key = tuple(sorted(word))
            #print("key=",key)
            if key not in groups: #if not seen yet
                groups[key]=[] #intitalize 
            groups[key].append(word)
        return list(groups.values())

        