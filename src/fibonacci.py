def fibonacci(max_number):
    results = []
    accumulator = 0

    while True:
        next_number = 1 if accumulator < 2 else results[-1] + results[-2]
        if (next_number > max_number):
            break

        results.append(next_number)
        accumulator += 1

    return results

print(fibonacci(89900000))
