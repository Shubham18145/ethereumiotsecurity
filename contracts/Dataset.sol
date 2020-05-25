pragma solidity ^0.5.0;
//pragma experimental ABIEncoderV2;

contract Dataset {
  struct Data {
    uint id;
    string item;
    uint category; //to idetify filenames of dataset
  }
  Data[] public dataobj;
  uint public nextId = 1;

  function insert(string memory data_item, uint category) public {
    dataobj.push(Data(nextId, data_item, category));
    nextId++;
  }


  function read(uint id) view public returns(uint, string memory, uint){
    uint index = find(id);
    return (dataobj[index].id, dataobj[index].item, dataobj[index].category);
  }

  function destroy(uint id) public {
    uint index = find(id);
    delete dataobj[index];
  }

  function find(uint id) view internal returns(uint) {
    for(uint i = 0; i < dataobj.length; i++) {
      if(dataobj[i].id == id) {
        return i;
      }
    }
    revert('Data item does not exist!');
  }

}
