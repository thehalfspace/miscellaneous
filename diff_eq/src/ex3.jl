##########################################
##  DIFFERENTIAL EQUATIONS USING JULIA
##  PRACTICE EXERCISES: Ex 3: boundary value problems
##  from the online documentation
##
##  Author: Prithvi Thakur
##  Date Created: 02-21-2019
##########################################

using DifferentialEquations
using Plots
using BoundaryValueDiffEq

# Define the equation function
function simplependulum!(du, u, p, t)
    θ = u[1]
    dθ = u[2]
    du[1] = dθ
    du[2] = -(p[1]/p[2])*θ
end

tspan = (-2π, 2π)    # time
p = [9.80, 10.0]   # parameters
uo = [1.0,0.0,0.0]      # initial conditions

function bc1!(residual, u, p, t)
    residual[1] = u[end÷2][1] + pi/2 # the solution at the middle of the time span should be -pi/2
    residual[2] = u[end][1] - pi/2 # the solution at the end of the time span should be pi/2
end

bvp1 = BVProblem(simplependulum!, bc1!, [pi/2,pi/2], tspan, p)
sol1 = solve(bvp1, GeneralMIRK4(), dt=0.05)

plot(sol1)

