import unittest

def checkPrime(n):
		if n>1:
			for i in range(2,n//2+1):
				if(n%i==0):
					return i
			return 1
		else:
			return -1

class PrimeTest(unittest.TestCase):

	def test_prime(self):
		self.assertEqual(checkPrime(2),1)
	def test_notPrime(self):
		self.assertEqual(checkPrime(4),1)


if __name__ == '__main__':
    unittest.main()