# Monte carlo simulation example on multiple processors

@everywhere include("count_heads.jl")

nheads = @parallel (+) for i = 1:20000000
    Int(rand(Bool))
end

# iterations assigned to multiple processes, and then combined with a specific reduction (+).


# pmap processes
M = Matrix{Float64}[rand(1000,1000) for i = 1:10]

@time pmap(svd, M)
