"""Run function for user to access this protocol."""

from analyzers.key_analyzer import KeyAnalyzer
from cube_encryption.encryption import Encryption


# Ask the user for a message to encrypt.
message = input("Please type in the message you want to encrypt.\n")
# Ask the user for a desired cube size.
cube_side_length = int(input("Please type in the desired cube side length.\n"))
# Initialize the protocol.
protocol = Encryption(message=message, cube_side_length=cube_side_length)
# Ask the user for a desired key length.
key_length = int(input("Please type in the desired key length.\n"))
# Generate the desired key.
key = protocol.generate_random_key(length=key_length)
# Print the random generated key.
print("\nThe random generated key is: ")
for each_key in key:
    print(f"The move is: {each_key.move}, "
          f"the angle is: {each_key.angle} "
          f"and the index is: {each_key.index}")

# Print a separator.
print("\n")

key = KeyAnalyzer(key=key).analyze()
# Print the random generated key.
print(f"\nThe reduced key has length {len(key)}, and it is: ")
for each_key in key:
    print(f"The move is: {each_key.move}, "
          f"the angle is: {each_key.angle} "
          f"and the index is: {each_key.index}")

# Print a separator.
print("\n")

# Show user the current un-encrypted binary.
print(f"The plain-text in binary padded is: {protocol.get_pad_binary()}\n")
# Encrypt the message based on the given key.
protocol.encrypt(key=key)
# Show user the current encrypted binary.
print(f"The cipher-text in binary is: {protocol.get_pad_binary()}\n")
# Decrypt the message.
protocol.decrypt()
# Show the plain-text recovered.
print(protocol.get_un_pad_string())
