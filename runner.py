from csv import writer
from os import path
from random import uniform

from associativite import main as associativite


def generate_random_series(n: int):
  series = []
  for _ in range(n):
    start = uniform(0.0, 10.0)  # Générer un start aléatoire entre 0.0 et 10.0
    end = uniform(start + 0.1, 15.0)  # Générer un end aléatoire entre start + 0.1 et 15.0
    step = uniform(0.01, 1.0)  # Générer un step raisonnable entre 0.01 et 1.0
    series.append((start, end, step))
  return series


def main():
  n = 5  # Nombre de séries à générer
  random_series = generate_random_series(n)

  # Nom du fichier CSV
  csv_file = 'data.csv'

  # Vérifie si le fichier existe déjà
  file_exists = path.isfile(csv_file)

  # Ouvre le fichier en mode ajout
  with open(csv_file, mode='a', newline='') as file:
    csv = writer(file)

    # Écrit les en-têtes si le fichier n'existe pas
    if not file_exists:
      csv.writerow(['start', 'end', 'step', 'result'])

    # Écrit les données dans le fichier
    for i, (start, end, step) in enumerate(random_series):
      result = associativite(start, end, step)
      print(f"Series {i + 1}: Start = {start:.2f}, End = {end:.2f}, Step = {step:.2f}, Result = {result}")
      csv.writerow([f"{start:.2f}", f"{end:.2f}", f"{step:.2f}", result])


if __name__ == "__main__":
  main()
