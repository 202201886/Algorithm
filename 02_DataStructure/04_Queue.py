from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)  #deque([10, 20, 30])
print(queue[0])  # Peek (10)

data = queue.popleft()
print(queue)  #deque([20, 30])

if not queue:  # len(queue) == 0 
    print("Queue is empty")
else:
    print("Queue is not empty")    