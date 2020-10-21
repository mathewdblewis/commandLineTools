# stackoverflow.com/questions/10457240

from sympy import *
x,y = symbols('x y')
from sympy import roots, solve_poly_system

ans = solve_poly_system([y**2 - x**3 + 1, y*x], x, y)

print(ans)


