def harmonic_number(n):

	if n == 1:
		return 1
	else:
		return harmonic_number(n-1) + 1/n

print(round(harmonic_number(8),5))
