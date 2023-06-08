from bech32 import *
HRP = "one"
def convert_eth_to_one(address: str, useHRP: str = HRP) -> str:
    address_remove_0x = bytearray.fromhex(address.replace("0x", ""))
    addrBz = convertbits(address_remove_0x, 8, 5)
    if not addrBz:
        return "error", "ERROR: Could not convert byte Buffer to 5-bit Buffer"
    return "success", bech32_encode(useHRP, addrBz)


address = "0x11c4e687b865c1e8e17437748ab3d1faed7444ff"

#b = convert_eth_to_one(address)

print(convert_eth_to_one(address)[1])