# Parallel computing exercises in julia

#=
# Serial version
function f(N::Int)
    iter = Int(1e4*2)

    p = 5000

    vec_mean = zeros(iter)

    for i=1:iter
        vec_mean[i] = mean(rand(p))
    end

    return mean(vec_mean)

end

println("The mean estimate: ", @time f(0))
=#

# Parallel version
#addprocs(nprocs() - 1)

@everywhere function f_parallel(N::Int)

    iter = Int(1e4*2)
    p = 5000
    vec_mean = zeros(iter)

    for i=1:iter
        vec_mean[i] = mean(rand(p))
    end

    return mean(vec_mean)
end

println("The mean estimate: ", @time f_parallel(0))
