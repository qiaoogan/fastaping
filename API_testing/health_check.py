import time
from clients.TestClient import get_health

while True:
    response = get_health()
    if response.status_code == 200:
        break
    else:
        print("checking health ...")
        time.sleep(2)
