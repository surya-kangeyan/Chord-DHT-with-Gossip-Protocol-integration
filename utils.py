import hashlib
import grpc
from proto import chord_pb2_grpc
import json
import argparse


def sha1_hash(key, m):
    """
    Function to hash the key using sha1 and return the hash value truncated to m bits
    Args:
        key: Key to be hashed
        m: Number of bits to truncate the hash value
    Returns:
        Hash value truncated to m bits
    """
    return int(hashlib.sha1(str(key).encode()).hexdigest(), 16) % (2**m)


def create_stub(ip, port):
    """
    Helper method to create and return a gRPC stub.
    Uses a context manager to ensure the channel is closed after use.
    """
    channel = grpc.insecure_channel(f'{ip}:{port}')
    return chord_pb2_grpc.ChordServiceStub(channel), channel


def get_args():
    parser = argparse.ArgumentParser(description="Chord Node")
    parser.add_argument("--ip", type=str, help="IP address of the node")
    parser.add_argument("--port", type=int, help="Port number of the node")
    parser.add_argument(
        "--m", type=int, help="Number of bits in the hash space")
    parser.add_argument("--bootstrap_ip", type=str,
                        help="IP address of the bootstrap node", required=False)
    parser.add_argument("--bootstrap_port", type=int,
                        help="Port number of the bootstrap node", required=False)
    return parser.parse_args()
