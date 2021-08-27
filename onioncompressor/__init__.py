"""
OnionCompressor: (un)compress v3 tor onion addresses by stripping checksum
Copyright (C) 2021 Kevin Froman - VoidNetwork LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from base64 import b32decode, b32encode
from hashlib import sha3_256


def compress(onion: str) -> bytes:
    return b32decode(onion.upper()[:-6])[:-3]


def decompress(onion: bytes) -> str:
    onion_version_byte = int(3).to_bytes(1, 'big')
    checksum = sha3_256(b'.onion checksum' +
                        onion +
                        onion_version_byte).digest()[:2]
    return b32encode(
        onion +
        checksum +
        onion_version_byte).decode('utf-8').lower() + '.onion'
