def is_prime(number):
	if ((number/number) == 1) | ((number/1) == number):
		return True
	if ((number/number) != 1) | ((number/1) != number):
		return False