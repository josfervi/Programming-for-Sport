class StackMachine(object):
    
    def __init__(self):
        self.stk = []
    
    def empty_stk_check(self, func):
        if not self.stk:
            raise ValueError('Cannot call {} with an empty stack.'.format(func.__name__))
        func()
    
    def bin_opcode_stk_check(self, func):
        if len(self.stk) < 2:
            raise ValueError('Cannot call {} with a stack with less than two items.'.format(func.__name__))
        func()
    
    def execute(self, instruction):
        opcode, operand = instruction, ''
        if isinstance(instruction, tuple):
            opcode, operand = instruction
        executable_str = 'self.' + opcode + '(' + operand + ')'
        exec(executable_str)
    
    def push(self, operand):
        self.stk.append(operand)
    
    @self.empty_stk_check
    def pop(self):
        self.stk.pop()
    
    @self.empty_stk_check
    def print_and_pop(self):
        print self.stk.pop()
    
    @self.bin_opcode_stk_check
    def add(self):
        op1 = self.stk.pop()
        self.stk[-1] = op1 + self.stk[-1]
    
    def execute_all(self, instructions):
        
        OPCODE = 0
        NEW_IC = 1
        
        ic = 0
        while ic < len(instructions):
            instruction = instructions[ic]
            
            if isinstance(instruction, tuple) and instruction[OPCODE] is 'jump':
                new_ic = instruction[NEW_IC]
                ic = new_ic
            else:
                self.execute(instruction)
                ic += 1


def debug_jumps(instructions):
    
    OPCODE = 0
    NEW_IC = 1
    
    debugged_instructions = []
    
    ic_wrt_is = 0
    while ic_wrt_is < len(instructions):
        
        instruction = instructions[ic_wrt_is]
        
        if isinstance(instruction, tuple) and instruction[OPCODE] is 'jump':
            
            new_ic_wrt_is = instruction[NEW_IC]
            # convert new_ic from index into instructions to index into debugged_instructions
            new_ic_wrt_dis = new_ic_wrt_is + 2 * num_jumps_in_instructions_before(new_ic_wrt_is, jump_ics_wrt_is)
            
            debug_str = 'Jumping form line {} to line {}.'.format(ic_wrt_is, new_ic_wrt_is)
            debugged_instructions.append( ('push', debug_str) )
            debugged_instructions.append(  'print_and_pop' )
            
            debugged_instructions( ('jump', new_ic_wrt_dis) )
        else:
            debugged_instructions.append(instruction)
        
        ic_wrt_is += 1
    
    return debugged_instructions


instructions = [
    ('push', 5),
    ('push', 'I am '),
    'add',
    'print_and_pop',
    ('jump', 0)]

sm = StackMachine()
sm.execute_all(instructions)