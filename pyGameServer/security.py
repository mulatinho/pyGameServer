# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Author: Alexandre Mulatinho <alex@mulatinho.net>

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID

class Security(object):
    """ Security class for dealing with cryptographic and security issues """
    
    _private_key = None
    
#    def __init__(self):
    
    def pk_new_key(self, password=None):
        """ Generate a new private key """
        self._private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

    def pk_save_key(self, key_path=None):
        """ Save a private key into a file """
        pem = self._private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        if key_path == None:
            key_path = "../data/privkey.pem"
        
        with open(key_path, "wb") as pem_out:
            pem_out.write(pem)
        