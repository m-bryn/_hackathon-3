import numpy as np
def matrix_for_simplex(size):
  A = np.zeros(size)
  working_shifts = [4,5,6,7,8]
  count = 0
  for shift in working_shifts:
    k = 0
    for j in range(A.shape[1] - shift + 1):
      for i in range(shift):
        A[j + count][i + k] = 1
      k+=1
    count += j + 1
  return A
#можно кастомить size но тут подстроено под 15 часовой рабочий день, в примере был 11 часовой и матрица 30 x 11, в нашем случае 50 * 15
size = (50, 15)
A = matrix_for_simplex(size)
A
