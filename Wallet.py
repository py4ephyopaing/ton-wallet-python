from tonsdk.contract.wallet import WalletContract, Wallets, WalletVersionEnum
import requests
import asyncio
from pathlib import Path
from ton import TonlibClient


def create_wallet() -> tuple:
    mnemonic, pub_k, pri_k, wallet = Wallets.create(
        version=WalletVersionEnum.v4r2, workchain=0
    )
    return mnemonic, pub_k, pri_k, wallet


def import_wallet(mnemonic: list) -> WalletContract:
    mnemonic, pub_k, pri_k, wallet = Wallets.from_mnemonics(mnemonic)

    return wallet


async def get_client():
    ton_config = requests.get('https://ton.org/global.config.json').json()
    
    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=0, config=ton_config, keystore=keystore_dir)
    
    return client


async def deploy_wallet(wallet: WalletContract):
    boc = wallet.create_init_external_message()["message"].to_boc(False)
    client = await get_client()

    await client.send_boc(boc)
