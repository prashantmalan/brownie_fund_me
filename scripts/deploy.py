from brownie import accounts, network, FundMe, MockV3Aggregator, config
from scripts.helpful_script import get_account, deploy_mocks, LOCAL_DEPLOPMENT_ENV
from web3 import Web3

# account = get_account()
def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_DEPLOPMENT_ENV:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        print(f"goerli price_feed_address {price_feed_address}")
    else:
        print("dev or ganache network")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        # Pass the price_feed address to  fundME
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    return fund_me


def main():
    deploy_fund_me()
