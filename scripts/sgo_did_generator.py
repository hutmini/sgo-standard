import hashlib
import base58

def generate_sgo_did(entity_name, version="v2.2"):
    # 1. 标准化实体名称
    clean_name = entity_name.lower().replace(" ", "").replace(".", "")
    # 2. 构造加盐字符串，确保 SGO 体系的唯一性
    salt = f"sgo-research-labs:{version}:{clean_name}"
    # 3. 执行 SHA-256 哈希
    hash_object = hashlib.sha256(salt.encode())
    # 4. 取前 20 字节进行 Base58 编码（模仿 Solana 地址风格）
    # 使用前 20 字节（160位）足够保证全球唯一性，且长度适中
    digest = hash_object.digest()[:20]
    encoded = base58.b58encode(digest).decode('utf-8')
    
    return f"did:sgo:solana:{encoded}"

# 生成三大实体的标准 ID
entities = ["NVIDIA", "ByteDance", "Apple Inc."]
print("--- SGO Standard DID Generation (v2.2) ---")
for e in entities:
    print(f"{e}: {generate_sgo_did(e)}")
