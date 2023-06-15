# marketplace/marketplace.py
import os

from flask import Flask, render_template, request
import grpc

from account_details_pb2 import GetAccountDetailsRequest
from account_details_pb2_grpc import AccountDetailsServiceStub

from transaction_pb2_grpc import TransactionServiceStub
from transaction_pb2 import TransactionRequest

from loan_pb2_grpc import LoanServiceStub
from loan_pb2 import LoanRequest, LoanResponse


app = Flask(__name__)




@app.route("/")
def render_homepage():
    account_details_host = os.getenv("ACCOUNT_DETAILS_HOST", "localhost")
    account_details_channel = grpc.insecure_channel(f"{account_details_host}:50051")
    account_details_client = AccountDetailsServiceStub(account_details_channel)

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



@app.route('/loan', methods=['GET', 'POST'])
def loan_form():
    # gRPC setup
    channel = grpc.insecure_channel('localhost:50053')
    client = LoanServiceStub(channel)
    if request.method == 'POST':
        account_number = request.form['account_number']
        amount = float(request.form['amount'])

        # Create a gRPC request
        loan_request = LoanRequest(account_number=account_number, amount=amount)

        # Send the gRPC request to the Loan Microservice
        response = client.ProcessLoanRequest(loan_request)
        # response.account_number = account_number

        print(f"Loan response: {response.approved}")

        return f"Loan Response: {response}"   #render_template('loan_result.html', response=response)

    return render_template('loan_form.html')


if __name__ == "__main__":
    app.run(debug=True)
