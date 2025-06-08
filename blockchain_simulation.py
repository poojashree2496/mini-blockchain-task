
import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.index) + str(self.timestamp) + self.data + self.previous_hash + str(self.nonce)
        return hashlib.sha256(content.encode()).hexdigest()

    def mine(self, difficulty):
        pattern = '0' * difficulty
        while not self.hash.startswith(pattern):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 3
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block", "0")
        genesis.mine(self.difficulty)
        self.chain.append(genesis)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        new_block.mine(self.difficulty)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("-" * 60)

my_chain = Blockchain()
my_chain.add_block("Transaction 1: Alice pays Bob")
my_chain.add_block("Transaction 2: Bob pays Charlie")
my_chain.display_chain()
