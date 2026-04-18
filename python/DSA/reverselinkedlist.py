class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Linkedlist:
	def __init__(self):
		self.head = None
	def append(self,data):
		new_node = Node(data)
		
		if not self.head:
			self.head = new_node;
			return
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = new_node
	def display(self):
		temp = self.head
		while temp:
			print(temp.data, end=" -> ")
			temp = temp.next
	def reverse(self):
		prev = None
		current = self.head
		while current:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node
			self.head = prev
if __name__ == "__main__":
	ll = Linkedlist()
	ll.append(1)
	ll.append(2)
	ll.append(3)

	ll.reverse()
	ll.display()	