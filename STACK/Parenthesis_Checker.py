# Input:
# {([])}
# Output: 
# true
# Explanation: 
# { ( [ ] ) }. Same colored brackets can form 
# balaced pairs, with 0 number of 
# unbalanced bracket.

class Para_check:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "$"
    def check(self,problem):
        for i in problem:
            if i in  ("{", "(" , "["):
                self.push(i)
            else:
                if not self.stack:
                    return False
                else:
                    curr_pan=self.stack.pop()
                    if i=="}":
                        if curr_pan!="{":
                            return False
                    elif i=="]":
                        if curr_pan!="[":
                            return False
                    elif i==")":
                        if curr_pan!="(":
                            return False

        if self.stack:
            return False            
        return True


if __name__ == '__main__':
    problem="[({[([{}])]})}"
    obj=Para_check()
    print(obj.check(problem))
    