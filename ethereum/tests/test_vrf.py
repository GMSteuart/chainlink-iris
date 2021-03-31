import pytest
import time
from brownie import network, VrfNftGenerator, convert


def test_can_request_random_number(
    deployer,
    vrf_coordinator,
    keyhash,
    link_token,
    chainlink_fee,
    seed,
):
    # Arrange
    vrf_consumer = VrfNftGenerator.deploy(
        keyhash,
        vrf_coordinator,
        link_token,
        {"from": deployer},
    )

    link_token.transfer(vrf_consumer, chainlink_fee * 3, {"from": deployer})

    # Act
    requestId = vrf_consumer.getRandomNumber.call(seed, {"from": deployer})
    assert isinstance(requestId, convert.datatypes.HexString)


def test_returns_random_number_local(
    deployer, vrf_coordinator, keyhash, link_token, chainlink_fee, seed
):
    # Arrange
    if network.show_active() not in ["development"] or "fork" in network.show_active():
        pytest.skip("Only for local testing")
    vrf_consumer = VrfNftGenerator.deploy(
        keyhash, vrf_coordinator, link_token, {"from": deployer}
    )
    link_token.transfer(vrf_consumer, chainlink_fee * 3, {"from": deployer})

    # Act
    transaction_receipt = vrf_consumer.getRandomNumber(seed, {"from": deployer})
    requestId = vrf_consumer.getRandomNumber.call(seed, {"from": deployer})
    assert isinstance(transaction_receipt.txid, str)

    vrf_coordinator.callBackWithRandomness(
        requestId, 777, vrf_consumer, {"from": deployer}
    )

    # Assert
    assert vrf_consumer.randomResult() > 0
    assert isinstance(vrf_consumer.randomResult(), int)


# def test_returns_random_number_testnet(deployer, vrf_coordinator, keyhash,
#                                        link_token, chainlink_fee, seed):
#     # Arrange
#     if network.show_active() not in ['kovan', 'rinkeby']:
#         pytest.skip('Only for testnet testing')
#     vrf_consumer = VrfNftGenerator.deploy(
#         keyhash, vrf_coordinator, link_token, {'from': deployer})
#     link_token.transfer(vrf_consumer,
#                             chainlink_fee * 3, {'from': deployer})
#     # Act
#     transaction_receipt = vrf_consumer.getRandomNumber(
#         seed, {'from': deployer})
#     assert isinstance(transaction_receipt.txid, str)
#     time.sleep(30)
#     # Assert
#     assert vrf_consumer.randomResult() > 0
#     assert isinstance(vrf_consumer.randomResult(), int)
