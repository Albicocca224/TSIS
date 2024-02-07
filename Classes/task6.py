class PrimeFilter:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    def filter_primes(self, numbers):
        return list(filter(self.is_prime, numbers))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_filter = PrimeFilter()
prime_numbers = prime_filter.filter_primes(numbers)
print("Original list:", numbers)
print("Prime numbers:", prime_numbers)
