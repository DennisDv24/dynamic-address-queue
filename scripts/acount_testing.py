from brownie import DynamicAddressQueue as queue
from brownie import accounts
from scripts.utils import get_account

def basic_test_deploy():
    main_acc = get_account()
    q = queue.deploy({'from': main_acc})
    addr_to_add = '0x7A1Ca128f581eA57862EE463fCc7DEeA7b7De4f8'
    q.enqueue(addr_to_add, {'from': main_acc})
    returned_address = q.dequeue({'from': main_acc}).return_value
    print(returned_address)

def main():
    basic_test_deploy()
