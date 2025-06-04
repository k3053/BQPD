// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BQPD {
    struct Entity {
        string uid;
        string entityType;
        address publicKey;
        bool isRegistered;
    }

    mapping(address => Entity) public registeredEntities;

    event EntityRegistered(address indexed addr, string uid, string entityType);

    function registerEntity(string memory _uid, string memory _entityType) public {
        require(!registeredEntities[msg.sender].isRegistered, "Entity already registered");
        require(
            keccak256(bytes(_entityType)) == keccak256("PS") || 
            keccak256(bytes(_entityType)) == keccak256("ECC") ||
            keccak256(bytes(_entityType)) == keccak256("TA"),
            "Invalid Entity Type"
        );

        registeredEntities[msg.sender] = Entity({
            uid: _uid,
            entityType: _entityType,
            publicKey: msg.sender,
            isRegistered: true
        });

        emit EntityRegistered(msg.sender, _uid, _entityType);
    }

    function getEntity(address _addr) public view returns (string memory, string memory, bool) {
        Entity memory entity = registeredEntities[_addr];
        return (entity.uid, entity.entityType, entity.isRegistered);
    }
}
