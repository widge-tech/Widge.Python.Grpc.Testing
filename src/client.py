import grpc
from packages.grpc import greeter_pb2_grpc, greeter_pb2


def run():
  channel = grpc.insecure_channel('[::]:6000')
  stub = greeter_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(greeter_pb2.HelloRequest(name='Tom'))
  print("Greeter client received: " + response.message)
  response = stub.SayHello(greeter_pb2.HelloRequest(name='Jerry'))
  print("Greeter client received: " + response.message)

run()