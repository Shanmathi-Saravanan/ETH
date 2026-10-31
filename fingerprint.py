import snowflake.connector
from cryptography.hazmat.primitives import serialization

with open(r"C:\Users\shanm\rsa_key.p8", "rb") as f:
    p_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

print("Connecting...")

conn = snowflake.connector.connect(
    account="JNSMHVJ-VO98306",
    user="SHANMATHI",
    private_key=pkb,
    login_timeout=15,
    network_timeout=15,
)

print("CONNECTED")
