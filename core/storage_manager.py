import uuid
import base64
import json
import random
import time

def random_uuid():
    return str(uuid.uuid4())

def random_base64(length=22):
    return base64.urlsafe_b64encode(random.randbytes(length)).decode('utf-8').rstrip('=')

def generate_mirror_storage():
    # Example schema based on extracted sample
    storage = {
        '_stripe_mid': random_uuid(),
        '_stripe_sid': random_uuid(),
        'device_id': random_uuid(),
        'machine_id': random_uuid(),
        'persist:root': json.dumps({
            'pcid': random_uuid(),
            'pcidDate': int(time.time() * 1000),
            'group': 'B',
            'dbsaved': 'false',
            'abTestUuid': 'g_' + random_uuid(),
        }),
        '_ga': random_base64(),
        '_cl': random_base64(),
        # Add more keys as needed based on sample
    }
    return storage

def generate_fingerprint_storage():
    # Legacy stub for compatibility
    return generate_mirror_storage()

def mirror_sample():
    # Generate a known-good legacy storage for test
    return {
        '_stripe_mid': 'e56412a6-f65b-4b08-9627-ae8348971a72',
        '_stripe_sid': '8362d311-b1e2-4083-a93c-ada7ecc4e9e6',
        'device_id': '7f3e78bf-d21f-44c2-aad7-789339dc83d7',
        'machine_id': '99d5fac0-09d0-4cd0-903c-25ae5ec176bf',
        'persist:root': json.dumps({
            'pcid': '0d923308-81bb-ae17-fc96-8bd61c6359fa',
            'pcidDate': 1768485049438,
            'group': 'B',
            'dbsaved': 'false',
            'abTestUuid': 'g_79869585-3eec-459d-800a-4f6c97d61f4f',
        }),
        '_ga': 'U1bXs5vQhGN6J0riG34uRWRiXneeRkYrY5gU',
        '_cl': 'vyIVr5uALslLoLCe1EJxblnJi2Rn',
    }

if __name__ == "__main__":
    print(json.dumps(generate_mirror_storage(), indent=2))
