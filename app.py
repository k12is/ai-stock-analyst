import yfinance as yf
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for API accessibility

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
            "Momentum Signal": "Strong Bullish" if info.get('currentPrice', 0) > info.get('fiftyTwoWeekLow', 0) * 1.5 else "Neutral" if info.get('currentPrice', 0) > info.get('fiftyTwoWeekLow', 0) * 1.2 else "Bearish",
            "Investment Insight": "Stock is in a strong uptrend, potential for growth." if info.get('currentPrice', 0) > info.get('fiftyTwoWeekHigh', 0) * 0.9 else "Approaching resistance, consider technical analysis."
        }
        return {"status": "success", "data": analysis}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to AI Stock Analyst API.",
        "usage": "Use /analyze?ticker=STOCK_SYMBOL (e.g., /analyze?ticker=AAPL) to get stock analysis.",
        "status": "API is running"
    }), 200

@app.route('/analyze', methods=['GET'])
def analyze():
    ticker = request.args.get('ticker', '').upper()
    if not ticker:
        return jsonify({"status": "error", "message": "Please provide a valid stock ticker symbol."}), 400
    
    stock_data = get_stock_analysis(ticker)
    stock_data["Disclaimer"] = "Invest at your own risk. This is not financial advice."  # Small professional disclaimer
    return jsonify(stock_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
