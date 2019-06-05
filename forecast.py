import random as rn
import numpy as np

story_points = 50
sample_size = 6
num_simulations = 10000

# Takts is made up of the last 10 sprints - Sprint Length and Stories completed - Change as required
takts = [
    [10, 6],
    [8, 6],
    [10, 3],
    [10, 10],
    [10, 2],
    [10, 8],
    [10, 15],
    [9, 6],
    [10, 8],
    [10, 10]
]

results = []
for i in range(num_simulations):
    # Get reduced number of sample data randomly
    random_takts = rn.sample(takts, sample_size)

    takt = []
    sprint_length = 0
    for n in range(sample_size):
        sprint_length = sprint_length + random_takts[n][0]
        takt.append(random_takts[n][0] / random_takts[n][1])

    avg_sprint_length = sprint_length / sample_size
    project_duration = round(story_points * np.mean(takt) / avg_sprint_length, 2)
    results.append(project_duration)

projected_sprints = np.mean(results).round(2)
print(projected_sprints)
