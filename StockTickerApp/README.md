 # Stock Ticker App
 
- The Stock Ticker App is a project to display skills in:
  - Backend Python
  - Web App Development
  - SQL Databases
  - Frontend Javascript and HTML

- The app uses a Web App to display live or the previous days stock data for given tickers.
  - It uses Python to gather the stock data and store it in a Database and host the app. 
  - JS is then used to fetch the data from the database through python and display the stock data
 
 ![alt text](assets/ClosedMarketExample.png "Title")

- Project is at a basic functionality stage
- Future updates will show extra market data and hopefully some time series analysis and stock predictions


## How to use
NB - These instructions are for the current setup (28 Oct 22) as the code design is not finalised
- Add the details of your mySQL database login to config/db_login.yaml
 - For other SQL types you will need to change the URI string returned from utils.get_uri()
- Run main.py 
 -(currently set to debug mode and port 4444 as 5000 is no longer available on MacOS Ventura, these params can be changed from top of main.py). Any edits to the app.run() will needed to be made to the AppClass.run() in the app.py file
- Open localhost link
