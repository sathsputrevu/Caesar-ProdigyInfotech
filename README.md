# Caesar Cipher Program

## Overview
This is a **Python-based terminal application** that implements the **Caesar Cipher** for text encryption and decryption. The application allows users to easily shift letters in a message by a specified number of positions, making it a simple yet effective cryptography tool. 

This project was developed as the first task at **Prodigy InforTech** with a focus on creating a clean and interactive terminal interface that provides clear feedback to the user.

## Features
- **Encryption** and **Decryption** of text using Caesar Cipher.
- **Customizable shift value** for the cipher.
- **Case sensitivity option**: choose whether to keep the case of the original message or convert it.
- **Colorful and intuitive terminal interface** using `colorama`.
- Error handling for invalid input (e.g., non-numeric shift values).

## Prerequisites
Make sure you have Python 3.x installed. Additionally, you'll need to install the following library:
- [Colorama](https://pypi.org/project/colorama/)

You can install `colorama` by running the following command:

```bash
pip install colorama
```

## Usage
To run the program, simply execute the Python file:

```bash
python caesar_cipher.py
```

### Options:
1. **Encrypt a Message**: You will be prompted to enter your message, the shift value, and whether the case should be preserved.
2. **Decrypt a Message**: Same process as encryption but in reverse.
3. **Exit**: You can exit the application at any time by choosing this option.

### Example Workflow:
```bash
========== Welcome to the Caesar Cipher Program ==========
> Encrypt and Decrypt Texts Securely


----- Options -----
[1] Encrypt
[2] Decrypt
[3] Exit

> Choose an option (1, 2, or 3): 1

Enter your message: HELLO
Enter the shift value (e.g., 4): 3
Case sensitive (yes/no)? no

✔ Encrypted message: khoor
```

## File Structure
```
.
├── caesar_cipher.py       # Main script implementing the Caesar Cipher program
├── README.md              # Project documentation (this file)
```

## Contributing
If you would like to contribute to this project, feel free to open a pull request or submit issues. All contributions are welcome!

## License
This project is licensed under the MIT License 

## Acknowledgments
This project was completed as part of my work with **Prodigy InforTech**. Special thanks to the team for the opportunity to grow and learn through this task.
