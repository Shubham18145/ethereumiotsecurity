const Dataset = artifacts.require("Dataset");

module.exports = function(deployer) {
  deployer.deploy(Dataset);
};
