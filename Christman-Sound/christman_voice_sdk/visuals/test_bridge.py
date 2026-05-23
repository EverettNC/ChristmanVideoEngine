from timbre.memory_bridge import MemoryBridge
import time

bridge = MemoryBridge(name="timbre_stream")

print("Waiting for data from TimbreModeler...")
while True:
    data = bridge.read()
    if data:
        print(f"Engine Data Received: F0={data['f0']:.2f} Hz")
    time.sleep(0.1) # 10Hz polling is plenty for a console test
