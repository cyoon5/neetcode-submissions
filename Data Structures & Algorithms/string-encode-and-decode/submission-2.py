class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "-" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        num = ""
        i = 0
        while i < len(s):
            word = ""
            if(s[i].isnumeric()):
                num += s[i]
                i+=1
            elif(s[i] == "-"):
                word = s[i+1: i+1+int(num)]
                decoded.append(word)
                i = i+1+int(num)
                num = ""

        return decoded


