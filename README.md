# Python Stock Analyzer (Flask Web App)

This project is a **web-based Stock Analysis tool** built with **Python and Flask**, designed to analyze historical stock market data, visualize trends, and evaluate stock performance. The web interface allows users to search for any ticker, choose custom date ranges, and see detailed visualizations powered by the Yahoo Finance API.

This tool helps investors and enthusiasts:

- Analyze historical price data
- Visualize 20-day moving averages
- View daily return volatility
- Inspect basic company information

> Data is powered by [Yahoo Finance](https://finance.yahoo.com/)

[Software Demo Video](https://youtu.be/)

---

## Features

- User-friendly web form to enter stock ticker and date range
- Responsive design using **Bootstrap 5**
- Data visualizations with **Matplotlib**
- Key statistics and historical summary table
- Ticker validation and error handling
- Powered by Flask — ready to deploy

---

## Development Environment

| Tool / Library | Purpose                       |
| -------------- | ----------------------------- |
| Python 3       | Core programming language     |
| Flask          | Web framework                 |
| Pandas         | Data manipulation             |
| yFinance       | Fetch stock data from Yahoo   |
| Matplotlib     | Data visualization            |
| Tabulate       | Console-based tables          |
| Bootstrap 5    | UI styling and responsiveness |

---

## Live Demo / Run Locally

To run this project locally:

```bash
git clone https://github.com/your-username/your-repo-name
cd your-repo-name
pip install -r requirements.txt
python app.py
```

---

## Useful Websites

- [Yahoo Finance](https://finance.yahoo.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)

---

## Future Work

- Add real-time news integration for tickers
- Implement machine learning models for price prediction
- Add more technical indicators (e.g., RSI, MACD, Bollinger Bands)
- Enable export to CSV/Excel for downloaded data
- Deploy the app to a cloud platform like Render or Heroku
