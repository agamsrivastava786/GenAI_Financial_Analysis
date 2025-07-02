from flask import Flask, request, render_template_string

app = Flask(__name__)

financial_data = {
    "total_revenue": "$500 million",
    "net_income_change": "increased by $50 million",
    "gross_margin": "30%",
    "operating_expenses": "$120 million",
    "profit_growth": "5% year-over-year"
}

responses = {
    "What is the total revenue?": f"The total revenue is {financial_data['total_revenue']}.",
    "How has net income changed over the last year?": f"The net income has {financial_data['net_income_change']}.",
    "What is the gross margin?": f"The gross margin is {financial_data['gross_margin']}.",
    "What are the total operating expenses?": f"The total operating expenses are {financial_data['operating_expenses']}.",
    "What is the profit growth rate?": f"The profit has grown by {financial_data['profit_growth']}."
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Financial Chatbot</title></head>
<body>
    <h2>GFC Financial Chatbot</h2>
    <form method="post">
        <input name="query" style="width: 400px;">
        <input type="submit">
    </form>
    <p><strong>Bot:</strong> {{ response }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_query = request.form["query"]
        response = responses.get(user_query, "Sorry, I can only provide information on predefined queries.")
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
