from ctc import evm


token_address = '0x956F47F50A910163D8BF957Cf5846D573E7f87CA'


def test_fetch_token_total_supply():
    total_supply = evm.fetch_token_total_supply(token=token_address, block=13436621, normalize=False)
    assert total_supply == 542154246176449338629996405


def test_fetch_token_balance_of():
    address = '0x94b0a3d511b6ecdb17ebf877278ab030acb0a878'
    balance = evm.fetch_token_balance_of(address=address, token=token_address, block=13436621, normalize=False)
    assert balance == 137680097380114452997476874
