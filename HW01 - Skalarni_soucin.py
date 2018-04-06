class MyVector:
 
    def __init__(self, the_first):
        self.fi = the_first
 
    def get_vector(self):
        return self.fi
 
    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.get_vector(), other.get_vector()))
 
if __name__ == "__main__":
 
    a = MyVector([1, 2, 4])
    b = MyVector([4, 5, 6])
    print(a.get_vector())
    dot_product = a*b
    print (dot_product)