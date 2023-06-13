from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk import transaction
from algosdk import constants
import json
import base64
import algorandGameCreateAccount


base = 1000000

#Conexión con el cliente
#Si usas PureStake

algod_client = algod.AlgodClient(
   algod_token="",
   algod_address="https://testnet-algorand.api.purestake.io/ps2",
   headers={"X-API-Key": "6Ldr1ttQTq3a8vOnny59OamXnbMAcvgAtISf31Tc"}
)


basile_keller_address = "LLIW67OEIG54QBZA4NSI4RCFP5YEH37DOV3CMFSZLCSLQDMB2GBK5LURR4"
private_key_basile_keller = mnemonic.to_private_key("leader file floor alien layer yard film pupil stamp strong stadium income life silk bargain glow diagram first wreck gorilla story uphold wink ability genuine")

#Verificando el balance de la cuenta


# print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")


my_address = ""
private_key_my_address = ""
account_info_my_address = None

def get_public_key_user(my_address_entry):
   global my_address, account_info_my_address
   my_address = my_address_entry
   account_info_my_address = algod_client.account_info(my_address)

def get_private_key_user(private_key_my_address_entry):
   global private_key_my_address
   private_key_my_address = mnemonic.to_private_key(private_key_my_address_entry)

account_info_basile_keller = algod_client.account_info(basile_keller_address)

def get_balance():
   if account_info_my_address is None:
      return 0.0
   balance = account_info_my_address['amount']
   return balance

def check_balance(amount):
   if account_info_my_address.get('amount') < amount:
      # print("Not enough funds!")
      return False
   return True


def client_looses(amount):
   global base
   params = algod_client.suggested_params()
   params.flat_fee = True
   params.fee = constants.MIN_TXN_FEE
   receiver = basile_keller_address # Basile Keller Account to receive
   note = "Client Looses".encode()
   amount = base * amount

   if check_balance(amount):
      unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)

      # sign transaction
      signed_txn = unsigned_txn.sign(private_key_my_address)

      #submit transaction
      txid = algod_client.send_transaction(signed_txn)
      print("Successfully sent transaction with txID: {}".format(txid))

      # wait for confirmation
      try:
          confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
      except Exception as err:
          print(err)

      print("Transaction information: {}".format(json.dumps(confirmed_txn, indent=4)))
      print("Decoded note: {}".format(base64.b64decode(confirmed_txn["txn"]["txn"]["note"]).decode()))
      print("Starting Account balance: {} microAlgos".format(account_info_my_address.get('amount')))
      print("Amount transfered: {} microAlgos".format(amount))
      print("Fee: {} microAlgos".format(params.fee))
   


def client_wins(amount):
   global base
   params = algod_client.suggested_params()
   params.flat_fee = True
   params.fee = constants.MIN_TXN_FEE
   receiver = my_address # Basile Keller Account to receive
   note = "Client Wins".encode()
   amount = base * amount * 2

   if account_info_basile_keller.get('amount') < amount:
      print("Not enough funds from basile_keller_address, please wait!")

   unsigned_txn = transaction.PaymentTxn(basile_keller_address, params, receiver, amount, None, note)

   # sign transaction
   signed_txn = unsigned_txn.sign(private_key_basile_keller)

   #submit transaction
   txid = algod_client.send_transaction(signed_txn)
   print("Successfully sent transaction with txID: {}".format(txid))

   # wait for confirmation
   try:
       confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
   except Exception as err:
       print(err)

   print("Transaction information: {}".format(json.dumps(confirmed_txn, indent=4)))
   print("Decoded note: {}".format(base64.b64decode(confirmed_txn["txn"]["txn"]["note"]).decode()))
   print("Starting Account balance: {} microAlgos".format(account_info_my_address.get('amount')))
   print("Amount transfered: {} microAlgos".format(amount))
   print("Fee: {} microAlgos".format(params.fee))


# TODO #mejorar las validaciones
      #no permitir al usuario apostar, revisar el saldo antes de la apuesta
