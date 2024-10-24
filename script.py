import requests

# Liste des dépôts GitHub à vérifier
repos = [
  "https://github.com/Matys53/REP_TP",
  "https://github.com/PaulineRoches/REP_popo_sos",
  # "https://github.com/l55I1/REP",
  "https://github.com/matth1446/rep_mh_vvk",
  "https://github.com/AntoineMarchalDombrat/REP_Antoine_Jean",
  "https://github.com/alpjakop/REP",
  "https://github.com/Humilokaki/TP2-REP-INSA-202425",
  "https://github.com/Repro-Arno-Jeremy/REP-TP2",
  "https://github.com/Kaeios/assoc-REP",
  "https://github.com/Dyskal/repro",
]

# Chemin vers le fichier de référence
reference_file_path = "./answer_associativity.txt"

# Lire le contenu du fichier de référence
reference_value = open(reference_file_path, 'r').read().strip()

# URL de base pour accéder aux fichiers bruts sur GitHub
base_url = "https://raw.githubusercontent.com"

# Comparer les fichiers dans les dépôts
for repo in repos:
  repo_name = repo.split('https://github.com/')[1]
  default_branch = 'master' if repo_name in ['Matys53/REP_TP', 'Kaeios/assoc-REP'] else 'main'

  # Construire l'URL du fichier answer_associativity.txt
  file_url = f"{base_url}/{repo_name}/{default_branch}/answer_associativity.txt"
  try:
    # Faire une requête GET pour récupérer le contenu du fichier
    response = requests.get(file_url)
    response.raise_for_status()  # Vérifier si la requête a réussi

    # Lire le contenu du fichier récupéré
    answer_value = response.text.strip()

    # Comparer les valeurs
    if answer_value == reference_value:
      print(f"{repo}: Les valeurs sont identiques ({answer_value}).")
    else:
      print(f"{repo}: Les valeurs sont différentes. Référence: {reference_value}, Trouvé: {answer_value}.")

  except requests.exceptions.HTTPError as err:
    print(f"Erreur lors de la récupération de {file_url}: {err}")
  except Exception as e:
    print(f"Une erreur est survenue pour {repo_name}: {e}")
