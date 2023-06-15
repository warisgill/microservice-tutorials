from concurrent import futures
import random

import grpc


from account_details_pb2 import GetAccountDetailsResponse, Account

import account_details_pb2_grpc


# creat a list of accounts and fill with dummy data

accounts = []
for i in range(1, 10):
    account = Account()
    account.account_number = str(i)
    account.account_holder_name = "Account Holder " + str(i)
    account.balance = random.randint(1000, 10000)
    account.currency = "USD"
    accounts.append(account)



class AccountDetailsService(account_details_pb2_grpc.AccountDetailsServiceServicer):

    def GetAccountDetails(self, request, context):
        for account in accounts:
            if account.account_number == request.account_number:
                return GetAccountDetailsResponse(account=account)
        return GetAccountDetailsResponse()
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    account_details_pb2_grpc.add_AccountDetailsServiceServicer_to_server(AccountDetailsService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
