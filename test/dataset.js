const Dataset = artifacts.require('Dataset');

contract('Dataset', () => {
  let dataset = null;
  before(async () => {
    dataset = await Dataset.deployed();
  });

  it('Should insert a new data item', async () => {
    await dataset.insert('Category1');
    const user = await dataset.read(1);
    assert(user[0].toNumber() === 1);
    assert(user[1] === 'Category1');
  });

  it('Should destroy an existing data item', async () => {
    await dataset.destroy(1);
    try {
      const user = await dataset.read(1);
    } catch(e) {
      assert(e.message.includes('Data item does not exist!'));
      return;
    }
    assert(false);
  });

  it('Should NOT destroy a non-existing user', async () => {
    try {
      await dataset.destroy(10);
    } catch(e) {
      assert(e.message.includes('Data item does not exist'));
      return;
    }
    assert(false);
  });
});
