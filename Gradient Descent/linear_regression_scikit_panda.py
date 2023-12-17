import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

def prepare_country_stats(oecd_bli, gdp_per_capita):
    # This line of code filters the OECD Better Life Index data 
    # by selecting only the rows where the value of the INEQUALITY 
    # column is equal to TOT. The resulting data frame will only 
    # contain the total values for each country.
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    # In this case, the Country column is used as the row labels, 
    # the Indicator column is used as the column labels, and the 
    # Value column is used as the cell values
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    # This line of code uses the .rename() method in Pandas DataFrame to rename 
    # the column named 2015 to GDP per capita 12. The columns argument specifies
    #  a dictionary that maps the old column name to the new column name. 
    # The inplace argument is set to True to modify the DataFrame directly
    # instead of creating a new copy.
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)

    gdp_per_capita.set_index("Country", inplace=True)

    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    
    full_country_stats.sort_values(by="GDP per capita", inplace=True)

    remove_indices = [0, 1, 6, 8, 33, 34, 35]

    keep_indices = list(set(range(36)) - set(remove_indices))
    
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]

# Load the data
oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv",thousands=',',delimiter='\t', encoding='latin1', na_values="n/a")

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)

# X = np.c_[country_stats["GDP per capita"]]
# y = np.c_[country_stats["Life satisfaction"]]
# # Visualize the data
# country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
# plt.show()
# # Select a linear model
# model = sklearn.linear_model.LinearRegression()
# # Train the model
# model.fit(X, y)
# # Make a prediction for Cyprus
# X_new = [[22587]] # Cyprus's GDP per capita
# print(model.predict(X_new)) # outputs [[ 5.96242338]]