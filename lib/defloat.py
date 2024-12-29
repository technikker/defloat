"""
a small implementation of a portable float format
	with no loss of precision
"""
import typing as _tp
from math import frexp, ldexp


class DeFloat(_tp.NamedTuple):
	""" De[composed]Float[ing] Point Object """

	z: int  # numerator
	# ^^ denominator can be obtained via 1 << z.bit_length(),
	#  and will be the next power of 2 greater than z
	e: int  # exponent

	@classmethod
	def decomp(cls, r: float):
		""" de-compose into portable integer repr, (fraction, exponent) """
		return decomp(r)

	def recomp(self) -> float:
		""" re-compose into native floating point object """
		return recomp(*self)

	__float__ = recomp


def decomp(r: float) -> DeFloat:
	""" de-compose into portable integer repr, (fraction, exponent) """
	fr, ex = frexp(r)  # normalize fraction to 0 <= 'fr' < 1
	#  and return the old exponent
	num, div = fr.as_integer_ratio()
	if "test block":  # you can remove this via compile and introspection
		try:
			assert div.bit_length() == num.bit_length() + 1
			assert div == 1 << num.bit_length()
			# assert div + 1 == 1 << num.bit_length()
			# ^^ used for testing the assertion printout
		except AssertionError as err:
			# this *should* never occur
			# by default there's no description attached to the
			#  assertion error, so we add one
			kwargs = tuple(f"{k}={repr(v)}" for k, v in vars().items())
			kwargs = kwargs[:-1]  # don't print out the err object
			err.args = (f"local vars | dict({', '.join(kwargs)})", )
			raise
	return DeFloat(num, ex)


def recomp(z: int, e: int) -> float:
	""" re-compose into native floating point object """
	divisor = 1 << z.bit_length()
	# ^^ equivalent to:
	#   divisor = 2 ** z.bit_length()
	#  (using exponent operator) but *should* be faster
	fraction = z / divisor
	return ldexp(fraction, e)
