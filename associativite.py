from argparse import ArgumentParser

from numpy import arange


def main(start=0.0, end=5.0, step=0.1):
  bad_result = 0
  cpt = 0

  for i in arange(start, end, step):
    for j in arange(start, end, step):
      for k in arange(start, end, step):
        cpt += 1
        if (i + j) + k != i + (j + k):
          bad_result += 1

  return f"{(cpt - bad_result) * 100 / cpt:.2f}"


if __name__ == "__main__":
  # Parse arguments at runtime
  parser = ArgumentParser(description="Check associativity of specified range.")
  parser.add_argument('--start', type=float, default=0.0, help="Start of the range (e.g., '0.0').")
  parser.add_argument('--end', type=float, default=5.0, help="End of the range (e.g., '5.0').")
  parser.add_argument('--step', type=float, default=0.1, help="Step size (e.g., '0.1').")

  args = parser.parse_args()

  result = main(**vars(args))
  print(result)
