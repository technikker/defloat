
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
