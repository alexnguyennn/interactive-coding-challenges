# implement with internal list (array?)

# class Node(object):
#     def __init__(self, data):
#         self.data = data

# class Stack(object):
#     def __init__(self, top=None):
#         self.nodes = []
#         if top is not None:
#             self.nodes.append(top)

#     def push(self, data: Node):
#         self.nodes.append(Node(data))

#     def pop(self):
#         return self.nodes.pop().data if not self.is_empty() else None

#     def peek(self):
#         print(f"{self.nodes}; {self.is_empty()}")
#         return self.nodes[-1].data if not self.is_empty() else None

#     def is_empty(self):
#         return len(self.nodes) == 0


# implement with linked list
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data)
        if self is not None:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top
        self.top = self.top.next
        return popped.data

    def peek(self):
        return self.top.data if not self.is_empty() else None

    def is_empty(self):
        return self.top is None