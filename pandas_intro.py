import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/IMDb_Data_final.csv')


# Data Extraction: loc

# data_extracted = data.loc[15:85, ['Title','Stars','Category']]
# print(data_extracted)


# Extract data with even and odd indices
# even = data.iloc[lambda x: x.index % 2 == 0 ]
# odd = data.iloc[lambda x: x.index % 2 != 0 ]

# print(even.head(5), odd.tail(5))

# Extract data from the first 50 rows and columns 1 and 4
# data_extracted = data.iloc[:50, [1,4]]