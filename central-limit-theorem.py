
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


population = pd.DataFrame()
population['numbers'] = np.random.uniform(0,1,size=10000)
population['numbers'].hist(bins=100)

population['numbers'].mean()
# Create a list
sampled_means = []

# For 1000  times,
for i in range(0,1000):
    # Take a random sample of 100 rows from the population, take the mean of those rows, append to sampled_means
    sampled_means.append(population.sample(n=100).mean().values[0])
    #Create a histogram with the samples_means
    pd.Series(sampled_means).hist(bins=100)
pd.Series(sampled_means).mean()