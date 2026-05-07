import random
import string

def generate_credentials(filename, count=3000):
    users = ["admin", "user", "guest", "test", "root", "info", "webmaster", "sales", "support", "john", "jane"]
    with open(filename, "w") as f:
        for i in range(count):
            user = f"user{i}" if i > 100 else random.choice(users) + str(i)
            # Mix of common passwords and random ones
            if i % 10 == 0:
                password = "password123"
            elif i % 5 == 0:
                password = "admin"
            else:
                password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
            f.write(f"{user}:{password}\n")

def generate_coupons(filename, count=1000):
    prefixes = ["SAVE", "DISCOUNT", "OFFER", "PROMO", "WINTER", "SUMMER", "BFRIDAY", "CYBER"]
    with open(filename, "w") as f:
        for i in range(count):
            prefix = random.choice(prefixes)
            code = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
            f.write(f"{prefix}-{code}-{i}\n")

def generate_valid_credentials(source_filename, dest_filename, count=10):
    with open(source_filename, "r") as f_in, open(dest_filename, "w") as f_out:
        for _ in range(count):
            line = f_in.readline()
            if not line:
                break
            f_out.write(line)

if __name__ == "__main__":
    print("Generating credentials.txt (3050 lines)...")
    generate_credentials("credentials.txt", 3050)
    print("Generating coupons.txt (1050 lines)...")
    generate_coupons("coupons.txt", 1050)
    print("Generating valid_credentials.txt (10 lines from credentials.txt)...")
    generate_valid_credentials("credentials.txt", "valid_credentials.txt", 10)
    print("Wordlists generated successfully.")
