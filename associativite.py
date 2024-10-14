import numpy as np

badResult = 0

for i in range(0, 50):
    for j in range(0, 50):
        for k in range(0, 50):
            if (i * 0.1 + j * 0.1) + k * 0.1 != i * 0.1 + (j * 0.1 + k * 0.1):
                badResult += 1

print("Manual range: Expected 26898; Current", badResult)

badResult = 0

for i in np.arange(0.0, 5.0, 0.1):
    for j in np.arange(0.0, 5.0, 0.1):
        for k in np.arange(0.0, 5.0, 0.1):
            if (i + j) + k != i + (j + k):
                badResult += 1

print("Manual numpy arange: Expected 26898; Current", badResult)
