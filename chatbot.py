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

def simple_chatbot():
    print("Welcome to the GFC Financial Chatbot. Ask a question (type 'exit' to quit):")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Chatbot: Thank you. Goodbye!")
            break
        response = responses.get(user_query, "Sorry, I can only provide information on predefined queries.")
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    simple_chatbot()

def simple_chatbot(user_query):
   if user_query == "What is the total revenue?":
       return "The total revenue is [amount]."
   elif user_query == "How has net income changed over the last year?":
       return "The net income has [increased/decreased] by [amount] over the last year."
   # Add more conditions for other predefined queries
   else:
       return "Sorry, I can only provide information on predefined queries."