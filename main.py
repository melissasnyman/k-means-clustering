import pandas as pd
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    main()


