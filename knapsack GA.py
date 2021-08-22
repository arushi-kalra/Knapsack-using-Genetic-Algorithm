import random
import numpy as np
individuals=10
chromosome_length=6
W=14
profit=[10,3,7,4,2,9]
w=[2,5,4,4,1,6]
expected_count=[]
def constraint(population):
    for i in range(len(population)):
        s=0
        for j in range(chromosome_length):
            if(population[i][j]==1):
                s=s+w[j]
        if(s>W):
            return False
    return True

def create_starting_population(individuals, chromosome_length):
    # Set up an initial array of all zeros
    population = np.zeros((individuals, chromosome_length))
    # Loop through each row (individual)
    c=0
    while(c<individuals):
        # Choose a random number of ones to create
        index = random.randint(1, chromosome_length)
        # Change the required number of zeros to ones
        population[c, 0:index] = 1
        # Sfuffle row
        np.random.shuffle(population[c])
        sum=0
        for i in range(chromosome_length):
            if(population[c][i]==1):
                sum=sum+w[i]
        if(sum<=W):
            c=c+1
            continue
        else:   
            population[c][0:]=0
            
    
    return population

def calculate_fitness(population,profit):
    fitness_scores=[]
    for i in range(len(population)):
        s=0
        for j in range(chromosome_length):
            if(population[i][j]==1):
                s=s+profit[j]
        fitness_scores.append(s)
    
    return fitness_scores

def Roulette_Wheel_Selection(population,fitness):
    #F=np.sum(fitness,axis=1)
    #for i in range(individuals):
     #   expected_count[i]=int(fitness[i]/F)
    #x=int(input("Enter the crossover probability"))
    #mating_pool_size=individuals*c"""
    no_of_parents=int(input("Enter the no. of parents"))
    parents=[]
    for i in range(no_of_parents):
        index=np.argmax(fitness)
        fitness[index]=-99999
        parents.append(population[index])
        
    return parents

def crossover(parents):
    offspring=np.zeros((len(parents),chromosome_length))
    c=0
    for i in range(0,len(parents),2):
        crossover_point=random.randint(1,chromosome_length-1)
        print("crossover point:",crossover_point)
        offspring[c][0:crossover_point]=parents[i][0:crossover_point]
        offspring[c][crossover_point:]=parents[i+1][crossover_point:]
        c=c+1
        offspring[c][0:crossover_point]=parents[i+1][0:crossover_point]
        offspring[c][crossover_point:]=parents[i][crossover_point:]
        
        c=c+1
        
    return offspring

def mutation(offspring):
    m=input("Enter mutation rate")
    genes_to_be_mutated=int(float(m)*individuals*chromosome_length)
    print("Genes to be mutated :")
    print(genes_to_be_mutated)
    flag=0
    #for i in range(0,individuals*chromosome_length,int((individuals*chromosome_length)/genes_to_be_mutated)):
    while(flag==0):
        random_number=[]
        ct=1
        #for i in range(genes_to_be_mutated):  
        while(ct<=genes_to_be_mutated):
            index=random.randint(0,len(offspring)*chromosome_length)
            if(index not in random_number):
                random_number.append(index)
                a=int(index/chromosome_length)
                b=index-chromosome_length*a
                if(b==0):
                    a=a-1
                    b=chromosome_length-1
                else:
                    b=b-1
                if(offspring[a][b]==0):
                    offspring[a][b]=1
                else:
                    offspring[a][b]=0
                ct=ct+1
        if(constraint(offspring)):
                flag=1
    return offspring

def next_generation(population,offspring,fitness):
    new_population=[]
    fit=calculate_fitness(offspring,profit)
    for i in range(individuals):
        index1=np.max(fitness)
        index2=np.max(fit)
        if(index1>index2):
            j=np.argmax(fitness)
            new_population.append(population[j])
            fitness[j]=-99999
        else:
            j=np.argmax(fit)
            new_population.append(offspring[j])
            fit[j]=-99999
        
    return new_population


gen=int(input("Enter the no. of generations : "))
for i in range(gen):
    print("GENERATION : ",i+1)
    if(i==0):
        population=create_starting_population(individuals, chromosome_length)
    else:
        population=new_population
    print("Population : ")
    print(population)
    fitness= calculate_fitness(population,profit)
    print("Fitness Values : ")
    print(fitness)
    parents=Roulette_Wheel_Selection(population,fitness)
    print("Chromosomes chosen as parents : ")
    print(parents)
    offspring=crossover(parents)
    print("Offspring produced : ")
    print(offspring)
    child=mutation(offspring)
    print("Mutated Offspring : ")
    print(child)
    new_population=next_generation(population,child,fitness)
    print("Next generaton : ")
    print(new_population)