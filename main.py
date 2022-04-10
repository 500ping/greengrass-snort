import sys
import src.greeter as greeter
import time
import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    QOS,
    PublishToIoTCoreRequest
)
from datetime import datetime

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        print(greeter.get_greeting(args[0]))

    TIMEOUT = 10

    ipc_client = awsiot.greengrasscoreipc.connect()
                        
    topic = "my/topic"
    message = "Hello, World"
    qos = QOS.AT_LEAST_ONCE
    while True:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        request = PublishToIoTCoreRequest()
        request.topic_name = topic
        request.payload = bytes(f"{current_time}: {message}", "utf-8")
        request.qos = qos
        operation = ipc_client.new_publish_to_iot_core()
        operation.activate(request)
        future = operation.get_response()
        future.result(TIMEOUT)
        time.sleep(10)

    
if __name__ == "__main__":
    main()