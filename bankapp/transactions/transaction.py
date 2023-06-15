from concurrent import futures
import random

import grpc

from transaction_pb2 import TransactionResponse, TransactionRequest

import transaction_pb2_grpc 

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



class TransactionService(transaction_pb2_grpc.TransactionServiceServicer):

    def getAccount(self, account_num):
        r = None
        for acc in accounts:
            if acc.account_number == account_num:
                r = acc
                break     
        # print(f"Account {r}")
        return r
    
    def doTransaction(self, sender, receiver, amount):
        if sender.balance < amount:
            return False
        
        sender.balance -= amount
        receiver.balance += amount
        return True


    def SendMoney(self, request, context):
        
        sender_account =  self.getAccount(request.sender_account_number)
        receiver_account = self.getAccount(request.receiver_account_number)

        

        if sender_account is not None or receiver_account is not None:
            result = self.doTransaction(sender_account, receiver_account, request.amount)
            
            print(f"sender {sender_account}" )
            print(f"receiver {receiver_account}")

            if result: 
                return TransactionResponse(success=result, message="Transaction Successful")
            else:
                return TransactionResponse(success=result, message="Transaction Failed")
        
        # handle if sender or receiver account is not found
        return TransactionResponse()



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transaction_pb2_grpc.add_TransactionServiceServicer_to_server(TransactionService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()


