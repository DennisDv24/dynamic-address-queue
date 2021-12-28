// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DynamicAddressQueue {
	
	struct Node {
		address value;
		address nextNodeAddress;
	}
	
	address private _headAddress = address(0);
	mapping(address => Node) private _getNodeFromAddress;
	
	function enqueue(address addr) external {
		// TODO isEmpty() function?
		if(isEmpty())
			_caseBaseEnqueue(addr);
		else
			_genericEnqueue(addr);
	}

	function isEmpty() public returns(bool) {
		return _headAddress == address(0);
	}

	function _caseBaseEnqueue(address addr) private {
		Node memory firstNode = Node(addr, addr);
		_getNodeFromAddress[addr] = firstNode;
		_headAddress = addr;
	}

	function _genericEnqueue(address addr) private {
		Node memory headNode = _getNodeFromAddress[_headAddress];
		_getNodeFromAddress[addr] = Node(addr, headNode.nextNodeAddress);
		_getNodeFromAddress[_headAddress].nextNodeAddress = addr;
		_headAddress = addr;

	}
	
	function dequeue() external returns (address toReturn) {
		Node memory headNode = _getNodeFromAddress[_headAddress];
		if(headNode.nextNodeAddress == headNode.value) {
			toReturn = headNode.value;
			delete _getNodeFromAddress[_headAddress];
			_headAddress = address(0);
		} else {
			toReturn = headNode.nextNodeAddress;
			Node memory nextNodeToHead = _getNodeFromAddress[headNode.nextNodeAddress];
			headNode.nextNodeAddress = nextNodeToHead.nextNodeAddress;
			delete _getNodeFromAddress[toReturn];
		}
	}
	
	// NOTE Only for testing purpose
	function printQueue() public returns (string memory) {
		return "test";
	}

}
