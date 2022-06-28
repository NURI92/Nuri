

# Customer Yield Calculation with Rule-Based-Classification


# Installation of necessary libraries

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/nuri/PycharmProjects/pythonProject_n/dsmlbc_9_simge_ilgim/Homeworks/nuri_iyibaslar/modul1_part2_homeworks/persona.csv")

def check_df(dataframe, head=5):
    print("########### Shape ###############")
    print(dataframe.shape)
    print("########### Types ###############")
    print(dataframe.dtypes)
    print("########### Head ###############")
    print(df.head(head))
    print("########### Tail ###############")
    print(df.tail(head))
    print("########### NA ###############")
    print(dataframe.isnull().sum())
    print("############ Information ############")
    print(dataframe.info())
    print("############# Descritive Stats #########")
    print(dataframe.describe().T)


def unique(dataframe):
    print("################### UNIQUE VALUES #################")
    for col in dataframe:
        if dataframe[col].dtypes in ["int"]:
            continue
        print(f"Unique Names:{dataframe[col].unique()} ")
        print("-----------------------------------------------")
        print(f"Unique Counts:{dataframe[col].nunique()} ")
        print("-----------------------------------------------")


unique(df)
check_df(df)


# Question 2: How many unique SOURCE are there? What are their frequencies?

df["SOURCE"].nunique()

# Question 3: How many unique PRICEs are there?

df["PRICE"].nunique()

# Question 4: How many sales were made from which PRICE?

df["PRICE"].value_counts()

# Question 5: How many sales were made from which country?

df["COUNTRY"].value_counts()

# Question 6: How much was earned in total from sales by country?

df.groupby("COUNTRY").agg({"PRICE": "sum"})

# Question 7: What are the sales numbers by SOURCE types?

df.groupby("SOURCE").agg({"PRICE": "count"})

# Question 8: What are the PRICE averages by country?

df.groupby("COUNTRY")["PRICE"].mean()

# Question 9: What are the PRICE averages by SOURCE?

df.pivot_table("PRICE","SOURCE")

# Question 10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?

df.pivot_table("PRICE","COUNTRY","SOURCE")


# Task 2: What are the average earnings in breakdown of COUNTRY, SOURCE, SEX, AGE?


df.pivot_table("PRICE", ["COUNTRY","AGE"],["SEX","SOURCE"])
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})


# Task 3: Sort the output by PRICE

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE" : "mean"})
agg_df = df.groupby([col for col in df.columns[df.columns != "PRICE"]]).mean()
agg_df.sort_values(by="PRICE", ascending=False,inplace=True)


# Task 4: Convert the names in the index to variable names

agg_df.reset_index(inplace=True)

# Task 5: Convert age variable to categorical variable and add it to agg_df

agg_df["AGE_CAT"] = pd.cut(x=agg_df["AGE"],
                           bins=[0, 18, 24, 30, 40, 70],
                           labels=['0_18', '19_23', '24_30', '31_40', '41_70'])



# Task 6: Identify new level-based customers (personas)




agg_df["customers_level_based"] = ["_".join(i).upper() for i in agg_df.drop(["AGE","PRICE"],axis=1).values]

# Task 7: Segment new customers (personas)

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])

agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

# Task 8: Categorize the new customers and estimate how much income they can bring.

new_user = "ANDROID_FEMALE_TUR_31_40"

agg_df[agg_df["customers_level_based"] == new_user]

agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

agg_df[agg_df["customers_level_based"] ==" TUR_ANDROID_FEMALE_31_40"]




