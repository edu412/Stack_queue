# Implementación de stack personalizada en Python
class Stack:
 
    # Constructor para inicializar la stack
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
 
    # Función para agregar un elemento `val` a la stack
    def push(self, val):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)
 
        print(f'Inserting {val} into the stack…')
        self.top = self.top + 1
        self.arr[self.top] = val
 
    # Función # para sacar un elemento superior de la stack
    def pop(self):
        # comtrie si hay subdesbordamiento de stack
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)
 
        print(f'Removing {self.peek()} from the stack')
 
        # reduce el tamaño de la stack en 1 y (opcionalmente) devuelve el elemento reventado
        top = self.arr[self.top]
        self.top = self.top - 1
        return top
 
    # Función para devolver el elemento superior de la stack
    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]
 
    # Función para devolver el tamaño de la stack
    def size(self):
        return self.top + 1
 
    # Función # para comprobar si la stack está vacía o no
    def isEmpty(self):
        return self.size() == 0
 
    # Función # para comprobar si la stack está llena o no
    def isFull(self):
        return self.size() == self.capacity
 
 
if __name__ == '__main__':
 
    stack = Stack(3)
 
    stack.push(1)       # Insertar 1 en la stack
    stack.push(2)       # Insertar 2 en la stack
 
    stack.pop()         # quitando el elemento superior (2)
    stack.pop()         # quitando el elemento superior (1)
 
    stack.push(3)       # Insertar 3 en la stack
 
    print('Top element is', stack.peek())
    print('The stack size is', stack.size())
 
    stack.pop()         # quitando el elemento superior (3)
 
    # comprobar si la stack está vacía
    if stack.isEmpty():
        print('The stack is empty')
    else:
        print('The stack is not empty')