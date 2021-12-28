from brownie import DynamicAddressQueue as queue
from brownie import accounts
from scripts.utils import get_account
import pytest

def test_queue_is_empty():
    acc = get_account()
    q = queue.deploy({'from': acc})
    assert q.isEmpty() == True

def test_enqueue_and_dequeue_one_address():
    main_acc = get_account()
    q = queue.deploy({'from': main_acc})
    acc_to_enqueue_index = 3
    q.enqueue(accounts[acc_to_enqueue_index], {'from': main_acc})
    returned_address = q.dequeue({'from': main_acc}).return_value
    assert returned_address == accounts[acc_to_enqueue_index]

def test_dequeue_enqueue_and_isempty():
    main_acc = get_account()
    q = queue.deploy({'from': main_acc})
    acc_to_enqueue_index = 3
    q.enqueue(accounts[acc_to_enqueue_index], {'from': main_acc})
    returned_address = q.dequeue({'from': main_acc}).return_value
    assert returned_address == accounts[acc_to_enqueue_index]
    assert q.isEmpty() == True

def test_two_enqueues_map():
    main_acc = get_account()
    q = queue.deploy({'from': main_acc})
    q.enqueue(accounts[0], {'from': main_acc})
    q.enqueue(accounts[1], {'from': main_acc})
    t1 = q.getNodeFromAddress(accounts[0])
    t2 = q.getNodeFromAddress(accounts[1])
    assert t1[0] == accounts[0]
    assert t1[1] == accounts[1]
    assert t2[0] == accounts[1]
    assert t2[1] == accounts[0]

    

def test_multiples_enqueues_map():
    main_acc = get_account()
    q = queue.deploy({'from': main_acc})
    accs = [accounts[3], accounts[4], accounts[1], accounts[8], accounts[5]]
    for acc in accs:
        q.enqueue(acc, {'from': main_acc})
        print(acc)

    
    for i in range(len(accs)):
        acc_tuple = q.getNodeFromAddress(accs[i])
        assert acc_tuple[0] == accs[i]
        if(i == len(accs) - 1):
            assert acc_tuple[1] == accs[0]
        else:
            assert acc_tuple[1] == accs[i+1]



def test_multiples_enqueues_and_dequeues():
    main_acc = get_account()
    q = queue.deploy({'from': main_acc})
    accs = [accounts[3], accounts[4], accounts[1], accounts[8], accounts[5]]
    for acc in accs:
        q.enqueue(acc, {'from': main_acc})
        print(acc)
    
    print('-----------')

    for acc in accs:
        dequeued_value = q.dequeue({'from': main_acc}).return_value
        assert dequeued_value == acc
    
def test_multiples_enqueues_dequeues_and_isempty():
    main_acc = get_account()
    q = queue.deploy({'from': main_acc})
    accs = [accounts[3], accounts[4], accounts[1], accounts[8], accounts[5]]
    for acc in accs:
        q.enqueue(acc, {'from': main_acc})
        print(acc)
    
    print('-----------')

    for acc in accs:
        dequeued_value = q.dequeue({'from': main_acc}).return_value
        assert dequeued_value == acc

    assert q.isEmpty()

def test_multiple_actions():
    main_acc = get_account()
    q = queue.deploy({'from': main_acc})
    actions = [
        ('isempty', True),
        ('enqueue', accounts[7]),
        ('dequeue', accounts[7]),
        ('isempty', True),
        ('isempty', True),
        ('enqueue', accounts[3]),
        ('enqueue', accounts[7]),
        ('dequeue', accounts[3]),
        ('isempty', False),
        ('enqueue', accounts[0]),
        ('isempty', False),
        ('enqueue', accounts[3]),
        ('enqueue', accounts[4]),
        ('isempty', False),
        ('dequeue', accounts[7]),
        ('isempty', False),
        ('dequeue', accounts[0]),
        ('isempty', False),
        ('enqueue', accounts[5]),
        ('dequeue', accounts[3]),
        ('isempty', False),
        ('dequeue', accounts[4]),
        ('enqueue', accounts[4]),
        ('enqueue', accounts[0]),
        ('isempty', False),
        ('enqueue', accounts[3]),
        ('isempty', False),
        ('dequeue', accounts[5]),
        ('dequeue', accounts[4]),
        ('isempty', False),
        ('dequeue', accounts[0]),
        ('dequeue', accounts[3]),
        ('isempty', True),
        ('enqueue', accounts[9]),
        ('enqueue', accounts[0]),
        ('isempty', False),
        ('dequeue', accounts[9]),
        ('isempty', False),
        ('dequeue', accounts[0]),
        ('isempty', True),
        ('isempty', True)
    ]

    for action in actions:
        if action[0] == 'isempty':
            assert q.isEmpty() == action[1]
        elif action[0] == 'enqueue':
            q.enqueue(action[1], {'from': main_acc})
        elif action[0] == 'dequeue':
            assert q.dequeue({'from': main_acc}).return_value == action[1]
    





