from scripts.utils import get_account
from brownie import DynamicAddressQueue as queue
from web3 import Web3

def deploy_queue():
    acc = get_account()
    q = queue.deploy(
        {'from': acc},
        publish_source = True
    )


def main():
    deploy_queue()
