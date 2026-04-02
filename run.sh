#!/usr/bin/env bash
cd /home/eme/batompreto || exit 1
rm -f /tmp/batompreto.lock
python3 /home/eme/batompreto/app.py
