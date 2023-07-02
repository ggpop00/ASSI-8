# 1) Create 2 classes for single inheritance named respectively A(base class) and B(derived class)
# class A:
#     def display(self):
#         print("This is class A")
        
# class B(A):
#     def display_1(self):
#         print("This is class B")
        
# b=B()
# b.display()
# b.display_1()

#2) Create 3 data members in class A: a(private), b(protected) and c(public) initialise their values in a parameterized constructor
# class A:
#      def __init__(self,__a,_b,c):
#         self.a=__a
#         self.b=_b
#         self.c=c
#         print(__a,_b,c)
# abc=A(10,20,30)

#3) Create a method known as display in both the classes, to display the values of a,b and c

# class A:
#     a=10
#     b=20
#     c=30
#     def display(self):
#         print("This is class A")
#         print(self.a)
#         print(self.b)
#         print(self.c)
# class B(A):
#     def display_1(self):
#         print("This is class B")
#         print(A.a)
#         print(A.b)
#         print(A.c)
# b=B()
# b.display()
# b.display_1()

#4) While accessing the private member an exception should be raised and a personalized message should be displayed and the exception should be handled properly so that the rest of the code can get executed

# class A:
#     def __init__(self, a, b, c):
#         self._a = a  
#         self.__b = b  
#         self.c = c  

#     def display(self):
#         print("This is Class A:")
#         print("a =", self._a)
#         print("b =", self.__b)
#         print("c =", self.c)


# class B(A):
#     def display(self):
#         try:
#             print("This is Class B:")
#             print("b =", self.__b)  
#         except AttributeError as e:
#             print("Error:", e)
#         super().display()
# b = B(67,34,663)
# b.display()


