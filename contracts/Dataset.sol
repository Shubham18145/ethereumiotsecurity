pragma solidity ^0.5.0;
//pragma experimental ABIEncoderV2;

contract Dataset {
  struct Data {
    uint id;
    string item; //includes features followed by label
  }
  Data[] public dataobj;
  uint public nextId = 1;

  function insert(string memory data_item) public {
    dataobj.push(Data(nextId, data_item));
    nextId++;
  }


  function read(uint id) view public returns(uint, string memory){
    uint index = find(id);
    return (dataobj[index].id, dataobj[index].item);
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
