# regular expressions and grammars resources:

# http://web.mit.edu/6.005/www/fa15/classes/17-regex-grammars/
# https://regexone.com/lesson/capturing_groups
# https://regex101.com/#python

import re

class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        #                      -----------number-----------   --exponent--
        pattern= r"^\s*([+-]?(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))(e[+-]?[0-9]+)?)\s*$"
        #                             -decimal     -decimal
        if re.search(pattern, A):
            return 1
        return 0