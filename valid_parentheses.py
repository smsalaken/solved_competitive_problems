class Solution:
    
        
    def isValid(self, s: str) -> bool:
        mapper = {'{' : '}', '(' : ')', '[' : ']'}
        
        if len(s) == 1 or len(s) %2 != 0:
            return False
        
        stack = []
        for letter in s :
            # print('letter : {}'.format(letter))
            # first letter and it is openning parentheses
            if not stack and letter in mapper.keys() :
                stack.append(letter)
            # first letter and closing parentheses
            elif not stack and letter not in mapper.keys() :
                return False
            # if subsequent letters are also openning letters    
            elif stack and letter in mapper.keys():
                stack.append(letter)
            elif stack and letter not in mapper.keys():
                # not first letter and not open parenthesis
                if letter == mapper.get(stack[-1]):
                    # remove the last letter as pair matched
                    _ = stack.pop()
                else: 
                    return False
            
        # an empty stack means all items has been matched        
        if not stack:
            return True
        else:
            return False
                
            
        
    
            
                
            
        