class Solution:

    
    def encode(self, strs: List[str]) -> str:
       
        encode_list = []
        for letters in strs:
            #print(letters)
            #print(len(letters))
            encode_list.append(str(len(letters))+"#"+letters)
            #print(encode_list)
        return "".join(encode_list)

    def decode(self, strs: List[str]) ->str:
        result = []
        i = 0 #current position in the string
        while i < len(strs):
            j =strs.find("#",i)#where this length number ends
            length = int(strs[i:j]) #digits between i and the "#"
            word = strs[j+1 :j+1+length] #the next length characters
            #print("word",word)

            result.append(word)
            #print("result",result)
            i = j+1+length #jump to start of next number
            #print("i=",i)
        return result            
        
        




    
