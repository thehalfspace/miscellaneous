##########################################
##  DIFFERENTIAL EQUATIONS USING JULIA
##  PRACTICE EXERCISES: Part 1
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


# Toy problem: du/dt = f(u,p,t) = αu

# Define RHS function
f(u,p,t) = 1.01*u

# Define initial condition
uo = 0.5

# Define the time period as a tuple
tspan = (0.0, 1.0)

# Create the PDE problem
prob = ODEProblem(f, uo, tspan)

# Solve using TSit5 algo
sol = solve(prob, Tsit5(), reltol=1e-8, abstol=1e-8, saveat=0.1)




