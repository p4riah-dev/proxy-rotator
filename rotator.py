# proxy-rotator

Automatic proxy rotation tool for anonymous network operations.

## Features
- Auto proxy rotation
- SOCKS4/SOCKS5 support
- Proxy health checking
- Custom rotation intervals
- Connection anonymity verification

## Usage
```bash
python3 rotator.py --interval 30
python3 rotator.py --proxy-list proxies.txt --interval 60
```

## Examples
```bash
# Rotate every 30 seconds
python3 rotator.py --interval 30

# Use custom proxy list
python3 rotator.py --proxy-list myproxies.txt
```

## Requirements
- Python 3.x
- requests
- socks

## Disclaimer
For authorized and educational use only.
