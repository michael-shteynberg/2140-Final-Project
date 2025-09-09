# Encryption Tool: Cryptographic Systems

A comprehensive encryption application implementing both symmetric and asymmetric cryptography with a user-friendly GUI.

## Overview

This system provides secure text encryption using industry-standard algorithms. It combines password-based symmetric encryption with RSA key pair generation, demonstrating fundamental cryptographic concepts through practical implementation.

## Key Technical Concepts

### Symmetric Encryption
The system uses Fernet encryption, built on AES in CBC mode with HMAC authentication. This provides fast, secure encryption where the same key encrypts and decrypts data. The implementation shows how modern applications protect data confidentiality while ensuring message integrity.

### Key Derivation Functions
PBKDF2 transforms user passwords into cryptographic keys through iterative hashing with salt. Using 480,000 iterations of SHA-256, the system resists brute-force attacks by making each password guess computationally expensive. This demonstrates how security systems protect against weak passwords.

### Asymmetric Cryptography
RSA key pair generation enables public-key cryptography where encryption and decryption use different keys. The public key can be shared openly while the private key remains secret. This forms the foundation of secure communications protocols like HTTPS and email encryption.

### Cryptographic Key Management
The system handles key serialization in PEM format with optional password protection for private keys. Keys are stored using PKCS8 standard formatting, demonstrating proper key lifecycle management from generation through secure storage.

### Security Usability
The Tkinter GUI makes cryptographic operations accessible to non-technical users. Mode switching between encryption and decryption with real-time feedback shows how security tools balance strong protection with user experience.

## Why This Matters

- **Foundation of Digital Security**: These algorithms protect everything from messaging apps to banking
- **Defense Against Attacks**: Multiple security layers resist various attack vectors
- **Practical Cryptography**: Bridges theoretical concepts with real-world implementation
- **Security Engineering**: Demonstrates proper use of cryptographic libraries
