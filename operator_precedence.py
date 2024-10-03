# Operator precedence.
# Operator precedence describes the order in which operations are performed in an arithmetic expression
 #operators of higher precedence are evaluated first(come first) 
#Examples:
result = 3 * 4 + 5
print(result)

result_two = 3 * (4+5)
print(result_two) 

result_three = 3*4+5-1
print(result_three)

result_four = 3*(4+5)-1
print(result_four)

 #practice question.
#What would be the output of the following expressions.
result_five = 5*3**2#solves 3**2 first
print(result_five)

result_six = (5+3)*2**2-10/2 
print(result_six)# output is a float type because of the division operator

result_seven = 25/5 + 2*1
print(result_seven)