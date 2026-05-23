"""
Timbre Memory Bridge — High-Speed IPC for Visualizers
Handles shared memory allocation between TimbreModeler and RenderEngine.
"""

import numpy as np
from multiprocessing import shared_memory
import struct

class MemoryBridge:
    def __init__(self, name="timbre_stream", size=4096):
        self.name = name
        self.size = size
        try:
            self.shm = shared_memory.SharedMemory(name=self.name, create=True, size=self.size)
        except FileExistsError:
            self.shm = shared_memory.SharedMemory(name=self.name)
        
        # Buffer layout: [Flag (1), F0 (4), F1 (4), F2 (4), X-Vec (512*4)]
        self.fmt = 'f f f f 512f' 
        self.data_size = struct.calcsize(self.fmt)

    def push(self, f0, f1, f2, x_vec):
        """Write current voice metrics to shared memory."""
        packed = struct.pack(self.fmt, 1.0, f0, f1, f2, *x_vec.tolist())
        self.shm.buf[:self.data_size] = packed

    def close(self):
        self.shm.close()
        self.shm.unlink()
    
    def read(self):
        """Read latest voice metrics from shared memory."""
        try:
            packed = self.shm.buf[:self.data_size]
            data = struct.unpack(self.fmt, packed)
            # data[0] is our status flag; data[1:] are the metrics
            if data[0] > 0:
                return {
                    "f0": data[1], 
                    "f1": data[2], 
                    "f2": data[3], 
                    "x_vec": data[4:]
                }
        except Exception:
            return None
        return None"""
Timbre Memory Bridge — High-Speed IPC for Visualizers
Handles shared memory allocation between TimbreModeler and RenderEngine.
"""

import numpy as np
from multiprocessing import shared_memory
import struct

class MemoryBridge:
    def __init__(self, name="timbre_stream", size=4096):
        self.name = name
        self.size = size
        try:
            self.shm = shared_memory.SharedMemory(name=self.name, create=True, size=self.size)
        except FileExistsError:
            self.shm = shared_memory.SharedMemory(name=self.name)
        
        # Buffer layout: [Flag (1), F0 (4), F1 (4), F2 (4), X-Vec (512*4)]
        self.fmt = 'f f f f 512f' 
        self.data_size = struct.calcsize(self.fmt)

    def push(self, f0, f1, f2, x_vec):
        """Write current voice metrics to shared memory."""
        packed = struct.pack(self.fmt, 1.0, f0, f1, f2, *x_vec.tolist())
        self.shm.buf[:self.data_size] = packed

    def close(self):
        self.shm.close()
        self.shm.unlink()
    
    def read(self):
     """Read latest voice metrics from shared memory."""
        try:
           packed = self.shm.buf[:self.data_size]
            data = struct.unpack(self.fmt, packed)
            # data[0] is our status flag; data[1:] are the metrics
            if data[0] > 0:
                return {"f0": data[1], "f1": data[2], "f2": data[3], "x_vec": data[4:]}
        except Exception:
            return None
        return None
#
