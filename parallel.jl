# Parallel computing exercises in julia

# Everywhere, @spawn, and remotecall()
#addprocs(4)

@everywhere function f_parallel(N::Int)

    iter = Int(1e5*2)
    p = 5000
    vec_mean = zeros(iter)

    for i=1:iter
        vec_mean[i] = mean(rand(p))
    end

    return mean(vec_mean)
end

#@time @spawn f_parallel(0)

#@time remotecall(f_parallel, 2, 0)


# Parallel for loop
a = SharedArray{Float64}(10)

@parallel for i = 1:10
    a[i] = i
end

# Using external variables in parallel for loops is reasonable if the
# variables are read-only

println(a)
