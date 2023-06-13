import random
from algosdk import account, transaction
from algosdk.v2client import algod

# Algorand node configuration
algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = "6Ldr1ttQTq3a8vOnny59OamXnbMAcvgAtISf31Tc"

# Account mnemonic for funding the game
mnemonic_phrase = ""

# Door options
doors = ["Door 1", "Door 2", "Door 3"]

# Prize amount
prize_amount = 1000  # In microAlgos

# Initialize Algod client
algod_client = algod.AlgodClient(algod_token, algod_address)

def create_account():
    private_key, address = account.generate_account()
    return private_key, address

def fund_account(address, amount):
    params = algod_client.suggested_params()
    params.flat_fee = True
    params.fee = 1000
    txn = transaction.PaymentTxn(address, params, address, amount)
    signed_txn = txn.sign(private_key)
    algod_client.send_transaction(signed_txn)
    return txn.get_txid()

def select_door():
    print("Available doors:")
    for i, door in enumerate(doors):
        print(f"{i + 1}. {door}")
    door_index = int(input("Choose a door (enter the corresponding number): "))
    if door_index < 1 or door_index > len(doors):
        print("Invalid door selection!")
        return None
    return door_index - 1

def play_game():
    print("Welcome to the Algorand game!")
    private_key, address = create_account()
    print(f"Your account address: {address}")
    print("Funding your account...")
    tx_id = fund_account(address, prize_amount * 2)  # Fund the account with twice the prize amount
    print(f"Account funded! Transaction ID: {tx_id}")

    chosen_door = select_door()
    if chosen_door is None:
        return

    print("Game in progress...")
    winning_door = random.randint(0, len(doors) - 1)

    if chosen_door == winning_door:
        print("Congratulations! You won the prize!")
        tx_amount = prize_amount * 2
    else:
        print("Sorry, you didn't win this time.")
        tx_amount = 0

    print("Transferring the prize...")
    params = algod_client.suggested_params()
    params.flat_fee = True
    params.fee = 1000
    txn = transaction.PaymentTxn(address, params, address, tx_amount)
    signed_txn = txn.sign(private_key)
    algod_client.send_transaction(signed_txn)
    print("Prize transferred!")

play_game()
