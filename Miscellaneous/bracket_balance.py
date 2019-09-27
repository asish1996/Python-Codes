# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:09:10 2019

@author: Asish Yadav
"""
#
#array1 = ['(','{','[']
#array2 = [')','}',']']
#string = '([])[]({})'
#word1 = 'true'
#word2 = 'false'
#
#if len(string)%2 != 0:
#    print (word2)
def areParanthesisBalanced(expr) :  
  
    s = [];  
  
    # Traversing the Expression  
    for i in range(len(expr)) : 
  
        if (expr[i] == '(' or 
            expr[i] == '[' or expr[i] == '{') : 
  
            # Push the element in the stack  
            s.append(expr[i]);  
            continue;  
  
        # IF current character is not opening  
        # bracket, then it must be closing.   
        # So stack cannot be empty at this point.  
        if (len(s) == 0) : 
            return False;  
  
        if expr[i] == ')' : 
  
            # Store the top element in a  
            x = s.pop(); 
              
            if (x == '{' or x == '[') : 
                return False;  
  
        elif expr[i] == '}':  
  
            # Store the top element in b  
            x = s.pop(); 
              
            if (x == '(' or x == '[') : 
                return False;  
          
        elif x == ']':  
  
            # Store the top element in c  
            x = s.pop(); 
              
            if (x =='(' or x == '{') : 
                return False;  
  
    # Check Empty Stack  
    if len(s) : 
        return True
    else : 
        return False
  
# Driver Code 
if __name__ == "__main__" :  
  
    #expr = "{()}[]";
    expr = '([)]'
  
    if (areParanthesisBalanced(expr)) : 
        print("True");  
    else : 
        print("False"); 