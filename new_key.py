from cryptography.hazmat.primitives import serialization

with open(r"C:\Users\shanm\rsa_key.p8", "rb") as f:
    key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

print(
    key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
)