def moving_average(data, k=3):
    result = []
    for i in range(len(data) - k + 1):
        window = data[i:i+k]
        avg = sum(window) / k
        result.append(round(avg, 2))
    return result


def median_filter(data, k=3):
    result = []
    for i in range(len(data) - k + 1):
        window = data[i:i+k]
        sorted_window = sorted(window)
        median = sorted_window[k // 2]
        result.append(median)
    return result


# Hybrid filter (BEST)
def hybrid_filter(data, k=3):
    # First remove noise (median)
    step1 = median_filter(data, k)
    
    # Then smooth it (average)
    step2 = moving_average(step1, k)
    
    return step2


# Example input
data = list(map(int, input("Input: ").strip().split()))

print("Original:", data)
print("Muchiko (Average):", moving_average(data))
print("Sanchiko (Median):", median_filter(data))
print("Hybrid (Best):", hybrid_filter(data))
