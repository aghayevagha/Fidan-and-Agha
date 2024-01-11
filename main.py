import time
import matplotlib.pyplot as plt

def sieve_of_eratosthenes(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    return is_prime

def measure_performance(n):
    performance_times = []

    for _ in range(n):
        start_time = time.time()
        prime = sieve_of_eratosthenes(99999)
        end_time = time.time()
        performance_times.append(end_time - start_time)

    average_performance = sum(performance_times) / len(performance_times)
    print("Average Performance:", average_performance, "seconds")

    # Visualize performance over attempts
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, n + 1), performance_times, marker='*')
    plt.xlabel('Attempt')
    plt.ylabel('Time (seconds)')
    plt.title('Performance over Attempts')
    plt.show()