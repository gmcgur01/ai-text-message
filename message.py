import sys
import os
from dotenv import load_dotenv

def main():
    assert len(sys.argv) == 2
    load_dotenv()
    API_KEY = os.environ["API_KEY"]

    print(sys.argv[1])

if __name__ == "__main__":
    main()