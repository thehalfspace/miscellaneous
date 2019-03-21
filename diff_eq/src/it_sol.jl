# Iterative solvers example in julia

using IterativeSolvers
using Preconditioners
using LinearAlgebra

N = Int(1e4)
A = rand(N,N)
b= rand(N)

x = cg(A,b)
