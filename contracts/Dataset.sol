pragma solidity ^0.5.0;
//pragma experimental ABIEncoderV2;

contract Dataset {
  struct Data {
    uint id;
    string item;
    string label; //to idetify filenames of dataset
  }
  Data[] public dataobj;
  uint public nextId = 1;

  function insert(string memory data_item, string memory label) public {
    dataobj.push(Data(nextId, data_item, label));
    nextId++;
  }


  function read(uint id) view public returns(uint, string memory, string memory){
    uint index = find(id);
    return (dataobj[index].id, dataobj[index].item, dataobj[index].label);
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

  function getcurrentsize() view public returns (uint){
    return dataobj.length;
  }


}
