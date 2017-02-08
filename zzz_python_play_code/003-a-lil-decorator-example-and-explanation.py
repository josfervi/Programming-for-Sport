# What does the at (@) symbol do in Python
# http://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python

# the following snippend kind of elucidates what a decorator can do

def single_param_fcn(param):
    param.__call__()
@single_param_fcn
def call_me():
    print('You called!')
#=> You Called!

# # The following doesn't work though
# # The reason:
# # "The @ symbol is used for class, function and method decorators."
# # i.e. you must have
# # @decorator
# # <class, function, or method here>
#
# def single_param_fcn(param):
#     print(param)
#
# @single_param_fcn
# "Jose"