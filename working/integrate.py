import numpy as np
import matplotlib.pyplot as plt

def rect_left (a, b, N, f):
    
    h = (b-a)/N
    xi=np.linspace(a, b, N+1)
    
    return np.sum(f(xi[:-1])*h)

def rect_right (a, b, N, f):
    
    h = (b-a)/N
    xi=np.linspace(a, b, N+1)
    
    return np.sum(f(xi[1:])*h)

def rect_mdp (a, b, N, f):

    h = (b-a)/N
    xi=np.linspace(a, b, N+1)

    return np.sum(f((xi[:-1]+xi[1:])/2)*h)

def trapz(a, b, N, f):

    h = (b-a)/N
    xi = np.linspace(a,b,N+1)

    return 0.5*h*(f(a)+f(b)) + h*np.sum(f(xi[1:-1]))

def simpson (a, b, N, f):
    
    h = (b-a)/N
    xi = np.linspace(a, b, N+1)

    return h/3 * ( (f(a)+f(b)) + 4*np.sum(f(xi[1:-1:2])) + 2*np.sum(f(xi[2:-2:2])) )