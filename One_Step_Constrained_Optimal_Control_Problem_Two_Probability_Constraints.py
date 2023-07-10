import numpy as np
import cvxpy as cp
import scipy.stats as stats

# Ex_1 = cp.Variable((1,1))
u_0 = cp.Variable((1,1))
x_d = 2
Ex_0 = 1
Sigx_0 = 1

Ew_0 = 0
Sigw_0 = 1

delta_1 = 0.5
delta_2 = 0.1

Delta = delta_1 + delta_2 # delta_1 + delta_2 <=  Delta where Delta is the risk of violation 



Sigx_1= (0.8**2*Sigx_0 + Sigw_0)


# cost = 10*(Ex_1-x_d)**2 - 20*Ex_1*x_d + 10*(Sigx_1) + 50*u_0**2
cost = 10*(0.8*Ex_0 + u_0 + Ew_0)**2 -10*x_d**2 - 20*(0.8*Ex_0 + u_0 + Ew_0)*x_d + 10*(Sigx_1) + 50*u_0**2

constr = [0.5*(0.8*Ex_0 + u_0 + Ew_0) - np.sqrt(0.25*Sigx_1)*stats.norm.ppf(1-delta_1, loc=0, scale=1)<=0,0.8*Ex_0 + u_0 + Ew_0 - np.sqrt(Sigx_1)*stats.norm.ppf(1-delta_2, loc=0, scale=1)<=0, cp.abs(u_0)<=1] #g(x) <= 0 -> dual: \lambda*(g(x)-0), therefore abs(u_0) - 1 <= 0 -> \lambda*(abs(u_0)-0)

problem = cp.Problem(cp.Minimize(cost), constr)
problem.solve(verbose=True)


print("Optimal Primal solution:",cost[0].value)
dual = 10*(0.8*Ex_0 + u_0[0].value + Ew_0)**2 - 10*x_d**2 - 20*(0.8*Ex_0 + u_0[0].value + Ew_0)*x_d + 10*(Sigx_1) + 50*u_0[0].value**2 + constr[0].dual_value*(0.5*(0.8*Ex_0 + u_0[0].value + Ew_0) - np.sqrt(0.25*Sigx_1)*stats.norm.ppf(1-delta_1, loc=0, scale=1)) + constr[1].dual_value*(0.8*Ex_0 + u_0[0].value + Ew_0 - np.sqrt(Sigx_1)*stats.norm.ppf(1-delta_2, loc=0, scale=1)) + constr[2].dual_value*(np.abs(u_0[0].value)-1)
print("Optimal dual solution",dual)
print(Delta)