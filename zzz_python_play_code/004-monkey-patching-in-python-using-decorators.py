# tags: decorators, @, monkey patching, reopen class

# how to monkey patch an existing class,
#   i.e. adding methods to an existing class
#        changing the methods of an existing class
#   without subclassing

# useful link:
# http://stackoverflow.com/questions/352537/extending-builtin-classes-in-python

# The following method does not apply to builtin classes because
#   setattr(class_to_extend = builtin_class, k, v)
# triggers
#   TypeError: can't set attributes of built-in/extension type 'list'.
# This is discussed further down (at the bottom).
# For builtin classes, you can subclass them.

# # "The @ symbol is used for class, function and method decorators."
# # i.e. you must have
# # @decorator
# # <class, function, or method here>

def extend(class_to_extend):
    def decorator(extending_class):
        
        extending_class__dict__ = extending_class.__dict__
        attrs = extending_class__dict__.items()
        
        for k, v in attrs:
            if k != '__dict__':
                setattr(class_to_extend, k, v)
        return class_to_extend
    return decorator

class A(object):
    def hello(self):
        print('Hello!')
    def introduce(self, name):
        print('My name is ' + name + '.')
    
A().hello()           #=> Hello!
A().introduce('Jose') #=> My name is Jose!

# The following three snippets accomplish the same behavior.
# Having all of the together is useful for understanding what each snippet does.

# # reopen class A
# @extend(A)
# class B(object):          # class is in the local scope of the decorator function,
#                           # works when I name the extending class 'A' and also when I name it 'B'
#     def hello(self):      # change method
#         print('Hey')
#     def bye(self):        # add method
#         print('Chao!')

decor = extend(A)
@decor
class B(object):     # the extending_class can have any name since it exists in the scope of decor
    def hello(self):
        print('Hi!')
    def bye(self):
        print('Ciao!')

# decor = extend(A) # returns decorator function with environment context { class_to_extend => A }
# class B(object):          # class now Exists in the global frame
#                           # works only when I name the extending class something not equal to 'A' the name of the class_to_extend
#     def hello(self):      # change method
#         print('Hiya!')
#     def bye(self):        # add method
#         print('Bye bye!')
# decor(B)

# behavior of introduce is not changed
A().introduce('Jose') #=> My name is Jose.

# behavior of hello is changed
A().hello()           #=> Hey!  | Hi!  | Hiya!

# behavior of bye is added
A().bye()             #=> Chao! | Chao | Bye bye!


# # It is not possible to use the extend decorator pattern to extend
# # a builtin class because
# #   setattr(class_to_extend = builtin_class, k, v)
# # triggers
# #   TypeError: can't set attributes of built-in/extension type 'list'
# # 
# # The following is an attempt to do just that,
# # As discussed, this will eventually trigger a TypeError
#
# @extend(list)
# class list(object):
#     def addList(self, other):
        
#         assert isinstance(other, list)
#         assert len(other) == len(self)
        
#         for i in range(len(self)):
#             self[i] += other[i]