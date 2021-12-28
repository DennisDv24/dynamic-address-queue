// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DynamicAddressQueue {
	
	struct Node {
		address value;
		bytes32 nextNodeId;
	}
	
	bytes32 private _headId;
	mapping(bytes32 => Node) private _getNodeFromId;
	uint256 private _queueLength;
	
	function enqueue(address addr) external {
		// TODO isEmpty() function?
		if(_queueLength == 0)
			_caseBaseEnqueue(addr);
		else
			_genericEnqueue(addr);
	}

	function _caseBaseEnqueue(address addr) private {
		Node memory firstNode = Node(addr, 0);
		_headId = _generateNodeId(firstNode);
		firstNode.nextNodeId = _headId;
		_getNodeFromId[_headId] = firstNode;
	}

	function _genericEnqueue(address addr) private {
		bytes32 auxNodeId = _getNodeFromId[_headId].nextNodeId;
		Node memory newNode = Node(addr, auxNodeId);
		bytes32 newNodeId = _generateNodeId(newNode);
		_getNodeFromId[newNodeId] = newNode;
		_getNodeFromId[_headId].nextNodeId = newNodeId;
		_headId = _getNodeFromId[_headId].nextNodeId;
		_queueLength++;
	}

	function _generateNodeId(Node memory n) private returns(bytes32) {
		// NOTE n.value should be unique in my use case
		return keccak256(abi.encode(n.value));
	}

	function dequeue() external returns (address toReturn) {
		bytes32 auxNextNodeId = _getNodeFromId[_headId].nextNodeId;
		toReturn = _getNodeFromId[auxNextNodeId].value;
		bytes32 headNextId = _getNodeFromId[_headId].nextNodeId;
		bytes32	headNextNextId = _getNodeFromId[headNextId].nextNodeId;
		_getNodeFromId[_headId].nextNodeId = headNextNextId;
		_queueLength--;
	}

}
