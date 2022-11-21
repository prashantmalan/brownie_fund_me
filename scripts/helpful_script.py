from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

FORKED_MAINNET_ENVIORNMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_DEPLOPMENT_ENV = ["development", "ganache-local"]
DECIMALS = 18
STARTING_VALUE = 2000

acc = ""


def get_account():
    if (
        network.show_active() in LOCAL_DEPLOPMENT_ENV
        or network.show_active() in FORKED_MAINNET_ENVIORNMENT
    ):
        print(accounts[0])
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


print(acc)


def deploy_mocks():
    print(f"Active network= {network.show_active()}")
    print(f"Deploying Mock...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_VALUE, "ether"), {"from": get_account()}
        )
    print("Mock DEployed")
