from brownie import FundMe, MockV3Aggregator, config
from scripts.helpful_script import get_account
from web3 import Web3


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    # print(f" price pf ETH {fund_me.getPrice()}")
    # print(f"conversion rate  with USD is {fund_me.getConversionRate(1)}")
    print(entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f"Contract deplyed to  {fund_me.address}")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


# print(f"The entrance fee is {entrance_fee}")
# print("funding")
# fund_me.fund({"from": account, "value": entrance_fee})


def main():
    fund()
    withdraw()
