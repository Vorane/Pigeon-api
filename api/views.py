# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import PaymentTransaction, Wallet
from .mpesa import sendSTK
import json
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST


# Create your views here.
class SubmitView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        data = request.data
        phone_number = data['phone_number']
        amount = data['amount']
        orderId = data['order_id']

        print(phone_number)
        print(amount)
        sendSTK(phone_number, amount,orderId)
        # b2c()
        message = {"status": "ok"}
        return Response(message, status=HTTP_200_OK)


class ConfirmView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        # save the data
        request_data = json.dumps(request.data)
        request_data = json.loads(request_data)
        body = request_data.get('Body')
        print("Body " + json.dumps(body))
        resultcode = body.get('stkCallback').get('ResultCode')
        # Perform your processing here e.g. print it out...
        if resultcode == 0:
            print('Payment successful')
            requestId = body.get('stkCallback').get('CheckoutRequestID')
            transaction =  PaymentTransaction.objects.filter(checkoutRequestID=requestId).get()
            if transaction:
                transaction.isFinished = True
                transaction.isSuccessFull = True
                transaction.save()
                try:
                    wallet = Wallet.objects.filter(user=user.id).get()
                    if not wallet:
                        wallet = Wallet.objects.create(user=user,amount=transaction.amount )
                    else:
                        wallet.amount = wallet.amount + transaction.amount
                    wallet.save()
                except Wallet.DoesNotExist:
                    wallet = Wallet.objects.create(user=user, amount=transaction.amount)
                    wallet.save()

        else:
            print ('unsuccessfull')
            requestId = body.get('stkCallback').get('CheckoutRequestID')
            transaction = PaymentTransaction.objects.filter(checkoutRequestID=requestId).get()
            if transaction:
                transaction.isFinished = False
                transaction.isSuccessFull = False
                transaction.save()

        # Prepare the response, assuming no errors have occurred. Any response
        # other than a 0 (zero) for the 'ResultCode' during Validation only means
        # an error occurred and the transaction is cancelled
        message = {
            "ResultCode": 0,
            "ResultDesc": "The service was accepted successfully",
            "ThirdPartyTransID": "1237867865"
        }

        # Send the response back to the server
        return Response(message, status=HTTP_200_OK)

    def get(self, request):
        return Response("Confirm callback", status=HTTP_200_OK)


class ValidateView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        # save the data
        request_data = request.data

        # Perform your processing here e.g. print it out...
        print("validate data" + request_data)

        # Prepare the response, assuming no errors have occurred. Any response
        # other than a 0 (zero) for the 'ResultCode' during Validation only means
        # an error occurred and the transaction is cancelled
        message = {
            "ResultCode": 0,
            "ResultDesc": "The service was accepted successfully",
            "ThirdPartyTransID": "1234567890"
        };

        # Send the response back to the server
        return Response(message, status=HTTP_200_OK)
