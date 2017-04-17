import re

isValidNumber = lambda s,n,c,d: re.sub(n*'-?'+'('+c*'\d{1,3}(,\d{3})+|'+'\d*)'+d*'(\.\d+)?',s,s)==s