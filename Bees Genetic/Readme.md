

La reproduction se fait en combinant les gènes de deux parents jusqu'à un point de croisement, puis en ajoutant les gènes manquants de chaque parent pour former deux nouveaux ensembles de gènes, qui sont attribués à deux nouveaux individus représentant les enfants.

La reproduction des abeilles implique une certaine forme de sélection aléatoire des gènes des parents pour créer de nouveaux individus (les enfants).


Création des gènes des enfants:
Les gènes de chaque enfant sont formés en combinant les gènes des deux parents jusqu'au point de croisement.
Pour child1, les gènes proviennent de parent1 jusqu'au point de croisement, tandis que pour child2, les gènes proviennent de parent2 jusqu'au même point.
Ensuite, les coordonnées manquantes dans chaque enfant (qui ne sont pas déjà présentes avant le point de croisement) sont ajoutées à partir de l'autre parent. Cela garantit que chaque enfant possède tous les gènes uniques des deux parents.
Ces coordonnées manquantes sont identifiées en vérifiant les gènes des parents qui ne sont pas déjà présents dans les gènes partiels des enfants.


Le choix du point de croisement pour la reproduction est effectué de manière aléatoire parmi les gènes des parents, ce qui détermine comment les gènes seront échangés entre les deux parents pour former les enfants. Cela introduit une forme d'aléatoire dans le processus de reproduction.

Ensuite, les gènes des enfants sont partiellement hérités de chaque parent jusqu'au point de croisement, et les gènes manquants (qui ne sont pas déjà présents avant le point de croisement) sont ajoutés en fonction de l'autre parent. Cette méthode crée une diversité génétique parmi la progéniture, ce qui est l'un des aspects importants dans les algorithmes évolutifs pour explorer et trouver de bonnes solutions dans l'espace des solutions possibles.


Concretement en Exemple :
choisissons un point de croisement aléatoire entre 1 et la longueur de la liste - 1.
Considérons les listes de coordonnées suivantes pour les parents :
Parent 1: [10, 20, 30, 40, 50, 60, 70]
Parent 2: [15, 25, 35, 45, 55, 65, 75]
Si le point de croisement est choisi comme 3 (par exemple, via random.randint(1, len(self.genes) - 1)), cela signifie que les trois premières coordonnées de chaque parent resteront intactes pour les enfants, et les coordonnées après le point de croisement seront échangées entre les parents pour former les gènes des enfants.
Parent 1: [10, 20, 30 | 40, 50, 60, 70]
Parent 2: [15, 25, 35 | 45, 55, 65, 75]
Les barres verticales (|) représentent le point de croisement. Dans cet exemple, les trois premières coordonnées restent inchangées pour chaque parent. Maintenant, pour créer les gènes des enfants :
Enfant 1:
Il commence par les trois premières coordonnées de Parent 1 : [10, 20, 30]
Ensuite, il complète les coordonnées manquantes à partir de Parent 2, sans répéter les coordonnées déjà présentes : [10, 20, 30, 40, 50, 60, 70] - [15, 25, 35] = [10, 20, 30, 40, 50, 60, 70, 15, 25, 35]
Enfant 2:
Il commence par les trois premières coordonnées de Parent 2 : [15, 25, 35]
Ensuite, il complète les coordonnées manquantes à partir de Parent 1, sans répéter les coordonnées déjà présentes : [15, 25, 35, 45, 55, 65, 75] - [10, 20, 30] = [15, 25, 35, 45, 55, 65, 75, 10, 20, 30]
C'est ainsi que la reproduction à ce point de croisement spécifique combine les gènes des deux parents pour créer les gènes des deux enfants.