def get_valid_configs(T, L1, L2, L3, D):
    configs = []
    
    for i in range(min(L1, T) + 1):
        for j in range(min(L2, T - i) + 1):
            k = T - i - j
            
            if 0 <= k <= L3 and abs(i - k) <= D:
                configs.append((i, j, k))
    
    return configs


def cost(c1, c2, W):
    return (
        abs(c1[0] - c2[0]) * W[0] +
        abs(c1[1] - c2[1]) * W[1] +
        abs(c1[2] - c2[2]) * W[2]
    )


def min_wear_cost(Limits, Wear, Targets, D):
    L1, L2, L3 = Limits
    
    # Initial state
    prev_configs = [(0, 0, 0)]
    prev_costs = { (0,0,0): 0 }

    for T in Targets:
        curr_configs = get_valid_configs(T, L1, L2, L3, D)
        curr_costs = {}

        for curr in curr_configs:
            min_cost = float('inf')

            for prev in prev_configs:
                c = prev_costs[prev] + cost(prev, curr, Wear)
                min_cost = min(min_cost, c)

            curr_costs[curr] = min_cost

        prev_configs = curr_configs
        prev_costs = curr_costs

    return min(prev_costs.values())


# Sample Input
Limits = [10, 10, 10]
Wear = [1, 3, 5]
Targets = [15, 8]
D = 4

print("Minimum Cost:", min_wear_cost(Limits, Wear, Targets, D))
