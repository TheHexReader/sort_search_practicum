def search(ar, r, key, l = 0):
	while r >= l:
		
		mid1 = l + (r-l) // 3
		mid2 = r - (r-l) // 3

		if key == ar[mid1]:
			return mid1
		if key == ar[mid2]:
			return mid2

		if key < ar[mid1]:
			r = mid1 - 1
		elif key > ar[mid2]:
			l = mid2 + 1
		else:
			l = mid1 + 1
			r = mid2 - 1

	return -1

if __name__ == '__main__':
	ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	r = 9
	key = 5
	p = search(r, key, ar)
	print("Index of", key, "is", p)

	key = -123
	p = search(r, key, ar)
	print("Index of", key, "is", p)
