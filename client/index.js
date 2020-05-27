import Web3 from 'web3';
import Dataset from '../build/contracts/Dataset.json';

let web3;
let dataset;

const initWeb3 = () => {
  return new Promise((resolve, reject) => {
    // if(typeof window.ethereum !== 'undefined') {
    //   const web3 = new Web3(window.ethereum);
    //   window.ethereum.enable()
    //     .then(() => {
    //       resolve(
    //         new Web3(window.ethereum)
    //       );
    //     })
    //     .catch(e => {
    //       reject(e);
    //     });
    //   return;
    // }
    // if(typeof window.web3 !== 'undefined') {
    //   return resolve(
    //     new Web3(window.web3.currentProvider)
    //   );
    // }
    resolve(new Web3('http://localhost:9545'));
  });
};

const initContract = () => {
  const deploymentKey = Object.keys(Dataset.networks)[0];
  return new web3.eth.Contract(
    Dataset.abi,
    Dataset
      .networks[deploymentKey]
      .address
  );
};

const initApp = () => {
  const $created = document.getElementById('create');
  const $createResult = document.getElementById('create-result');
  const $read = document.getElementById('read');
  const $readResult = document.getElementById('read-result');
  let accounts = [];

  web3.eth.getAccounts()
  .then(_accounts => {
    accounts = _accounts;
  });


  $created.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = e.target.elements[0].value;
    let items = name.split(";")
    console.log(items[0]+" "+items[1])
    dataset.methods.insert(items[0],items[1]).send({"from": accounts[0], "gas": 300000})
    .then(result => {
      $createResult.innerHTML = `New dataitem ${name} successfully inserted`;
    })
    .catch(_e => {
      $createResult.innerHTML = `Ooops... there was an error while trying to insert a new data item...`;
    });
  });

  $read.addEventListener('submit', (e) => {
    e.preventDefault();
//code added
      dataset.methods.getcurrentsize().call()
      .then(size => {
        //str = "";
        //$readResult.innerHTML = `size: ${size}`;
        let str2;

        for (let i=1;i<=size;i++){
          dataset.methods.read(i).call()
          .then(result => {
            str2 = `${result[0]},${result[1]},${result[2]}`;
            //$readResult.innerHTML = str;
            $readResult.innerHTML += str2+'</br>';
          })
          .catch(_e => {
            $readResult.innerHTML = `Ooops... there was an error while trying to read data item`;
          });
          //str = str+"index: "+i+"\n";
        }
        console.log(str2);
        $readResult.innerHTML = "";
        // let i = 0;
        // //for (i=0;i<size;i++){
        //   dataset.methods.read(i).call()
        //   .then(result => {
        //     str = `${result[0]}, ${result[1]}, ${result[2]}\n`;
        //     $readResult.innerHTML = str;
        //   })
        //   .catch(_e => {
        //   $readResult.innerHTML = `Ooops... there was an error while trying to read data item`;
        // });
      //}
        //$readResult.innerHTML = str;
    })
    //new code ends

    .catch(_e => {
      $readResult.innerHTML = `Ooops... there was an error while trying to read dataset length`;
    });
  });
};

  document.addEventListener('DOMContentLoaded', () => {
    initWeb3()
      .then(_web3 => {
        web3 = _web3;
        dataset = initContract();
        initApp();
      })
      .catch(e => console.log(e.message));
  });
