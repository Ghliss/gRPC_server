# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging
import time
import grpc
import serv_pb2
import serv_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Hello ")
    with grpc.insecure_channel('localhost:50051') as channel:
       stub = serv_pb2_grpc.MqttservicesStub(channel)
       clt= stub.connect(serv_pb2.conInfo(adr=15))
       
       print("client request sent! " )
       
       pub = stub.publish(clt)
       
       print("client published" )
       sub = stub.subscribe(serv_pb2.subInfo(adr=15))
      

       print("client subscribed")
       dis = stub.disconnect(serv_pb2.disInfo(adr=15))
      
    
       print("client disconnected")
       
if __name__ == '__main__':
  logging.basicConfig()
  run()
