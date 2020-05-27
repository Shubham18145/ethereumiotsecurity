const Dataset = artifacts.require('Dataset');

contract('Dataset', () => {
  let dataset = null;
  before(async () => {
    dataset = await Dataset.deployed();
  });

  it('Should insert a new data item', async () => {
    await dataset.insert('Hello',1);
    const user = await dataset.read(1);
    assert(user[0].toNumber() === 1);
    assert(user[1] === 'Hello');
    assert(user[2].toNumber() === 1);
  });

});
