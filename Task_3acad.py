def make_step(k):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
           m[i][j+1] = k + 1

h = int(input('Введите количество строк матрицы: '))
w = int(input('Введите количество столбцов: '))
start_x, start_y = map(int, input('Введите точку старта: ').split())
end_x, end_y = map(int, input('Введите точку финиша: ').split())
a = []
for i in range(h):
    a.append([int(i) for i in input('Введите строку, заполняя числа через пробел: ').split()])

#a = [
#    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
#    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
#    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
#    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
#    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
#    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
#    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
#    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
#    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
#    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
#    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
#    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#]
m = [[0 for i in range(w)] for j in range(h)]
m[start_x][start_y] = 1

k = 0
while m[end_x][end_y] == 0:
    k += 1
    make_step(k)

path = [(end_x, end_y)]
k = m[end_x][end_y]
while k > 1:
  if end_x > 0 and m[end_x - 1][end_y] == k-1:
    end_x, end_y = end_x-1, end_y
    path.append((end_x, end_y))
    k-=1
  elif end_y > 0 and m[end_x][end_y - 1] == k-1:
    end_x, end_y = end_x, end_y-1
    path.append((end_x, end_y))
    k-=1
  elif end_x < len(m) - 1 and m[end_x + 1][end_y] == k-1:
    end_x, end_y = end_x+1, end_y
    path.append((end_x, end_y))
    k-=1
  elif end_y < len(m[end_x]) - 1 and m[end_x][end_y + 1] == k-1:
    end_x, end_y = end_x, end_y+1
    path.append((end_x, end_y))
    k -= 1

print(path)