from scripts.helpful_script import get_account, LOCAL_DEPLOPMENT_ENV
from scripts.deploy import deploy_fund_me
from brownie import FundMe, network, accounts, exceptions
import pytest


def test_can_fund_and_withdrawl():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    txn = fund_me.fund({"from": account, "value": entrance_fee})
    txn.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw()
    tx2.wait(2)


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_DEPLOPMENT_ENV:
        {pytest.skip("only or local network")}
    account = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    # fund_me.withdraw({"from": bad_actor})
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})


def main():
    test_can_fund_and_withdrawl()
