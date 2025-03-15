import yfinance as yf
from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    def get_stock_analysis(ticker):
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            # Perform quantitative & qualitative analysis
            analysis = {
                "Company Name": info.get("longName", "N/A"),
                "Symbol": ticker.upper(),
                "Current Price": f"${info.get('currentPrice', 'N/A')}",
                "Market Cap": f"${info.get('marketCap', 'N/A'):,}",
                "PE Ratio": info.get("trailingPE", "N/A"),
                "52-Week High": f"${info.get('fiftyTwoWeekHigh', 'N/A')}",
                "52-Week Low": f"${info.get('fiftyTwoWeekLow', 'N/A')}",
                "Dividend Yield": info.get("dividendYield", "N/A"),
                "Sector": info.get("sector", "N/A"),
                "Recommendation": info.get("recommendationKey", "N/A"),
                "Analyst Target Price": f"${info.get('targetMeanPrice', 'N/A')}",
                "Momentum Signal": "Bullish" if info.get('currentPrice', 0) > info.get('fiftyTwoWeekLow', 0) * 1.2 else "Neutral",
                "Investment Insight": "Stock is in an uptrend, consider further technical analysis." if info.get('currentPrice', 0) > info.get('fiftyTwoWeekHigh', 0) * 0.8 else "Stock is near resistance, be cautious."
            }
            return analysis
        except Exception as e:
            return {"error": str(e)}

    @app.route('/analyze', methods=['GET'])
    def analyze():
        ticker = request.args.get('ticker', '').upper()
        if not ticker:
            return jsonify({"error": "Please provide a valid stock ticker symbol."})
        
        stock_data = get_stock_analysis(ticker)
        stock_data["Disclaimer"] = "Invest at your own risk. This is not financial advice."  # Small professional disclaimer
        return jsonify(stock_data)

    return app

app = create_app()
