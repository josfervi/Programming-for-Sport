# https://codefights.com/challenge/9kmuSXmkpwEpNLkYj/solutions

S = re.sub

def codeGolfReducedScore(c):
    return len(
               S('[\s]', '',
                 S('[a-zA-Z]\w*', '_',
                   S('["\'][^"\']*.', lambda m : ':'*len(m.group()),
                     c
                     )
                   )
                 )
               )




# c = S('(".*?")|(\'.*?\')', lambda m : ':'*len(m.group()), c) # don't be greedy with text bt. quotes