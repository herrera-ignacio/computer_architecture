def get_unsigned_binary(n: int):
	if n > 0:
		return bin(n)[2:]
	return bin(n)[3:]

def invert_bits(b: str):
	inverted_binary = ""
	for char in b:
		if char == "0":
			inverted_binary += "1"
		elif char == "1":
			inverted_binary += "0"
	return inverted_binary

def to_fixed_digits(b: str, d: int):
	return b.zfill(d)

def handle_overflow(b: str, d: int):
	if len(b) > d - 1:
		raise 'overflow'

def get_signed_binary(n: int, d: int):
	try:
		binary = to_fixed_digits(get_unsigned_binary(n), d - 1)
		handle_overflow(binary, d)
		if(n > 0):
			return '0' + binary
		else:
			return '1' + binary
	except Exception as e:
		return 'overflow'

def get_one_complement(n: int, d: int):
	binary = to_fixed_digits(get_unsigned_binary(n), d)
	if n > 0:
		return binary
	return invert_bits(binary)

if __name__ == "__main__":
	print(get_one_complement(10, 5))
	print(get_one_complement(-15, 5))
