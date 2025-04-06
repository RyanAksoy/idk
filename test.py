import os
import random
import string

# Set folder and file path
folder_path = "C:/python"
file_path = os.path.join(folder_path, "compress_proof_1gb.txt")

# Create folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# File size settings
target_size_bytes = 1 * 1_073_741_824  # 1GB
chunk_size = 10_000_000  # 10MB per chunk
chars = string.ascii_letters + string.digits + string.punctuation

print("Generating 1GB compress-proof file...")

with open(file_path, "w", buffering=1_048_576) as f:
    written = 0
    while written < target_size_bytes:
        chunk = ''.join(random.choices(chars, k=chunk_size))
        f.write(chunk)
        written += len(chunk)
        print(f"Written: {written / (1024 ** 2):.2f} MB", end="\r")

print(f"\n✅ File created: {file_path}")
