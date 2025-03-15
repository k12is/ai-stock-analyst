import yfinance as yf
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_stock_analysis(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
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
            "Analyst Target Price": f"${info.get('targetMeanPrice', 'N/A')}"
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
    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)
