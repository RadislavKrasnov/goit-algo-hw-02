"""Task one - service center"""
from queue import Queue
from uuid import uuid1

queue = Queue()

def generate_request() -> None:
    """Generates queue message - message publisher."""
    request = {
        "id": uuid1(),
        "message": f'Message Text {uuid1()}'
    }
    queue.put(request)
       
def process_request() -> None:
    """Process queue message - message comsumer."""
    if not queue.empty():
        request = queue.get()
        id = request["id"]
        message = request["message"]
        print(f"Request with id: {id} and message: '{message}' is processed.")
    else:
        print('Queue is empty')

try:
    while True:
        generate_request()
        process_request()
except KeyboardInterrupt:
    pass
