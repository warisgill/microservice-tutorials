# marketplace/marketplace.py
import os

from flask import Flask, render_template, request
import grpc

from account_details_pb2 import GetAccountDetailsRequest
from account_details_pb2_grpc import AccountDetailsServiceStub

from transaction_pb2_grpc import TransactionServiceStub
from transaction_pb2 import TransactionRequest, TransactionResponse


app = Flask(__name__)

account_details_host = os.getenv("ACCOUNT_DETAILS_HOST", "localhost")
account_details_channel = grpc.insecure_channel(f"{account_details_host}:50051")
account_details_client = AccountDetailsServiceStub(account_details_channel)


@app.route("/")
def render_homepage():
    account_details_request = GetAccountDetailsRequest(account_number="1")
    account_details_response = account_details_client.GetAccountDetails(
        account_details_request
    )
    return render_template(
        "homepage.html", account=account_details_response.account
    )

@app.route('/transaction', methods=['GET', 'POST'])
def transaction_form():
    if request.method == 'POST':
        sender_account_number = request.form['sender_account_number']
        receiver_account_number = request.form['receiver_account_number']
        amount = float(request.form['amount'])

        channel = grpc.insecure_channel('localhost:50052')
        client = TransactionServiceStub(channel)

        req = TransactionRequest(
            sender_account_number=sender_account_number,
            receiver_account_number=receiver_account_number,
            amount=amount
        )

        print("Sending transaction request...")

        response = client.SendMoney(req)

        return f"Transaction successful. Transaction ID: {response}"
    
    return render_template('transaction.html')

if __name__ == "__main__":
    app.run(debug=True)
