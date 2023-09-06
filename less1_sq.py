# Ex. procedural programming - roots of sguare equations

def calculate_x(a, b):
  return-b/(2*a)

def calculate_x1x2(a,b,D):
  x1 = (-b + D**0.5) / (2*a)
  x2 = (-b - D**0.5) / (2*a)
  return x1, x2

def calculate_D(a,b,c):
  return b**2 - 4*a*c

def solve_for_x(a,b,c):
  D = calculate_D(a,b,c)             # расчет дискриминанта
  if D > 0:                          # проверка знака дискриминанта
    return calculate_x1x2(a,b,D)     # вычисление корней
  elif D ==0:                        # проверка знака дискриминанта 
    return calculate_x(a,b)          # вычисление корня
  else:                              # проверка знака дискриминанта
    return "No real solutions"       # возвращаем "нет решения"

if __name__ == "__main__":
  a,b,c = 6, -17, 12                 # 6^2 - 17x +12
  solution = solve_for_x(a,b,c)
  
  print(solution)