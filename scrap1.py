from bs4 import BeautifulSoup as bs
import requests
import csv
import pandas as pd
url="https://www.scrapethissite.com/pages/simple/"
response=requests.get(url)
# print(response)
soup=bs(response.text)
# type(soup)
# print(soup.find('title').text)
data=soup.find_all('div',class_="col-md-4 country")
# print(data[:2])
country_1=data[0]
country_list=[]
for country_1 in data:
    country_name=country_1.find('h3',class_="country-name").text.strip()
    # print(country_name)
    country_capital=country_1.find('span',class_="country-capital").text.strip()
    # print(country_capital)
    country_population=country_1.find('span',class_="country-population").text
    # print(country_population)
    country_area=country_1.find('span',class_="country-area").text
    # print(country_area)
    country_list.append((country_name,country_capital,country_population,country_area))
    print(country_list)
with open("countries.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Country", "Capital", "Population", "Area"])  # header
    writer.writerows(country_list)
print("csv file created successfully!")
df = pd.DataFrame(country_list, columns=["Country", "Capital", "Population", "Area"])

# Convert to numeric
df["Population"] = pd.to_numeric(df["Population"])
df["Area"] = pd.to_numeric(df["Area"])

# 1. Show first 5 rows
print(df.head())

# 2. Total countries
print("Total countries:", len(df))

# 3. Average population
print("Average population:", df["Population"].mean())

# 4. Country with highest population
print(df.loc[df["Population"].idxmax()])

# 5. Country with lowest population
print(df.loc[df["Population"].idxmin()])

# 6. Sort by population (top 5)
print(df.sort_values(by="Population", ascending=False).head())

# 7. Filter countries > 50 million population
print(df[df["Population"] > 50000000])

# 8. Add density column
df["Density"] = df["Population"] / df["Area"]

# 9. Density statistics
print(df["Density"].describe())

# 10. Countries with large area (>1M)
print("Large countries:", len(df[df["Area"] > 1000000]))