#! /usr/vin/env bash

# Initialize DB
python /app/app/backend_pre_start.py

# Run migrations
# TODO: add albemic?

python /app/app/initialize.py