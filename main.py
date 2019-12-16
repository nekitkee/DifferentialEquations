import math
import matplotlib.pyplot as plt

#grid step
h1 = 0.05
h2=0.01


y0 = 1
t = [0,1]


a =0.9
b=0.2
funtask= lambda x: a * x - b * x ** 2

#alalytic form
funtask_an = lambda x : 4.5*math.exp(0.9*x)/(3.5+math.exp(0.9*x))

####test function from workbook
c=-3
d=2
funtest = lambda x, t : -3* t + 2 * x ** 2


def euler(func,y0,t,h):
    lenght =int((t[1]-t[0])/h)
    x = []
    y=[]

    y.append(y0)
    x.append(t[0])

    for i in range(lenght):
        x.append(h*(i+1))
        y.append(y[i]+h*func(y[i]))

    return (x,y)


def adamsBashforth(func,y0,t,h):
    lenght = int((t[1] - t[0]) / h)
    x = []
    y = []

    y.append(y0)
    x.append(t[0])

    #we have to calculate first 3 point for extapolation
    for i in range(3):
        x.append(h*(i+1))
        # Euler
        y.append(y[i]+h*func(y[i]))


    for i in range(3,lenght):
        x.append(h*(i+1))
        #Adams (newton cotes quadrature formula)
        yk1 = y[i]+h/24*(55*func(y[i])-59*func(y[i-1]) + 37*func(y[i-1])-9*func(y[i-2]))
        #Bashforth
        y.append(y[i]+h/24*(9*func(yk1)+19*func(y[i])-5*func(y[i-1])+func(y[i-2])))

    return x , y

xab, yab = adamsBashforth(funtask, y0, t, h1)

xe, ye = euler(funtask, y0, t, h1)

# print(x)
# print(y)

#array of reall y (analytic form)
yreall = []
for x in xab :
    yreall.append(funtask_an(x))

plt.plot(xab, yab)
plt.plot(xab,yreall)
plt.xlabel("Adams-Bashforth and analytic")
plt.show()

plt.plot(xe, ye)
plt.plot(xab,yreall)
plt.xlabel("Euler and analytic")
plt.show()





