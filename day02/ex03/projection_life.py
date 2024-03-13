from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker


def extract_data_for_year(data, year):
    """Extract data for a specific year."""
    return data[['country', str(year)]]


def merge_data(life_expectancy_data, gdp_per_capita_data, year):
    """Merge life expectancy and GDP per capita data for a specific year."""
    life_expectancy_year = extract_data_for_year(life_expectancy_data, year)
    gdp_per_capita_year = extract_data_for_year(gdp_per_capita_data, year)
    merged_data = pd.merge(life_expectancy_year, gdp_per_capita_year, on='country', suffixes=('_life_expectancy', '_gdp_per_capita'))
    return merged_data.dropna()


def plot_relationship(data, year):
    """Plot relationship between life expectancy and GDP per capita."""
    plt.scatter(data[str(year) + '_gdp_per_capita'], data[str(year) + '_life_expectancy'], label=f'Year {year}')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title(year)
    plt.legend()
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x * 1e-3:.0f}K'))

    plt.show()


def main():
    data = load("../../../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data1 = load("../../../life_expectancy_years.csv")
    year = 1900
    merged_data = merge_data(data1, data, year)
    plot_relationship(merged_data, year)


if __name__ == "__main__":
    main()
