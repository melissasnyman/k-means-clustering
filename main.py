import pandas as pd
import matplotlib.pyplot as plt
import random


def main():
    airbnb = pd.read_csv('airbnb.csv')
    latitude = airbnb['latitude']
    longitude = airbnb['longitude']
    latitude = latitude.to_numpy()
    longitude = longitude.to_numpy()
    plt.scatter(x=longitude, y=latitude)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()

    k = int(input('How many clusters? '))
    print(k)

    sample_count = len(latitude)
    points = []  # k unique points selected randomly.
    indices = []  # Sample indices of points already selected.

    # Loop while the number of selected points is less than the number of clusters.
    while len(points) < k:
        # Randomly select a sample index.
        sample_index = random.randint(0, sample_count - 1)

        # If the point has not already been chosen, then choose the point.
        if sample_index not in indices:
            point = {'sample_index': sample_index,
                     'coordinates': [longitude[sample_index], latitude[sample_index]]}
            points.append(point)
            indices.append(sample_index)

    print(points)


if __name__ == '__main__':
    main()


