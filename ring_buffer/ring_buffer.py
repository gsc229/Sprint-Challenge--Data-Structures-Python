from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
     # test creates a RingBuffer instance with a capacity of 5

    def append(self, item):
        # append to the tail up to the capacity
        # keep the current as the tail until capacity is reached
        # a app(b) --> a, b etc. current = b
        # a, b, c, d, e at capacity, add 'f'
        # after current travels the length of the list once, that means the head will be the oldest. 'f' needs to replace the oldest, which is the head
        # set current to f
        # f, b, c, d, e --> add 'g'
        # now f is the current, which meas the oldest is to the right of it 'b'
        # replace b with 'g', set 'g' to current
        # f, g, c, d, e --> add 'h', repeat steps until the current reaches the capacity.

        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            print(f"\nitem: {item}, current: {self.current.value}")

        elif self.storage.length == self.capacity:
            print(f"AT CAPACITY...")
            print(f"CURRENT: {self.current.value}")
            if not self.current.next:
                print("**NO CURRENT.NEXT**")

            else:
                print("**THERE'S A CURRENT.NEXT**")

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


buffer = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')

buffer.append('f')
