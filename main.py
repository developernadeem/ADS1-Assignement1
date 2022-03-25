"""
main.py, ADS1 assignment
created: 24 Mar, 2022
main.py is mainly intended for interactive plots and and analysis of data set available at
(https://www.kaggle.com/code/aniruddhasshirahatti/us-unemployment-rate-analysis-updated/data?select=unemployment_data_us.csv)
"""
import matplotlib.pyplot as plt
import pandas as pd


def plot_multiline(df, columns, title):
    """
    Plots trend in un-employment base on the education
    :param df: DataFrame
        Sorted dataframe which need to be plotted
    :param columns: list

    :param title: str
        Title of the plot, name of image
    """
    plt.figure()
    for column in columns:
        # format the axes as date
        plt.plot('Date', column, data=df)
    plt.legend()
    plt.title(title)
    plt.savefig(title + ".png")
    plt.show()


def plot_bar(df, title):
    """
    Plots the bar graph of mean unemployment of men and women with comparison to each other .
    :param df: DataFrame
        dataframe that contains data that need to be compared
    :param title: str
        Title of the plot, name of image
    """
    # Set year as an index, it will be used by pandas to plot it x-axis
    df = df[["Year", "Men", "Women"]].set_index("Year")
    # Calculate the mean of each year
    df = df.groupby("Year").mean()
    # Prepare dataset for appropriate plotting
    dft = df.T
    plt.figure()
    dft.plot(kind='bar', rot=0)
    plt.title(title)
    plt.savefig(title + "")
    plt.show()


def read_data(name):
    """
    Reads a cvs file and prepare data set for basic analysis with matplotlib
    :param name: str
        is name of cvs file to be read for analysis
    """

    df = pd.read_csv(name)
    # drop all the rows with nan values as it may effect plotting at this stage
    df = df.dropna()
    # convert date to date time format
    df['Date'] = pd.to_datetime(df.Date)
    df = df.sort_values(by='Date', ascending=True)
    # plot a multiline graph of un-employment on the bases of education
    plot_multiline(df, ["Primary_School", "High_School", "Associates_Degree", "Professional_Degree"],
                   "Education base unemployment")
    # plot a multiline graph of un-employment on the bases of ethnicity
    plot_multiline(df, ["White", "Black", "Asian", "Hispanic"],
                   "Ethnicity base unemployment")
    plot_bar(df, "Men vs Women")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(read_data.__doc__)
    read_data('unemployment_data_us.csv')
