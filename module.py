'''1st way import module '''
'''import math
print(dir(math))
print((math.sqrt(25)))'''

''' 2nd way import module as alias name'''

'''import math as m
print(m.pi)'''

'''3rd way from module name import function name'''
'''from math import sqrt
print(sqrt(9))'''

'''4th way from module_name importy function_name as alias_name'''
'''start with _ function will not be imported'''
from math import sqrt as s
print(s(9))


