##########################################
##  DIFFERENTIAL EQUATIONS USING JULIA
##  PRACTICE EXERCISES: Ex 2: system of equations
##  from the online documentation
##
##  Author: Prithvi Thakur
##  Date Created: 02-21-2019
##########################################

using DifferentialEquations
using Plots

#--------------------------------------------------
# Choice of solvers in differential equation solve:
#--------------------------------------------------
#    AutoTsit5(Rosenbrock23()) handles both stiff and non-stiff equations. This is a good algorithm to use if you know nothing about the equation.

#   BS3() for fast low accuracy non-stiff.

#    Tsit5() for standard non-stiff. This is the first algorithm to try in most cases.

#    Vern7() for high accuracy non-stiff.

#    Rodas4() for stiff equations with Julia-defined types, events, etc.

#    radau() for really high accuracy stiff equations (requires installing ODEInterfaceDiffEq.jl)



# Lorenz equations

# Define the equation function
#   du is the solution which is also an input in the
#   function for better memory management
#   p are the parameters
function lorenz(du, u, p, t)
    du[1] = p[1]*(u[2]-u[1])
    du[2] = u[1]*(p[2]-u[3]) - u[2]
    du[3] = u[1]*u[2] - p[3]*u[3]
end

tspan = (0.0, 100.0)  # time
p = [10.0, 28.0, 8/3]   # parameters
uo = [1.0,0.0,0.0]        # initial conditions

# create the pde
prob = ODEProblem(lorenz, uo, tspan, p)

# solution
sol = solve(prob)

