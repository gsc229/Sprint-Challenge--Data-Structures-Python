class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node):
        # TO BE COMPLETED
        prev = None
        current = self.head
        next_item = current.get_next()
        new_list = []

        if node.get_next() == None:
            self.head = node
            print(node.value)
            return

        self.reverse_list(node.get_next())
        current = node.get_next()
        print(f"{node.value}")
        current.set_next(node)

        node.set_next(None)

        # while current is not None:

        #     new_list.append(current.value)
        #     current = next_item
        #     if next_item is not None:
        #         next_item = next_item.get_next()

        # print(new_list)
        # while :
        #     if current:
        #         new_list.append(current)
        #     current = next_item
        #     next_item = current.get_next

        # for item in new_list:
        #     print(item)


list = LinkedList()

list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)
list.add_to_head(4)
list.add_to_head(5)


current = list.head
while current:
    print(current.value)
    current = current.get_next()
print(f"=====REVERSE IT:===========")
print(list.reverse_list(list.head))
