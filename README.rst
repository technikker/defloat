
.. image:: https://img.shields.io/pypi/v/defloat.svg
	:target: https://pypi.python.org/pypi/defloat

.. image:: https://img.shields.io/pypi/l/defloat
	:target: https://spdx.org/licenses/MPL-2.0.html

.. image:: https://img.shields.io/pypi/pyversions/defloat.svg
	:target: https://pypi.python.org/pypi/defloat


DeFloat
=======

Floating Point Decomposition

A small implementation of a portable floating point format
(i.e. with no loss of precision across floating point
implementations).


Examples
----------

..
	Because GitHub doesn't support the include directive
	we just copy/paste these from examples


Object-Oriented style:

.. code:: python

	if __name__ == '__main__':
		from defloat import DeFloat

		a = 5.32515
		b = b_z, b_e = DeFloat.decomp(a)
		c = float(b)  # 1 way to do it
		d = b.recomp()  # the other way to do it

		print(f"decomposition:   fraction={b_z}, exponent={b_e}")
		print(f"recomposition 1: {c}")
		print(f"recomposition 2: {d}")
		print(f"check:           {a}")

		assert c == d == a

		"""
		expected output:
			decomposition:   fraction=5995585888922999, exponent=3
			recomposition 1: 5.32515
			recomposition 2: 5.32515
			check:           5.32515
		"""


Procedural style:

.. code:: python

	if __name__ == '__main__':
		import defloat

		a = 5.32515
		b_z, b_e = defloat.decomp(a)
		c = defloat.recomp(b_z, b_e)

		print(f"decomposition: fraction={b_z}, exponent={b_e}")
		print(f"recomposition: {c}")
		print(f"check:         {a}")

		assert c == a

		"""
		expected output:
			decomposition: fraction=5995585888922999, exponent=3
			recomposition: 5.32515
			check:         5.32515
		"""


Notes
-------

Recomposition on hardware with lower precision may/will result
in data/precision loss.  Precision is only guaranteed within
the decomposed format, and recomposition to the same implementation
as decomposed from.


License
-------

`DeFloat`_ is licensed under `Mozilla Public License`_.

.. External References:
.. _DeFloat: https://github.com/technikian/defloat
.. _Mozilla Public License:
	https://github.com/technikian/defloat/blob/master/LICENCE
