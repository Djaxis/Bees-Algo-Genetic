import random
import numpy as np


class Bee:
    counter = 0  # Compteur pour attribuer des identifiants uniques aux abeilles 
        

    def __init__(self, generation_id, parent1=None, parent2=None):
        Bee.counter += 1
        self.id = Bee.counter  # Identifiant unique de l'abeille
        self.genes = []  # Liste des gènes de l'abeille
        self.fitness_score = 0  # Score de performance de l'abeille
        self.generation_id = generation_id  # ID de la génération de l'abeille
        self.parent1 = None  # Référence vers le parent 1
        self.parent2 = None  # Référence vers le parent 2
        


        
    def set_genes(self, flowers):# Mélange aléatoirement les fleurs pour créer un chemin unique pour chaque abeille 
        self.genes = flowers[:]  # Copie les fleurs pour ne pas modifier la liste originale
        random.shuffle(self.genes)  # Mélange les fleurs aléatoirement pour chaque abeille


    def calculate_performance(self):
        genes_np = np.array(self.genes)# Convertit les gènes en tableau numpy
        distances = np.sum(np.abs(genes_np[:-1] - genes_np[1:]), axis=1)# Calcule la distance entre chaque paire de fleurs dans les gènes
        self.fitness_score = np.sum(distances) # Somme des distances pour obtenir le score de performance
        
        
    def reproduce(self, parent1, parent2, generation_id):
        child1 = Bee(generation_id)  # Crée un nouvel enfant 1 avec generation_id
        child2 = Bee(generation_id)  # Crée un nouvel enfant 2 avec generation_id
       
        crossover_point = random.randint(1, len(self.genes) - 1)  # Point de croisement pour la reproduction
        
        child1_genes = parent1.genes[:crossover_point] # Gènes de l'enfant 1 provenant du parent 1 jusqu'au point de croisement
        child2_genes = parent2.genes[:crossover_point] # Gènes de l'enfant 2 provenant du parent 2 jusqu'au point de croisement
       
        missing_coords_child1 = [coord for coord in parent2.genes if coord not in child1_genes] # Coordonnées manquantes pour l'enfant 1 à partir du parent 2    
        missing_coords_child2 = [coord for coord in parent1.genes if coord not in child2_genes] # Coordonnées manquantes pour l'enfant 2 à partir du parent 1
       
        child1_genes += missing_coords_child1 # Ajoute les coordonnées manquantes aux gènes des enfants
        child2_genes += missing_coords_child2
        
        child1.genes = child1_genes # Définit les gènes des enfants
        child2.genes = child2_genes
        
        return child1, child2


class Beehive:
    def __init__(self, num_bees, flowers):  # Initialise la ruche avec un nombre donné d'abeilles et une liste de fleurs
        self.bees = [Bee(generation_id=0) for _ in range(num_bees)]  # Assurez-vous de passer l'ID de génération
        self.generation = 0  # Numéro de génération
        self.average_scores = []  # Liste pour stocker les scores moyens
        self.flowers = flowers  # Liste de fleurs disponibles
        self.generation_id = 0  # Attribut pour stocker l'ID de génération actuelle
        self.position = (500, 500)  # Position de la ruche (500, 500)

    def initialize_bees(self):# Initialise les gènes et les scores de performance de toutes les abeilles dans la ruche
        for bee in self.bees:
            bee.set_genes(self.flowers)
            bee.calculate_performance()
            bee.generation_id = self.generation_id  # Assurez-vous d'initialiser generation_id pour chaque abeille
    
    def evolve_generation(self):
        self.bees.sort(key=lambda bee: bee.fitness_score)  # Trie les abeilles en fonction de leur score de performance
        best_bees = self.bees[:50]  # Sélectionne les 50 meilleures abeilles
        
        new_bees = []  # Liste pour stocker les nouvelles abeilles générées

        # Logique de reproduction pour créer de nouvelles abeilles
        while len(new_bees) < len(self.bees):
            parent1, parent2 = random.sample(best_bees, 2)
            child1, child2 = parent1.reproduce(parent1, parent2, self.generation_id)
            
            child1.calculate_performance()  # Calcule les performances des nouveaux enfants
            child2.calculate_performance()
            
            child1.generation_id = self.generation_id  # Met à jour l'ID de génération pour les nouveaux enfants
            child2.generation_id = self.generation_id
           
            new_bees.extend([child1, child2])  # Ajoute les enfants à la liste des nouvelles abeilles
        

        
        self.bees = new_bees  # Remplace les anciennes abeilles par les nouvelles pour la prochaine génération
        self.generation_id += 1  # Mise à jour de l'ID de la génération actuelle
        
        

