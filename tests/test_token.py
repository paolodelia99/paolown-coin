import pytest

from brownie import accounts, PaolownCoin

founder_address = '0x60502Fb7DdC4d3027ADF657d764606AA7ab26BB5'


@pytest.fixture
def token():
    return PaolownCoin.deploy(founder_address, {'from': accounts[0]})


def test_initial_state(token):
    assert token.totalSupply() == 100000
    assert token.name() == "Paolown Coin"
    assert token.symbol() == "PLW"
    assert token.get_max_supply() == 1000000

    assert token.balanceOf(founder_address) == 100000


def test_transfer(token):

    account_1 = accounts[1]

    assert token.balanceOf(founder_address) == 100000
    assert token.balanceOf(account_1) == 0

    tx = token.transfer(account_1, 10, {'from': founder_address})

    assert token.balanceOf(founder_address) == 99990
    assert token.balanceOf(account_1) == 10

    assert len(tx.events) == 1
    assert tx.events[0]['amount'] == 10


def test_allowances(token):
    account_1 = accounts[0]
    account_2 = accounts[1]

    assert token.allowance(account_2, account_1) == 0

    token.increaseAllowance(account_1, 10, {'from': account_2})

    assert token.allowance(account_2, account_1) == 10

    token.decreaseAllowance(account_1, 5, {'from': account_2})

    assert token.allowance(account_2, account_1) == 5


def test_transfer_from(token):
    spender = accounts[1]
    to = accounts[2]

    assert token.balanceOf(founder_address) == 100000
    assert token.balanceOf(spender) == 0

    tx1 = token.approve(spender, 10, {'from': founder_address})
    tx2 = token.transferFrom(founder_address, to, 10, {'from': spender})

    assert token.balanceOf(founder_address) == 99990
    assert token.balanceOf(to) == 10
    assert token.balanceOf(spender) == 0

    assert len(tx1.events) == 1
    assert tx1.events[0]['value'] == 10

    assert len(tx2.events) == 1
    assert tx2.events[0]['amount'] == 10


def test_minting(token):
    account = accounts[0]

    assert token.balanceOf(account) == 0

    token.mint(account, 10)

    assert token.balanceOf(account) == 10
    assert token.totalSupply() == 100010
