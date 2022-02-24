# 1,2,3
import matplotlib.pyplot as plt


x = (0, 3, 6, 9, 14)
y = (0, 5, 2, 8, 10)

fig, plots = plt.subplots(nrows=1, ncols=3)

plots[0].scatter(x, y)  # 1
plots[1].plot(x, y)  # 2
plots[2].plot(x, y, 'o-')  # 3

plt.show()
