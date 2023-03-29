def sort(arr):
    max_digits = max([len(str(x)) for x in arr])

    base = 10

    bins = [[] for _ in range(base)]

    for i in range(0, max_digits):
        for x in arr:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        bins = [[] for _ in range(base)]

    return arr


if __name__ == '__main__':
  import random

  arr = [random.randrange(1, 1000000) for _ in range(1000000)]
  out = sort(arr)
  print(out)
