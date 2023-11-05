import os

# Chemin du dossier contenant les images
image_folder = "C:/Users/alexo/Documents/DATALAKE/Pictures/Pokemon/GEN xxx"

# Parcourir les fichiers d'images dans le dossier
for filename in os.listdir(image_folder):
    # Vérifier si le fichier est une image PNG
    if filename.endswith(".png"):
        # Obtenir le chemin complet du fichier
        file_path = os.path.join(image_folder, filename)
        
        # Obtenir le nouveau nom de fichier en ajoutant des zéros à gauche
        file_name, file_ext = os.path.splitext(filename)
        new_file_name = file_name.zfill(3) + file_ext
        
        # Construire le nouveau chemin complet du fichier
        new_file_path = os.path.join(image_folder, new_file_name)
        
        # Renommer le fichier
        os.rename(file_path, new_file_path)
        print(f"Renamed {filename} to {new_file_name}")