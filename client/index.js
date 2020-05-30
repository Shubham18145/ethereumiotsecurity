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
var hello = "";



const initApp = () => {
  const $created = document.getElementById('create');
  const $createResult = document.getElementById('create-result');
  const $read = document.getElementById('read');
  const $readResult = document.getElementById('read-result');
  var copy_result = document.getElementById('read-result');
  let accounts = [];

  web3.eth.getAccounts()
  .then(_accounts => {
    accounts = _accounts;
  });


  $created.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = e.target.elements[0].value;
    let items = name
    console.log(items)
    dataset.methods.insert(items).send({"from": accounts[0], "gas": 300000})
    .then(result => {
      $createResult.innerHTML = `New dataitem ${name} successfully inserted`;
    })
    .catch(_e => {
      $createResult.innerHTML = `Ooops... there was an error while trying to insert a new data item...`;
    });
  });

  $("#read_clear").click(function (event) {
    console.log(hello);
    $readResult.innerHTML = "";
  });

  $("#copy_text").click(function (event) {
    /* Get the text field */
    var brRegex = /<br\s*[\/]?>/gi;

    var $temp = $("<textarea>");
    $("#body2").append($temp);
    $temp.val($("#read-result").html().replace(brRegex, "\r\n")).select();
    console.log($temp.val());
    document.execCommand("copy");
    $temp.remove();
    console.log("copied_content");
    /* Alert the copied text */
    alert("Copied the text!");
  });

  $("#read").click(function (event) {
    console.log("clicked on read button");
    let file_data = ""; 
      dataset.methods.getcurrentsize().call()
      .then(size => {
        //str = "";
        //$readResult.innerHTML = `size: ${size}`;
        var str2;
        for (let i=1;i<=size;i++){
          dataset.methods.read(i).call()
          .then(result => {
            str2 = `${result[0]}:${result[1]}`;
            file_data = `${result[1]}`;

            $readResult.innerHTML += str2+'</br>';
          })
          .catch(_e => {
            $readResult.innerHTML = `Ooops... there was an error while trying to read data item`;
          });

        }
        $readResult.innerHTML = "";
    })

    .catch(_e => {
      $readResult.innerHTML = `Ooops... there was an error while trying to read dataset length`;
    });

    ////////////////////////////////////////////////////////////////////////////////
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
