import math

def search( arr , n , x ):
	step = math.sqrt(n)
	
	prev = 0
	while arr[int(min(step, n)-1)] < x:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return -1

	while arr[int(prev)] < x:
		prev += 1
		
		if prev == min(step, n):
			return -1
	
	if arr[int(prev)] == x:
		return prev
	
	return -1

if __name__ == '__main__':
  arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
  x = 55
  n = len(arr)

  index = search(arr, x, n)

  print("Number" , x, "is at index" ,"%.0f"%index)
