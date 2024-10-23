import os
import secrets

# Generate a secure secret key
secret_key = secrets.token_hex(32)

# Define the path to the .env file
env_file = os.path.join(os.path.dirname(__file__), '.env')

# Check if the .env file exists
if os.path.exists(env_file):
    with open(env_file, 'r') as file:
        env_data = file.readlines()

    # Update or add the SECRET_KEY in the .env file
    with open(env_file, 'w') as file:
        secret_key_set = False
        for line in env_data:
            if line.startswith('SECRET_KEY'):
                file.write(f'SECRET_KEY={secret_key}\n')
                secret_key_set = True
            else:
                file.write(line)

        if not secret_key_set:
            file.write(f'SECRET_KEY={secret_key}\n')
else:
    # Create the .env file if it doesn't exist
    with open(env_file, 'w') as file:
        file.write(f'SECRET_KEY={secret_key}\n')

print(f"Secret key generated and saved to {env_file}")