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
        print(f'элемент {element} добавлен в стэк')
        stack_copy.push_stack(element)
    for element in stack_copy.isEmpty():
        value_pop = stack.pop_stack()
        value_peek = stack.peek_stack()
        if value_pop == aclose:
            count_aclose += 1
        elif value_pop == bclose:
            count_bclose += 1
        elif value_pop == cclose:
            count_cclose += 1
        elif value_pop == aopen:
            count_aopen += 1
            # if count_aclose == 0:
            #     print("Несбалансированно")
            #     return False
        elif value_pop == bopen:
            count_bopen += 1
            # if count_bclose == 0:
            #     print("Несбалансированно")
            #     return False
        elif value_pop == copen:
            count_copen += 1
            # if count_cclose == 0:
            #     print("Несбалансированно")
            #     return False

        if value_pop == aclose and value_peek == bopen or value_pop == aclose and value_peek == copen:
            print("Несбалансированно")
            return False
        elif value_pop == bclose and value_peek == aopen or value_pop == bclose and value_peek == copen:
            print("Несбалансированно")
            return False
        elif value_pop == cclose and value_peek == aopen or value_pop == cclose and value_peek == bopen:
            print("Несбалансированно")
            return False

    if count_aopen == count_aclose and count_bopen == count_bclose and count_copen == count_cclose:
        print("Сбалансированно")
        return True
    else:
        print("Несбалансированно")
        return False


if __name__ == '__main__':
    balance(input("Введите строку со скобками: "))


