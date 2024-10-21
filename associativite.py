import numpy as np

def main():
  #badResult = 0
  #cpt = 0

  #for i in range(10, 60):
  #    for j in range(10, 60):
  #        for k in range(10, 60):
  #            cpt += 1
  #            if (i * 0.1 + j * 0.1) + k * 0.1 != i * 0.1 + (j * 0.1 + k * 0.1):
  #                badResult += 1

  #print(f"Manual range: {(cpt-badResult)*100/cpt}%; Operations {cpt}")

  badResult = 0
  cpt = 0

  for i in np.arange(1.0, 6.0, 0.1):
      for j in np.arange(1.0, 6.0, 0.1):
          for k in np.arange(1.0, 6.0, 0.1):
              cpt += 1
              if (i + j) + k != i + (j + k):
                  badResult += 1

  print(f"Manual numpy arange: {(cpt-badResult)*100/cpt:.2f}")

if __name__ == "__main__":
  main()
