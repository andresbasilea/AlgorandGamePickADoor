import algosdk
# from algosdk.v2client import algod
# from algosdk import mnemonic
# from algosdk import transaction
# from algosdk import constants
# import json
# import base64
# import time

# algod_client = algod.AlgodClient(
#    algod_token="",
#    algod_address="https://testnet-algorand.api.purestake.io/ps2",
#    headers={"X-API-Key": "6Ldr1ttQTq3a8vOnny59OamXnbMAcvgAtISf31Tc"}
# )

# basile_keller_address = "LLIW67OEIG54QBZA4NSI4RCFP5YEH37DOV3CMFSZLCSLQDMB2GBK5LURR4"
# private_key_basile_keller = mnemonic.to_private_key("")



def create_account():
	# Generate a fresh private key and associated account address
	private_key, account_address = algosdk.account.generate_account()

	# Convert the private key into a mnemonic which is easier to use
	mnemonic = algosdk.mnemonic.from_private_key(private_key)

	print("Private key mnemonic: " + mnemonic)
	print("Account address: " + account_address)


# def create_account_fund_basile_keller():
# 	# Generate a fresh private key and associated account address
# 	private_key, account_address = algosdk.account.generate_account()

# 	# Convert the private key into a mnemonic which is easier to use
# 	mnemonic = algosdk.mnemonic.from_private_key(private_key)

# 	print("Private key mnemonic: " + mnemonic)
# 	print("Account address: " + account_address)

# 	time.sleep(10)

# 	account_info_basile_keller = algod_client.account_info(basile_keller_address)
# 	params = algod_client.suggested_params()
# 	# comment out the next two (2) lines to use suggested fees
# 	params.flat_fee = True
# 	params.fee = constants.MIN_TXN_FEE
# 	receiver = "LLIW67OEIG54QBZA4NSI4RCFP5YEH37DOV3CMFSZLCSLQDMB2GBK5LURR4"
# 	note = "Fund Basile Keller".encode()
# 	amount = 1000000 * 10
# 	unsigned_txn = transaction.PaymentTxn(account_address, params, receiver, amount, None, note)

# 	# sign transaction
# 	signed_txn = unsigned_txn.sign(private_key)

# 	#submit transaction
# 	txid = algod_client.send_transaction(signed_txn)
# 	print("Successfully sent transaction with txID: {}".format(txid))

# 	# wait for confirmation
# 	try:
# 	    confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
# 	except Exception as err:
# 	    print(err)


# 	print("Transaction information: {}".format(json.dumps(confirmed_txn, indent=4)))
# 	print("Decoded note: {}".format(base64.b64decode(confirmed_txn["txn"]["txn"]["note"]).decode()))
# 	print("Starting Account balance: {} microAlgos".format(account_info.get('amount')))
# 	print("Amount transfered: {} microAlgos".format(amount))
# 	print("Fee: {} microAlgos".format(params.fee))

# 	account_info = algod_client.account_info(my_address)
# 	print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")
