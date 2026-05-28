class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        nums = []
    
        for i in range(len(tokens)):
            if tokens[i] not in {"*", "/", "+", "-"}:
                nums.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    nums.append(nums.pop() + nums.pop())

                elif tokens[i] == "-":
                    v1 = nums.pop()
                    v2 = nums.pop()
                    nums.append(v2 - v1)
            
                elif tokens[i] == "*":
                    nums.append(nums.pop() * nums.pop())
                
                elif tokens[i] == "/":
                    v1 = nums.pop()
                    v2 = nums.pop()
                    nums.append(int(v2 / v1))
                else:
                    nums.append(tokens[i])


        return nums.pop()


