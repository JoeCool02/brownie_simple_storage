from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    # go take the index that's one less than the length
    # ABI - brownie knows ABI in build/contracts
    # Address - brownie knows address in build/deployments
    print(simple_storage.retrieve())


def main():
    read_contract()
