#!/usr/bin/python3
import os
from brownie import (
    project,
    interface,
    # LinkToken,
    # Oracle,
    # VRFCoordinator,
    VrfNftGenerator,
    accounts,
    network,
    config,
)


def main():
    # dev = accounts.add(os.getenv(config["wallets"]["from_key"]))

    print(f"Network: {network.show_active()}")
    # pm("alphachainio/chainlink-contracts@1.1.2").LinkToken

    p = project.load("alphachainio/chainlink-contracts@1.1.2")
    print(project.get_loaded_projects())

    print(sources.get_contract_list())
    # contracts = config["networks"][network.show_active()]
    # print(contracts)
    # return VrfNftGenerator.deploy(
    #     contracts["keyhash"],
    #     contracts["vrf_coordinator"],
    #     contracts["link_token"],
    #     {"from": dev},
    # )
