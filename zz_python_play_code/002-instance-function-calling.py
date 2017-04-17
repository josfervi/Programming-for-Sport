class A(object):
    
    def foo(self):
        print( "yas" )

a = A()

# foo must be called with an instance as self

a.foo()   #=> yas
A.foo(a)  #=> yas
A().foo() #=> yas

# A.foo() # TypeError: foo() missing 1 required positional argument: 'self'
# foo(a) # NameError: name 'foo' is not defined.