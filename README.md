# OnionCompressor

Per v3 Tor onion spec: https://github.com/torproject/torspec/blob/main/rend-spec-v3.txt

This small module 'compresses' v3 onions by decoding the base32, removing the non-security related checksum, and removing the version number.

The resulting bytes is actually a valid ed25519 public key, but you probably shouldn't use it for anything but normal Tor onion uses.

It can also uncompress the bytes back to the human friendly format.

The compressed result is about 50% smaller.

# Usage

`compressed: bytes = onioncompressor.compress('duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion')`

`uncompressed: str: = onioncompressor.decompress(compressed)`
