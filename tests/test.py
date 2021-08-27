import unittest
import base64
from hashlib import sha3_256

import onioncompressor

class TestCompressor(unittest.TestCase):

    def test_compress(self):
        onion = "duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"
        orig = onion
        expected_compress = b'\x1d\x04\xa1\xd0J3\x8cnj\xe9p\xbf\xab\xeeI\x04\x9dg\x02%\t\x84\xca\x95\x0c\x01g?N\xc04\xad'

        onion = onioncompressor.compress(onion)
        checksum = sha3_256(b".onion checksum" + onion + int(3).to_bytes(1, 'big')).digest()[:2]
        uncompressed = onion + checksum + int(3).to_bytes(1, 'big')
        self.assertEqual(onion, expected_compress)
        self.assertEqual(base64.b32encode(uncompressed), orig[:-6].upper().encode('utf-8'))
        assert len(onion) == 32

    def test_decompress(self):
        compressed = b'\x1d\x04\xa1\xd0J3\x8cnj\xe9p\xbf\xab\xeeI\x04\x9dg\x02%\t\x84\xca\x95\x0c\x01g?N\xc04\xad'
        onion = "duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"
        self.assertEqual(onioncompressor.decompress(compressed), onion)

unittest.main()