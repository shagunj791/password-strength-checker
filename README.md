# password-strength-checker
A simple tool to check if a password is Weak, Medium, or Strong
# Password Strength Checker

Simple password strength checker (CLI + optional Streamlit UI).  
Checks length, use of uppercase/lowercase, digits, special chars and estimates entropy.

## Features
- CLI function `check_password_strength(password)` returns label, entropy, suggestions
- Optional Streamlit demo (`app_streamlit.py`)
- Tests with pytest

## Quick start

1. Create virtual env (recommended)
```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
