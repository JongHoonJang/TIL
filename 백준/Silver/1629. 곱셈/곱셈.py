a,b,c = map(int, input().split())

def res(a, n):
  if n == 1:
      return a % c 
  else:
      tmp = res(a, n // 2)
      if n % 2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp * a) % c
          
print(res(a, b))