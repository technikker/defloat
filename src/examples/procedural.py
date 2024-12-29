
if __name__ == '__main__':
	import defloat

	a = 5.32515
	b_z, b_e = defloat.decomp(a)
	c = defloat.recomp(b_z, b_e)

	print(f"decomposition: fraction={b_z}, exponent={b_e}")
	print(f"recomposition: {c}")
	print(f"check:         {a}")

	assert c == a
