from scripts.utils import get_account
from brownie import DynamicAddressQueue as queue
from brownie import accounts
from web3 import Web3

def deploy_queue():
    acc = get_account()
    return queue.deploy({'from': acc})

def add_elements(q):
    for acc in accounts:
        q.enqueue(acc, {'from': get_account()})

def print_queue(q):
    for acc in accounts:
        t = q.getNodeFromAddress(acc)
        print('(' + t[0][:5]+'...'+', '+t[1][:5]+'...'+ ')')
    print('HEAD: ', q.getHeadAddress())

def main():
    q = deploy_queue()
    add_elements(q)
    print_queue(q)

