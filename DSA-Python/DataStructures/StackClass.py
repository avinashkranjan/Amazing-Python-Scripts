class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)


# class Stack():
#     def __init__(self):
#         self.stack = list()

#     def push(self, item):
#          self.items.append(item)

#      def pop(self):
#          return self.items.pop()


#      def peek(self):
#          return self.items[len(self.items)-1]

#      def size(self):
#          return len(self.items)

# def is_empty(self):
#          return self.items == []
