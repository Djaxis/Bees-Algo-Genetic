import csv
import matplotlib.pyplot as plt
import numpy as np
from beehive import Beehive  # Assuming Beehive is a class defined in 'beehive' module



def load_flowers(file_path):
    flowers = []
    with open(file_path, newline='') as file:
        content = csv.reader(file, delimiter=",")
        next(content)
        for line in content:
            try:
                line = tuple(map(int, line))  # Convert all elements to integers
                flower_tuple = tuple(line)
                flowers.append(flower_tuple)
            except ValueError:
                print("Non-numeric value found. Skipping this line:", line)
    return flowers
flowers = load_flowers('C:\\Users\\change\\Desktop\\BUREAU\\LA PLATE FORME\\COURS\\Les abeilles b3\\flowers.csv')



def main():
    nombre_de_geneartion = 50  # Nombre de générations pour l'algorithme génétique
    num_bees = 100  # Nombre d'abeilles dans la ruche
    generation_ids = []  # Crée une liste pour stocker les identifiants de génération

    
    beehive = Beehive(num_bees, flowers)  # Crée une ruche d'abeilles avec les fleurs chargées
    beehive.initialize_bees()  # Initialise les gènes et les performances des abeilles
    
    
    best_bee = None  # Variable pour stocker la meilleure abeille trouvée
    best_score = float('inf')  # Score initial de la meilleure abeille
    generation_scores = []  # Liste scores meilleure abeille à chaque génération
    all_bees_scores = []  # Liste scores de toutes les abeilles à chaque génération

    
    
    for i in range(nombre_de_geneartion):
        current_best_bee = min(beehive.bees, key=lambda bee: bee.fitness_score)

        if current_best_bee.fitness_score < best_score:
            best_bee = current_best_bee
            best_score = current_best_bee.fitness_score

        generation_scores.append(best_score)
        all_scores = [bee.fitness_score for bee in beehive.bees]
        all_bees_scores.append(all_scores)

        beehive.evolve_generation()  # Évolue la génération des abeilles
        beehive.generation_id += 1  # Mise à jour de l'ID de la génération


    average_scores = [np.mean(scores) for scores in all_bees_scores]  # Calcul de la moyenne des scores pour chaque génération

# collecter les ID de génération et les sauvegarder dans un fichier CSV après chaque itération 
    with open('generation_ids.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Generation', 'Generation ID'])  # Écriture de l'en-tête dans le fichier CSV

        for i in range(nombre_de_geneartion):
            beehive.evolve_generation()

            generation_ids.append(beehive.generation_id)  # Ajoute les IDs de génération à la liste

            # Ajoute les IDs de génération dans le fichier CSV
            writer.writerow([i, beehive.generation_id])

        # Récupération de la bee avec le score le plus bas (meilleur score) de la première génération
        worst_bee_first_gen = min(beehive.bees, key=lambda bee: bee.fitness_score)

        # Récupération de la bee avec le score le plus élevé (pire score) de la première génération
        best_bee_first_gen = max(beehive.bees, key=lambda bee: bee.fitness_score)
        
        
        
    # Affichage des détails des 100 premières abeilles de la première génération
    print("Détails des 100 premières abeilles de la première génération :")
    for bee in beehive.bees[:100]:
        print(f"ID : {bee.id}, Fitness : {bee.fitness_score}, ID Génération : {bee.generation_id}")

    # Évolue une nouvelle génération des abeilles
    beehive.evolve_generation()
    beehive.generation_id += 1  # Mise à jour de l'ID de la génération

    # Affichage des détails des 100 premières abeilles de la deuxième génération
    print("\nDétails des 100 premières abeilles de la deuxième génération :")
    for bee in beehive.bees[:100]:
        print(f"ID : {bee.id}, Fitness : {bee.fitness_score}, ID Génération : {bee.generation_id}") 
        
        
        
        for i in range(nombre_de_geneartion):
            current_best_bee = min(beehive.bees, key=lambda bee: bee.fitness_score)
        # le reste de votre boucle for
        print(f"Nombre de générations créées : {beehive.generation_id}")               

        print("\n")

        # Affichage des détails des bees avec les scores les plus bas et les plus élevés
        print("Détails de la bee avec le score le plus bas (meilleur score) dans la première génération :")
        print("ID :", worst_bee_first_gen.id)
        #print("Gènes :", worst_bee_first_gen.genes)
        print("Fitness :", worst_bee_first_gen.fitness_score)
        print("ID de la génération :", worst_bee_first_gen.generation_id)
        
        print("\n")
        
        print("Détails de la bee avec le score le plus élevé (pire score) dans la première génération :")
        print("ID :", best_bee_first_gen.id)
        #print("Gènes :", best_bee_first_gen.genes)
        print("Fitness :", best_bee_first_gen.fitness_score)
        print("ID de la génération :", best_bee_first_gen.generation_id)
        
        print("\n")
        
    # Accéder aux détails de la meilleure abeille dans la dernière génération après la boucle for
        last_gen_best_bee = min(beehive.bees, key=lambda bee: bee.fitness_score)
        print("Détails de la bee avec le score le plus bas dans la dernière génération :")
        print("ID :", last_gen_best_bee.id)
        print("Fitness :", last_gen_best_bee.fitness_score)
        print("ID de la génération :", last_gen_best_bee.generation_id)

        print(f"Nombre de générations créées : {beehive.generation_id}")
        
        

 
















    
    
    plt.figure(figsize=(18, 4)) # Crée un graphique pour visualiser les résultats
  
    plt.subplot(131)
    best_path = best_bee.genes
    x, y = zip(*best_path)
    plt.plot(x, y, marker='o', markerfacecolor='red', linestyle='-', label='Chemin')
    plt.scatter(x[0], y[0], color='green', marker='s', s=100,label='Départ')  
    plt.scatter(x[-1], y[-1], color='darkblue', marker='s', s=100, label='fin')  
    plt.xlabel('X Coordinate', color= 'blue')
    plt.ylabel('Y Coordinate', color = 'blue')
    plt.title("Best Bee Fitness score", color = 'blue')

    
    plt.subplot(132)
    plt.plot(range(nombre_de_geneartion), generation_scores, color='blue', label='Best Bee')
    plt.xlabel('Number Of Generation', color = 'blue')
    plt.ylabel("Best Bee's Fitness Score", color = 'blue')
    plt.title(" Fitness Score Evolution of Best Bee's", color = 'blue')

    
    plt.subplot(133)
    plt.plot(range(nombre_de_geneartion), average_scores, color='green', label='Average Score')
    plt.xlabel('Number Of Generation', color = 'blue')
    plt.ylabel('Average Fitness Score', color = 'blue')
    plt.title('Average > Fitness Score of All Bees', color = 'blue')
    plt.legend()

    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(8, 6))  # Crée un nouveau graphique




if __name__ == '__main__':
    main()  # Appelle la fonction principale si le script est exécuté directement

