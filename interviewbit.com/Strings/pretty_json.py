# https://www.interviewbit.com/problems/pretty-json/

# when you encounter an opening brace
#  first     print the brace
#  and then  inc indentation_level
#  and then  start a new line
 
# when you encounter a closing brace
#  first     dec indentation_level
#  and then  print the brace
#  and then  start a new line



class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        
        tabs= ""
        indentation_level= 0
        
        lines= []
        current_line= ""
        for char in A:
            if char == '{' or char == '[':
                
                if not current_line == "":
                    lines.append( tabs + current_line )
                
                lines.append( tabs + char )
                
                indentation_level+= 1
                tabs= '\t' * indentation_level
                current_line= ""
            
            elif char == '}' or char == ']':
                
                if not current_line == "":
                    lines.append( tabs + current_line)
                
                indentation_level-= 1
                tabs= '\t' * indentation_level
                lines.append( tabs + char )
                
                current_line= ""
            
            elif char == ',':
                
                if current_line == "": # to handle a closing brace followed by a ','
                    lines[-1]+= ','
                else:
                    lines.append( tabs + current_line + ',')
                
                current_line= ""
            
            else:
                current_line+= char
        
        return lines
