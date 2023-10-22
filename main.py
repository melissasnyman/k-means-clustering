import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


COLOURS = ['red', 'green', 'blue', 'yellow', 'purple']


def main():
    airbnb = pd.read_csv('airbnb.csv')
    latitudes = airbnb['latitude']
    longitudes = airbnb['longitude']
    latitudes = latitudes.to_numpy()
    longitudes = longitudes.to_numpy()
    plt.scatter(x=longitudes, y=latitudes)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()

    k = int(input('How many clusters? '))
    print(k)

    sample_count = len(latitudes)
    points = []  # k unique points selected randomly.
    indices = []  # Sample indices of points already selected.

    # Loop while the number of selected points is less than the number of clusters.
    while len(points) < k:
        # Randomly select a sample index.
        sample_index = random.randint(0, sample_count - 1)

        # If the point has not already been chosen, then choose the point.
        if sample_index not in indices:
            point = [longitudes[sample_index], latitudes[sample_index]]
            points.append(point)
            indices.append(sample_index)

    print(points)

    clusters = []

    # Add the index of each selected point to the list of clusters.
    for i in range(k):
        clusters.append([indices[i]])

    # Assign cluster to each non-selected point.
    for sample_index in range(sample_count):
        # If the sample index is not a previously selected point, then assign it to a cluster.
        if sample_index not in indices:
            distances = []

            # Calculate the distance from the current point to each selected cluster point.
            for k_index in range(k):
                distance = np.sqrt(np.square(points[k_index][0] - longitudes[sample_index]) +
                                   np.square(points[k_index][1] - latitudes[sample_index]))
                distances.append(distance)

            # Find the closest cluster point.
            min_distance = min(distances)
            min_index = distances.index(min_distance)

            # Add point to the closest cluster.
            clusters[min_index].append(sample_index)

    for i in range(k):
        plt.scatter(x=longitudes[clusters[i]], y=latitudes[clusters[i]], c=COLOURS[i])

    plt.show()


if __name__ == '__main__':
    main()
