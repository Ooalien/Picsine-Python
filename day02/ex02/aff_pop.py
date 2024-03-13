from load_csv import load
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker


def plot_population_comparison(data, country1, country2):
    """Plot population comparison between two countries."""

    campus_data = data[data['country'] == country1]
    other_country_data = data[data['country'] == country2]

    # Extracting the years range
    years = campus_data.columns[1:-50].astype(int)


    # Extracting the population data for the selected countries
    campus_population = campus_data.iloc[:, 1:-50].replace({'M': '*1e6', 'k': '*1e3'}, regex=True).apply(pd.eval).values.flatten()
    other_country_population = other_country_data.iloc[:, 1:-50].replace({'M': '*1e6', 'k': '*1e3'}, regex=True).apply(pd.eval).values.flatten()

    plt.plot(years, campus_population, label=f'{country1}')
    plt.plot(years, other_country_population, label=f'{country2}')

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.legend()
    plt.grid(True)
    plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x * 1e-6:.0f}M'))

    plt.show()



def main():
    data = load("../../../population_total.csv")
    print(data.head())
    print(data.info())
    plot_population_comparison(data, "France", "Belgium")


if __name__ == "__main__":
    main()
