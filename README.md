# Suitable-Lodging
This project aims to help you choose the most optimal apartment on the market in terms of price-time (before your work) ratio


The "lodging.py" file downloads data about the offered apartments from the "avito.ru" website into three lists: "adresses.csv", "links.csv" and "prices.csv"
Then the "routing.py" file runs a script, simulating user actions, on the "yandex.ru/maps" site to determine the travel time by public transport to the selected point (your work) from each of the apartments offered on the market
Now you have a list of the cost of apartments and time costs. The following actions are performed manually by the user in Google Sheets / Excel
Knowing the cost of your time, you can calculate the total cost of the apartment in terms of monetary and time costs and sort the list according to the most optimal ones
