import matplotlib.pyplot as plt

x = []
y = []

with open('27-10','r') as file:
    for line in file:
        parts = line.replace(',','.').strip().split()
        if len(parts) == 2:
            x.append(float(parts[0]))
            y.append(float(parts[1]))

plt.scatter(x, y, color='green')
plt.title("Точки из TXT-файла")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
