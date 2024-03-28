# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from database.models.todo_models import Todo
import proto.todo_pb2 as todo__pb2


class TodoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTodo = channel.unary_unary(
                '/todo.TodoService/GetTodo',
                request_serializer=todo__pb2.GetTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.Todo.FromString,
                )
        self.GetTodoList = channel.unary_unary(
                '/todo.TodoService/GetTodoList',
                request_serializer=todo__pb2.void.SerializeToString,
                response_deserializer=todo__pb2.TodoList.FromString,
                )
        self.UpdateTodo = channel.unary_unary(
                '/todo.TodoService/UpdateTodo',
                request_serializer=todo__pb2.GetTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.Todo.FromString,
                )
        self.DeleteTodo = channel.unary_unary(
                '/todo.TodoService/DeleteTodo',
                request_serializer=todo__pb2.GetTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.Todo.FromString,
                )


class TodoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    async def GetTodo(self, request, context: grpc.aio.ServicerContext,):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    async def GetTodoList(self, request, context: grpc.aio.ServicerContext,):
        """Missing associated documentation comment in .proto file."""
        raise NotImplementedError('Method not implemented!')

    async def UpdateTodo(self, request, context: grpc.aio.ServicerContext,):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    async def DeleteTodo(self, request, context: grpc.aio.ServicerContext,):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodo,
                    request_deserializer=todo__pb2.GetTodoRequest.FromString,
                    response_serializer=todo__pb2.Todo.SerializeToString,
            ),
            'GetTodoList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodoList,
                    request_deserializer=todo__pb2.void.FromString,
                    response_serializer=todo__pb2.TodoList.SerializeToString,
            ),
            'UpdateTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTodo,
                    request_deserializer=todo__pb2.GetTodoRequest.FromString,
                    response_serializer=todo__pb2.Todo.SerializeToString,
            ),
            'DeleteTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTodo,
                    request_deserializer=todo__pb2.GetTodoRequest.FromString,
                    response_serializer=todo__pb2.Todo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


