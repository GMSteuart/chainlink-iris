import pytest
from brownie import (
    config,
    network,
    accounts,
    MockV3Aggregator,
    VRFCoordinatorMock,
    LinkToken,
    Contract,
    MockOracle,
)
import os


@pytest.fixture
def chainlink_fee():
    return 1000000000000000000


@pytest.fixture
def expiry_time():
    return 300


@pytest.fixture
def seed():
    return 777


@pytest.fixture
def data():
    return 100


@pytest.fixture
def deployer(accounts):
    return accounts[0]


@pytest.fixture
def node_account():
    return accounts[1]


@pytest.fixture
def dev(accounts):
    return accounts[2]


@pytest.fixture
def user(accounts):
    return accounts[3]


# @pytest.fixture
# def get_eth_usd_price_feed_address():
#     if network.show_active() == "development":
#         mock_price_feed = MockV3Aggregator.deploy(18, 2000, {"from": accounts[0]})
#         return mock_price_feed.address
#     if network.show_active() in config["networks"]:
#         return config["networks"][network.show_active()]["eth_usd_price_feed"]
#     else:
#         pytest.skip("Invalid network specified ")
#         return


# @pytest.fixture(scope="module")
# def get_account():
#     if (
#         network.show_active() == "development"
#         or network.show_active() == "mainnet-fork"
#     ):
#         return accounts[0]
#     if network.show_active() in config["networks"]:
#         dev_account = accounts.add(os.getenv(config["wallets"]["from_key"]))
#         return dev_account
#     else:
#         pytest.skip("Invalid network/wallet specified ")


@pytest.fixture
def link_token(pm, deployer):
    if network.show_active() == "development" or "fork" in network.show_active():
        # link = pm("alphachainio/chainlink-contracts@1.1.2").LinkToken
        yield LinkToken.deploy({"from": deployer})

    if network.show_active() in config["networks"]:
        yield Contract.from_abi(
            "link_token",
            config["networks"][network.show_active()]["link_token"],
            LinkToken.abi,
        )

    else:
        pytest.skip("Invalid network/link token specified ")


@pytest.fixture
def vrf_coordinator(pm, deployer, link_token):
    if network.show_active() == "development" or "fork" in network.show_active():
        yield VRFCoordinatorMock.deploy(link_token, {"from": deployer})

    if network.show_active() in config["networks"]:
        yield Contract.from_abi(
            "vrf_coordinator",
            config["networks"][network.show_active()]["vrf_coordinator"],
            VRFCoordinatorMock.abi,
        )

    else:
        pytest.skip("Invalid network specified")


@pytest.fixture
def keyhash():
    if network.show_active() == "development" or "fork" in network.show_active():
        return 0
    if network.show_active() in config["networks"]:
        return config["networks"][network.show_active()]["keyhash"]
    else:
        pytest.skip("Invalid network/link token specified ")


@pytest.fixture
def job_id():
    if network.show_active() == "development" or "fork" in network.show_active():
        return 0
    if network.show_active() in config["networks"]:
        return config["networks"][network.show_active()]["jobId"]
    else:
        pytest.skip("Invalid network/link token specified")


@pytest.fixture
def oracle(deployer, link_token):
    if network.show_active() == "development" or "fork" in network.show_active():
        yield MockOracle.deploy(link_token, {"from": deployer})

    if network.show_active() in config["networks"]:
        yield Contract.from_abi(
            "mock_oracle",
            config["networks"][network.show_active()]["oracle"],
            MockOracle.abi,
        )

    else:
        pytest.skip("Invalid network specified")
