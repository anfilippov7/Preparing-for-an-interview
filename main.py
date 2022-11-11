class Stack:

    def __init__(self):
        self.stack = []

    '''добавляет новый элемент на вершину стека'''

    def push_stack(self, item):
        self.stack.append(item)

    '''проверка стека на пустоту'''

    def is_empty(self):
        empty = self.stack
        isEmpty = (empty is None) or (len(empty) == 0)
        return isEmpty

    '''возвращает стек'''

    def isEmpty(self):
        return self.stack

    '''удаляет верхний элемент стека'''

    def pop_stack(self):
        if len(self.stack) == 0:
            return None
        pop = self.stack.pop()
        return pop

    '''возвращает верхний элемент стека'''

    def peek_stack(self):
        if len(self.stack) == 0:
            return None
        peek = self.stack[-1]
        return peek

    '''возвращает количество элементов в стеке'''

    def size_stack(self):
        size = len(self.stack)
        return size


def balance(staples):
    stack = Stack()
    stack_copy = Stack()
    aopen, aclose = '(', ')'
    bopen, bclose = '[', ']'
    copen, cclose = '{', '}'
    count_aopen, count_aclose = 0, 0
    count_bopen, count_bclose = 0, 0
    count_copen, count_cclose = 0, 0
    for element in staples:
        stack.push_stack(element)
        stack_copy.push_stack(element)
    for element in stack_copy.isEmpty():
        bracket = stack.pop_stack()
        if bracket == aopen:
            count_aopen += 1
        elif bracket == aclose:
            count_aclose += 1
        elif bracket == bopen:
            count_bopen += 1
        elif bracket == bclose:
            count_bclose += 1
        elif bracket == copen:
            count_copen += 1
        elif bracket == cclose:
            count_cclose += 1
        print(count_aopen, count_aclose, count_bopen, count_bclose, count_copen, count_cclose)
    if count_aopen == count_aclose and count_bopen == count_bclose and count_copen == count_cclose:

        print("Сбалансированно")
    else:
        print("Несбалансированно")




if __name__ == '__main__':
    balance(input())

    # a = Stack()
    # # a.push_stack()
    # print(a.is_empty())
    # a.push_stack(1)
    # a.push_stack('fsfgsgs')
    # a.push_stack('3')
    # print(a.is_empty())
    # print(a.pop_stack())
    # print(a.pop_stack())
    # print(a.pop_stack())
    # print(a.pop_stack())
    # print(a.peek_stack())
    # print(a.size_stack())
    # print(a.__dict__)
    # a.push_stack(['afdfd', 'dfdfsd'], 12)
