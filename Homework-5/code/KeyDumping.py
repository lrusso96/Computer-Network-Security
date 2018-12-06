from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import *

# private key management
class PrivateDumping:
    def __init__(self):
        self.pkcs_format = PrivateFormat.TraditionalOpenSSL
        self.encoding = Encoding.PEM
        self.encryption = NoEncryption()

    def set_key(self, key):
        self.key = key

    def set_encoding(self, encoding):
        if encoding == "pem":
            self.encoding = Encoding.PEM
        elif encoding == "der":
            self.encoding = Encoding.DER

    def set_encryption(self, encryption):
        self.encryption = encryption

    def set_pkcs(self, pkcs):
        if pkcs == 1:
            self.pkcs_format = PrivateFormat.TraditionalOpenSSL
        elif pkcs == 8:
            self.pkcs_format = PrivateFormat.PKCS8

    def store_key(self, filename):            
        serialized = self.key.private_bytes(
            encoding = self.encoding,
            format = self.pkcs_format,
            encryption_algorithm = self.encryption
        )
        with open(filename, 'wb') as fout:
            fout.write(serialized)       

    def load_key(self, filename):
        with open(filename, 'rb') as fin:
            lines = fin.read()
        if self.encoding == Encoding.PEM:
            private_key = load_pem_private_key(lines, None, default_backend())
        elif self.encoding == Encoding.DER:
            private_key = load_der_private_key(lines, None, default_backend())
        self.private_key = private_key
# private key management
class PublicDumping:
    def __init__(self):
        self.pk_format = PublicFormat.SubjectPublicKeyInfo
        self.encoding = Encoding.PEM

    def set_key(self, key):
        self.key = key

    def set_encoding(self, encoding):
        if encoding == "pem":
            self.encoding = Encoding.PEM
        elif encoding == "der":
            self.encoding = Encoding.DER
        elif encoding == "ssh":
            self.encoding = Encoding.OpenSSH    

    def set_format(self, pk_format):
        if pk_format == "default":
            self.pk_format = PublicFormat.SubjectPublicKeyInfo
        elif pk_format == "OpenSSH":
            self.pk_format = PublicFormat.OpenSSH
        elif pk_format == "pkcs1":
            self.pk_format = PublicFormat.PKCS1

    def store_key(self, filename):            
        serialized = self.key.public_bytes(
            encoding = self.encoding,
            format = self.pk_format
        )
        with open(filename, 'wb') as fout:
            fout.write(serialized)       

    def load_key(self, filename):
        with open(filename, 'rb') as fin:
            lines = fin.read()
        if self.encoding == Encoding.PEM:
            public_key = load_pem_public_key(lines, default_backend())
        elif self.encoding == Encoding.DER:
            public_key = load_der_public_key(lines, default_backend())
        elif self.encoding == Encoding.OpenSSH:
            public_key = load_ssh_public_key(lines, default_backend())
        self.public_key = public_key

def gen_private_key(bits = 2048):
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=bits, backend=default_backend()
    )
    return private_key

def test_private():
    pk = gen_private_key()
    pd = PrivateDumping()

    # pem
    filename = 'privkey.pem'
    pd.set_key(pk)
    pd.store_key(filename)

    # der 
    pd.set_encoding("der")
    filename = 'privkey.der'
    pd.store_key(filename)


def test_public():
    pk = gen_private_key()
    pk = pk.public_key()
    pd = PublicDumping()

    # pem
    filename = 'pubkey.pem'
    pd.set_key(pk)
    pd.store_key(filename)

    # der 
    pd.set_encoding("der")
    filename = 'pubkey.der'
    pd.store_key(filename)

    #pub
    pd.set_encoding("ssh")
    pd.set_format("OpenSSH")
    filename = 'pubkey.pub'
    pd.store_key(filename)
