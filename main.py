from typing import List
from Wallet import import_wallet, deploy_wallet
from storage import read_config
import asyncio


async def main() -> None:
    secrets: List[str] = read_config("mnemonic")
    if not secrets:
        print("[ERR] You must save mnemonic before you used")
    wallet = import_wallet(secrets)
    await deploy_wallet(wallet)


if __name__ == "__main__":
    asyncio.run(main())
