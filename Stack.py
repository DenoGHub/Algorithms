# A stack is a data structure concept.
class Stack:

    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False


# The function checks if the variable 'to_check' has all the brackets closed or not.
def inspect_syntax(to_check):
    for i in range(len(to_check)):
        if to_check[i] == '(':
            stack.push(to_check[i])
        elif not stack.is_empty():
            stack.pop()
        else:
            print('Not all brackets are closed')
            return False
    if stack.is_empty():
        print('All brackets are closed')
        return True
    else:
        print('Not all brackets are closed')
        return False


stack = Stack()
to_check = '(()))'
inspect_syntax(to_check)

