from matplotlib import pyplot as plt
from load_csv import load


def aff_life(country_name):
    '''Plot life expectancy over time for a specific country'''
    try:
        data = load("../../../life_expectancy_years.csv")
        country_data = data[data['country'] == country_name]
        years = range(1800, 2101)
        life_expectancy = country_data.iloc[:, 1:].values.flatten()
        plt.plot(years, life_expectancy)
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title(f'Life Expectancy Over Time for {country_name}')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


def main():
    aff_life("Morocco")


if __name__ == "__main__":
    main()
