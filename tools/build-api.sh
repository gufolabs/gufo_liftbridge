#!/bin/sh

set -x
set -e

API_REPO=/tmp/liftbridge-api
OUT=src/gufo/liftbridge

if [ -d "$API_REPO" ]; then
    echo "$API_REPO is already exists. Cleanup before runnings script."
    exit 1
fi

# Clone liftbridge-api repo
git clone https://github.com/liftbridge-io/liftbridge-api.git $API_REPO

# Compile
python3 -m grpc_tools.protoc\
    -I$API_REPO\
    --python_out=$OUT\
    --pyi_out=$OUT\
    --grpc_python_out=$OUT\
    api.proto

# Fix import
GRPC_SRC=./src/gufo/liftbridge/api_pb2_grpc.py
cp $GRPC_SRC /tmp
cat /tmp/api_pb2_grpc.py | sed "s/import api_pb2 as api__pb2/import gufo.liftbridge.api_pb2 as api__pb2/" > $GRPC_SRC
rm /tmp/api_pb2_grpc.py

# Format code
black $OUT/api_pb2.py $OUT/api_pb2_grpc.py $OUT/api_pb2.pyi

# Cleanup API repo
rm -r $API_REPO