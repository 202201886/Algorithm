stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)  # [10, 20, 30]

stack.pop()  #take and delete the last element 
data = stack.pop(0) #pop element in index 0
print(data)  #10
print(stack)  #[20]

if not stack:  #len(stack) == 0
    print("Stack is empty")
else:
    print("Stack is not empty")