class Stack:
    """
    : LIFO DS
    """
    def __init__(self):
        """
        : Constructor init both stack
        """
        self.min_stack = []
        self.max_stack = []

    def push(self, ele):
        """
        :param ele: num
        :return: None
        """
        min_ele = ele
        max_ele = ele
        if self.min_stack:
            min_ele = min(min_ele, self.min_stack[-1])

        if self.max_stack:
            max_ele = max(max_ele, self.max_stack[-1])

        self.max_stack.append(max_ele)
        self.min_stack.append(min_ele)

    def display(self):
        """
        : Display both the stacks
        """
        print('min_stack : {}'.format(self.min_stack))
        print('max_stack : {}'.format(self.max_stack))


if __name__ == "__main__":
    st = Stack()
    st.push(3)
    st.push(6)
    st.push(2)
    st.push(7)
    st.push(1)
    st.push(9)
    st.push(0)
    st.display()