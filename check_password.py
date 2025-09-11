#!/usr/bin/env python3
"""
Password strength checker
- provides a label (Very weak -> Very strong)
- estimates entropy (bits)
- returns suggestions to improve
"""

import re
import math
import argparse
import sys

def charset_size(password):
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    size = 0
    if has_lower: size += 26
    if has_upper: size += 26
    if has_digit: size += 10
    if has_special: size += 32  # rough approximation for special chars
    return size, has_lower, has_upper, has_digit, has_special

def estimate_entropy(password):
    size, *_ = charset_size(password)
    if size <= 0:
        return 0.0
    return len(password) * math.log2(size)

def check_password_strength(password):
    length = len(password)
    size, has_lower, has_upper, has_digit, has_special = charset_size(password)
    entropy = estimate_entropy(password)

    # scoring (0-5)
    points = 0
    if length >= 12:
        points += 2
    elif length >= 8:
        points += 1

    categories = sum([has_lower, has_upper, has_digit, has_special])
    points += categories  # adds 0..4
    points = min(points, 5)

    if points <= 1:
        label = 'Very weak'
    elif points == 2:
        label = 'Weak'
    elif points == 3:
        label = 'Medium'
    elif points == 4:
        label = 'Strong'
    else:
        label = 'Very strong'

    suggestions = []
    if length < 12:
        suggestions.append('Use at least 12 characters (longer is better).')
    if not has_upper:
        suggestions.append('Add uppercase letters.')
    if not has_lower:
        suggestions.append('Add lowercase letters.')
    if not has_digit:
        suggestions.append('Add digits.')
    if not has_special:
        suggestions.append('Add special characters (e.g. !@#$%).')
    if ' ' in password:
        suggestions.append('Avoid spaces if possible (or be intentional with passphrases).')

    suggestions.append(f'Estimated entropy: {entropy:.1f} bits (aim for >= 60 bits for long-term safety).')

    return {
        'score': points,
        'label': label,
        'entropy': entropy,
        'suggestions': suggestions
    }

def cli():
    parser = argparse.ArgumentParser(description='Password strength checker')
    parser.add_argument('password', nargs='?', help='Password to evaluate (or omit to prompt)')
    parser.add_argument('--quiet', action='store_true', help='Only print label')
    args = parser.parse_args()

    if args.password:
        pwd = args.password
    else:
        try:
            pwd = input('Enter password: ')
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)

    res = check_password_strength(pwd)
    if args.quiet:
        print(res['label'])
        return

    print(f'Password length: {len(pwd)} — {res["label"]}')
    print(f'Entropy: {res["entropy"]:.1f} bits')
    print('Suggestions:')
    for s in res['suggestions']:
        print(' -', s)

if __name__ == '__main__':
    cli()
