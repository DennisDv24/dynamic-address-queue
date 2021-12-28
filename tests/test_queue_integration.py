from brownie import DynamicAddressQueue as queue
from brownie import accounts, config, network
from scripts.utils import get_account
import pytest

def test_multiple_actions():
    main_acc = get_account()
    q = queue.deploy(
        {'from': main_acc},
        publish_source = config['networks'][network.show_active()].get('verify', False)
    )
    accs = [
        '0x7A1Ca128f581eA57862EE463fCc7DEeA7b7De4f8',
        '0x0000000000000000000000000000000000000007', #
        '0x0000000000000000000000000000999999999999', #
        '0x000000000000000000000000000000000000dEaD', 
        '0x86D3E894b5CDb6a80affFd35eD348868fb98DD3f',
        '0xDFA0B3fCf7B9E6e1BFB8ef536Aa33B5aF6Fd7F47',
        '0x78E7a154287134f913057dc1692541f19eCD37BB',
        '0x0000000000000000000088888888888888888888',
        '0x0000000000000000000000000000000000000002', #
        '0x1000000000000000000000000000000000000001',
        '0x0000000000000000000000000000000000022222' #
    ]
    actions = [
        ('isempty', True),
        ('enqueue', accs[7]),
        ('dequeue', accs[7]),
        ('isempty', True),
        ('isempty', True),
        ('enqueue', accs[3]),
        ('enqueue', accs[7]),
        ('dequeue', accs[3]),
        ('isempty', False),
        ('enqueue', accs[0]),
        ('isempty', False),
        ('enqueue', accs[3]),
        ('enqueue', accs[4]),
        ('isempty', False),
        ('dequeue', accs[7]),
        ('isempty', False),
        ('dequeue', accs[0]),
        ('isempty', False),
        ('enqueue', accs[5]),
        ('dequeue', accs[3]),
        ('isempty', False),
        ('dequeue', accs[4]),
        ('enqueue', accs[4]),
        ('enqueue', accs[0]),
        ('isempty', False),
        ('enqueue', accs[3]),
        ('isempty', False),
        ('dequeue', accs[5]),
        ('dequeue', accs[4]),
        ('isempty', False),
        ('dequeue', accs[0]),
        ('dequeue', accs[3]),
        ('isempty', True),
        ('enqueue', accs[9]),
        ('enqueue', accs[0]),
        ('isempty', False),
        ('dequeue', accs[9]),
        ('isempty', False),
        ('dequeue', accs[0]),
        ('isempty', True),
        ('isempty', True)
    ]

    for action in actions:
        print(action)
        print(len(action)*'-')
        if action[0] == 'isempty':
            is_empty = q.isEmpty()
            print('\tqueue is empty:', is_empty)
            print('\texpected is empty:', action[1])
            assert is_empty == action[1]
        elif action[0] == 'enqueue':
            print('\tenqueued', action[1])
            q.enqueue(action[1], {'from': main_acc})
        elif action[0] == 'dequeue':
            # NOTE theres not .return_value becuase .return_value
            # is only used in local envs
            q.dequeue({'from': main_acc})
            deq = q.lastReturnedAddress()
            print('\tdequeued', deq)
            print('\texpected', action[1])
            assert deq == action[1]
        print('\n')
    





