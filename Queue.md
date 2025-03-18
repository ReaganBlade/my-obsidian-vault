 
Type -> Linear
Restricted -> True [One end for Insertion and One End for Deletion]
By Default - Dynamic

**Operations: **
1. Insertion -> Enqueue: Done from the end
2. Deletion -> Dequeue: Done from the front
3. Peek -> See the front Element
4. isEmpty -> Check if Empty
5. isFull -> Check if Full
### **Applications**
1. CPU Scheduling
2. Printer Queue
3. Call Center Systems
4. Graph Algorithm - BFS
5. Data Buffering
6. Network Queues
7. Tree Traversal

### Disadvantages
1. Poor Mem Utilization
2. Traversal


### **Types**
1. Simple Queue/Linear Queue
2. Double Ended Queue
3. Circular Queue
4. Priority Queue

Detail
1. **Linear Queue**
	**Disadvantage of Linear Queue**
	When we have space in linear queue but we cannot insert the value, because of overflow error. That condition is called poor memory utilization.

2. **Circular Queue / Ring Buffer**
	Why needed? -> because of Poor Mem Utilization of Linear Queue.
	static -> queue
	
3. **Double Ended Queue (Deque)**
	 Sliding Window Technique



## Queue Algorithms

1. Enqueue Operation:
	Algorithm
```
	def insert(self, val):
		self.l.append(1)
```


# **Assignment**

Bus Ticket Booking
1. Assume you have a bus with 25 seats
	- Seats 1 - 10 have a price of 1500
	- Seats 11 - 20 have a price of 1000
	- Seats 21 - 25 have a price of 700
2. Show Vacant Seats
3. Seat Booking
4. Confirm Seat (if not confirmed in 5 min time lim -> cancel and become vacant) 
5. Show Ticket
