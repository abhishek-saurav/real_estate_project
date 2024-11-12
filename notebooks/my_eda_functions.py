# importing libraries 

import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns, os

def cat_col_summary(df, var):
    import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
    print("="*50)
    # quick glance 
    print(f"Quick glance of {var}")
    print("="*15)

    print(df[var].sample(10))
    print("="*50)



    # cardinality check 
    print(f"Cardinality in the {var} column: ")
    print(df[var].nunique())
    print("="*50)

    # value coutnts
    print(df[var].value_counts())

    # missing values 
    print(f"Number of missing values in the {var} column: ")
    null_values = df[var].isnull()
    print(null_values.sum())
    print("="*50)

    # print("Frequency bins")
    # counts = (
    # df[var] 
    # .value_counts()
    # )

    # frequency_bins = {
    #     "Very High > 100": (counts > 100).sum(), 
    #     "High (50-100)": ((counts > 50) & (counts < 100)).sum(), 
    #     "Average (10-49)": ((counts > 10) & (counts < 50)).sum(), 
    #     "Low (2-9)": ((counts > 1) & (counts < 10)).sum(), 
    #     "Very Low (1)": (counts ==1).sum()
    # }

    # for key, value in frequency_bins.items():
    #     print("{}\t:\t{}".format(key, value))

        # bar chart 
    plt.figure(figsize=(10, 3))
    # plt.subplot(1, 2 , 1)
    df[var].value_counts().head(10).plot(kind = 'bar', title = f"Top categories in {var}")

    # # pie chart
    # plt.subplot(1, 2, 2)
    # plt.pie(data['bedRoom'].value_counts(normalize= True).head(), autopct= "%0.2f%%")
    # plt.show()
    print("="*100)


def cat_num_bivar(data, var1, var2):

    # print(f"{var1} vs {var2}")
    print(data.groupby(data[var1])[var2].median())
    print("="*50)

    print(f"Summary of {var1} vs {var2}")
    print(data.groupby(data[var1])[var2].describe())
    print("="*50)


    plt.figure(figsize=(15, 8))
    plt.subplot(2,2, 1)
    sns.barplot(x = data[var1], y = data[var2], estimator= np.median)
    plt.title(f"Bar Chart between {var1} and {var2}")
    plt.xticks(rotation = 45)

    # boxplot 
    plt.subplot(2, 2, 2)
    sns.boxplot(x = data[var1], y = data[var2])
    plt.title(f"Box plot for {var1} vs {var2}")
    plt.xticks(rotation = 45)
    plt.show()


def cat_cat_bivar(data, var1, var2):


    plt.figure(figsize= (10, 8))
    plt.subplot(2, 2, 1)
    sns.barplot(data = data, x = var1, y = var2)
    plt.title(f"{var1} vs {var2} Bar Plot")

    # boxplot 
    plt.subplot(2, 2, 2)
    sns.boxplot(data= data, x = var1, y = var2)
    plt.title(f"Box plot {var1} vs {var2}")
    plt.show()