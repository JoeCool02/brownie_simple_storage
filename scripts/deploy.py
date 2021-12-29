from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    print("Account:", account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print("Stored Value:", stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print("Updated Stored Value:", updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# account = accounts.load("freecodecamp-account")
# print(account)
# account = accounts.add(config["wallets"]["from_key"])
# print(account)


def main():
    deploy_simple_storage()
