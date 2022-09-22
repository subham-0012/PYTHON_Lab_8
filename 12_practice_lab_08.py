x,y = Symbol('x,y')
from sympy import *
integrate(x**2,x)
integrate(sin(x),x)
integrate(sin(x),y)
integrate(cos(x),y)
integrate(x**2,y)
integrate(cos(x),x)

diff(log(x),x)
diff(1/x,x)
diff(sin(x),x)
diff(cos(x),x)
f=Symbol('f',cls=function)
diffeq = Eq(f(x).diff(x, x) +9*f(x), 1)
dsolve(diffeq, f(x))

x = Symbol('x')
limit((sin(x)-x)/(x**3), x, 0)

solve((x+y-2,2*x+y),x,y)

simplify(sin(x)/cos(x))

N(sqrt(2),100)
Rational(1,2)+Rational(1,3)
expand((x+y)**6)

A=Matrix([[3,7],[4,-2]])
B=A.inv()
c=Matrix([12,5])
B*c