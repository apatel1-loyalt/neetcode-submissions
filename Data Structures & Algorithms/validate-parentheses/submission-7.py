class Solution:
    def isValid(self, s: str) -> bool:
        # You can remove the pairs and the find the lenght of the sting
        # if it is zero then it is valid else not

        tmp_arr = []

        for char in s:
            
            # Adding the brackets if it is starting
            if char == '[' or char == '{' or char == '(':
                tmp_arr.append(char)
            # Removing if we find the closing bracket 
            elif len(tmp_arr) != 0:
                if char == ']' and tmp_arr[-1] == '[':
                    tmp_arr.pop()
                elif char == '}' and tmp_arr[-1] == '{':
                    tmp_arr.pop()
                elif char == ')' and tmp_arr[-1] == '(':
                    tmp_arr.pop()
                else:
                    return False
            else:
                return False


        if len(tmp_arr) == 0:
            return True 
        
        print(tmp_arr)
        return False        