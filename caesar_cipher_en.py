class CaesarCipher():
	"""Class for doing encryption and decryption using a Caesar cipher."""

	def __init__(self, shift):
		"""Construct Caesar cipher using given integer shift for rotation."""
		
 		self._forward = ' '.join(chr((k + shift) % 26 + ord('A')) for k in range(26))
  		self._backward = ' '.join(chr((k - shift) % 26 + ord('A')) for k in range(26))


	def encrypt(self, message):
		"""Return string representing encripted message."""

		return self._transform(message.upper(), self._forward)


	def decrypt(self, secret):
		"""Return decrypted message given encrypted secret."""

		return self._transform(secret.upper(), self._backward)


	def _transform(self, original, code):
		"""Utility to perform transformation based on given code string"""
		msg = list(original)
		for k in range(len(msg)):
			if msg[k].isupper():
				j = ord(msg[k]) - ord('A')
				msg[k] = code[j]
				result = ''.join(msg)
		return result.lower()



cipher = CaesarCipher(3)
message = "GAEL DONT COME HOME"
codeed = cipher.encrypt(message)
print(f"Secret: {codeed}")
answer = cipher.decrypt(codeed)
print(f"Message: {answer}")
