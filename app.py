from flask import Flask,request,jsonify

app = Flask(__name__)
# @app.route("/")
# def ram():
#     return "hello this is "
@app.route("/" , methods = ["POST"])
def get_data():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name'][0]
    print(source_currency,target_currency)
    cf = convert(source_currency,target_currency)
    final_amount = cf*amount
    # print(final_amount)
    response ={
    'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency) }
    return jsonify(response)

def convert(s_cur, t_cur):
    if s_cur == "INR" and t_cur =="USD":
        return 0.013
    if s_cur == "USD" and t_cur =="INR":
        return 75
    if s_cur == "INR" and t_cur =="GBP":
        return 0.010
    if s_cur == "GBP" and t_cur =="INR":
        return 95
    if s_cur == "GBP" and t_cur == "USD":
        return 1.20

    # print(source_currency,amount,target_currency)


if __name__ == "__main__":
    app.run(debug=True)

