from concurrent import futures
import random

import grpc

from loan_pb2 import LoanResponse
import loan_pb2_grpc

class Account:
    def __init__(self):
        self.account_number = ""
        self.account_holder_name = ""
        self.balance = 0.0
        self.currency = ""

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder Name: {self.account_holder_name}, Balance: {self.balance}, Currency: {self.currency}"



accounts = []
for i in range(1, 10):
    account = Account()
    account.account_number = str(i)
    account.account_holder_name = "Account Holder " + str(i)
    account.balance = 100
    account.currency = "USD"
    accounts.append(account)


class LoanService(loan_pb2_grpc.LoanServiceServicer):
    def ProcessLoanRequest(self, request, context):

        account = self.getAccount(request.account_number)

        if account is None:
            return LoanResponse(approved=False)
        result =  self.approveLoan(account, request.amount)
        print(f"Result {result}")

        message = "Loan Approved" if result else "Loan Rejected"

        response = LoanResponse(approved=result,  message=message)
        print(f"Account: {account}")
        print(f"Response: {response}")
        return response
    
    def getAccount(self, account_num):
        r = None
        for acc in accounts:
            if acc.account_number == account_num:
                r = acc
                break     
        # print(f"Account {r}")
        return r
    
    def approveLoan(self, account, amount):
       
       if amount < 1:
           return False

       account.balance += amount
       return True


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    loan_pb2_grpc.add_LoanServiceServicer_to_server(LoanService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()