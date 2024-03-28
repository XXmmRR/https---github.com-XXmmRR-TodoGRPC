import asyncio
import proto.todo_pb2 as todo_pb2 
import grpc
import logging
import proto.todo_pb2_grpc as todo_pb2_grpc
import time
from concurrent import futures
from google.protobuf import empty_pb2
import os


async def serve() -> None:
    server = grpc.aio.server()
    todo_pb2_grpc.add_TodoServiceServicer_to_server(todo_pb2_grpc.TodoServiceServicer(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


# Wait for the server to stop
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
    