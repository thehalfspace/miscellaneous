# Iterative solvers example in julia

using IterativeSolvers
using Preconditioners
using LinearAlgebra
using LOBPCG

A = rand(5,5)
b= rand(5)

x = cg(A,b)
