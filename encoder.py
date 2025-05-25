#===========encoding-decoding============

from rich import print
import random
import string

# Constants for obfuscation length
ENCODE_PREFIX_LEN = 3
ENCODE_SUFFIX_LEN = 2
MIN_ENCODE_LEN = ENCODE_PREFIX_LEN + ENCODE_SUFFIX_LEN + 1


def obfuscate(word: str) -> str:
    """Obfuscate a word by rearranging and adding random characters."""
    prefix = ''.join(random.choices(string.ascii_letters, k=ENCODE_PREFIX_LEN))
    suffix = ''.join(random.choices(string.ascii_letters, k=ENCODE_SUFFIX_LEN))
    return prefix + word[1:] + word[0] + suffix


def deobfuscate(word: str) -> str:
    """Decode an obfuscated word back to its original form."""
    trimmed = word[ENCODE_PREFIX_LEN:-ENCODE_SUFFIX_LEN]
    return trimmed[-1] + trimmed[:-1]


def encode() -> None:
    """Encode a full message input by the user."""
    plain_text = input("Enter your message here: ")
    words = plain_text.split()
    encoded_words = []

    for word in words:
        if len(word) < 3:
            encoded_words.append(word[::-1])
        else:
            encoded_words.append(obfuscate(word))

    encoded_words.reverse()
    encoded_msg = ' '.join(encoded_words)
    print("[green]Here is your encoded version: [/green]" + encoded_msg)


def decode() -> None:
    """Decode an encoded message back to its original text."""
    try:
        encoded_text = input("Enter the message you want to decode: ")
        words = encoded_text.split()
        decoded_words = []

        for word in words:
            if len(word) < 3:
                decoded_words.append(word[::-1])
            else:
                decoded_words.append(deobfuscate(word))

        decoded_words.reverse()
        decoded_msg = ' '.join(decoded_words)
        print("[blue]Here is your decoded version: [/blue]" + decoded_msg)
    
    except Exception:
        print("[bold red] Please add a properly enoded message here[/bold red]")

def main() -> None:
    """Main loop to interact with the user."""
    while True:
        print("\n0 -> Encode\n1 -> Decode\nx -> Quit")
        action = input("Enter code here: ").strip().lower()

        if action == "0":
            encode()
        elif action == "1":
            decode()
        elif action == "x":
            break
        else:
            print("[bold red]INVALID CODE[/bold red]")


if __name__ == "__main__":
    main()

