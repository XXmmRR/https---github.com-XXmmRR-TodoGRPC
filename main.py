import todo_pb2 
import grpc
import logging
import todo_pb2_grpc
import time
from concurrent import futures
from google.protobuf import empty_pb2
import os

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Add the TodoServicer to the server
todo_pb2_grpc.add_TodoServiceServicer_to_server(todo_pb2_grpc.TodoServiceServicer(), server)

# Start the server
server.add_insecure_port('[::]:50051')
server.start()
logging.info("Server started on port 50051")

# Wait for the server to stop
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
    