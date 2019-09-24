def deleteDigit(n):
   ns = str(n)
   max_num = -1
   for i in range(len(ns)):
      n_num = ns[0:i] + ns[i+1:]
      n_num = int(n_num)
      if n_num > max_num:
         max_num = n_num
   return max_num