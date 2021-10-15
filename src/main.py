import asyncio
from utils import common
from concurrent import futures
import logging
import grpc
from packages.grpc import greeter_pb2_grpc, greeter_pb2


async def callphone(ms: int):
    common.say_hello("Hello world!")
    await asyncio.sleep(ms)
    common.say_hello("Hello again!")


class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(message='Hello, %s! [from python]' % request.name)


async def application():
    await callphone(2)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:6000')
    server.start()
    server.wait_for_termination()


task = application()
asyncio.run(task)
