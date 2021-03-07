# Paolown Coin

Here I made a smart contract in Vyper and brownie for my own coin.

**Disclaimer**: the contract hasn't been audited, do not use it production. I made it just for fun and learning how to write smart contract

# Quick start

First of all, after you've set up a virtual environment, install the required packages through

    pip install -r requirements.txt

For compiling the contract run:

    brownie compile

For running the tests run:

    brownie test

If you also want to know the coverage then run:

    brownie test --coverage

# Resources

- [Vyper Interfaces](https://github.com/vyperlang/vyper/blob/master/vyper/interfaces/ERC20.py)
- [ERC20 standard](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md)
- [ERC20 openzeppelin implementation](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/9b3710465583284b8c4c5d2245749246bb2e0094/contracts/token/ERC20/ERC20.sol)
- [ERC20 API: An Attack Vector on Approve/TransferFrom Methods](https://docs.google.com/document/d/1YLPtQxZu1UAvO9cZ1O2RPXBbT0mooh4DYKjA_jp-RLM/edit)
- [First blodio token implementaion](https://github.com/Firstbloodio/token/blob/master/smart_contract/FirstBloodToken.sol)

# Todos

- [refine tests](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/9b3710465583284b8c4c5d2245749246bb2e0094/test/token/ERC20/ERC20.test.js)

# Author

Paolo D'Elia

# License

MIT

