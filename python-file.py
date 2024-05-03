
import datetime
import os

def main():
    print(f"Current date and time: {datetime.datetime.now()}")

if __name__ == "__main__":
    main()
    print(os.getenv('PG_USER'))
