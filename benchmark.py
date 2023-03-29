from timeit import default_timer as timer

def benchmark(func, args_to_func):
  start = timer()
  func(*args_to_func)
  end = timer()
  return end - start
  

if __name__ == '__main__':
  import matplotlib.pyplot as plt
  import random

  list_lens = [i*1000 for i in range(1, 100)]

  from search import interpolation, jump, ternary
  from sort import bucket, heapify, radix

  times_interpolation = []
  times_jump = []
  times_ternary = []

  times_bucket = []
  times_heapify = []
  times_radix = []

  for list_len in list_lens:
    arr = [i for i in range(1000000)]

    number_to_find = random.randrange(1, 1000000)

    times_interpolation.append(benchmark(interpolation.search, [arr, len(arr)-1, number_to_find]))
    times_jump.append(benchmark(jump.search, [arr, len(arr)-1, number_to_find]))
    times_ternary.append(benchmark(ternary.search, [arr, len(arr)-1, number_to_find]))
  
  for list_len in list_lens:
    arr = [i for i in range(1000000)]
    random.shuffle(arr)

    number_to_find = random.randrange(1, 1000000)

    times_bucket.append(benchmark(bucket.sort, [arr]))
    times_heapify.append(benchmark(heapify.sort, [arr]))
    times_radix.append(benchmark(radix.sort, [arr]))

  plt.plot(list_lens, times_interpolation, label = "interpolation")
  plt.plot(list_lens, times_jump, label = "jump")
  plt.plot(list_lens, times_ternary, label = "ternary")

  plt.plot(list_lens, times_bucket, label = "bucket")
  plt.plot(list_lens, times_heapify, label = "heapify")
  plt.plot(list_lens, times_radix, label = "radix")
    
  plt.ylabel('time')
  plt.xlabel('len of list')
    
  plt.legend()
  plt.show()

    


