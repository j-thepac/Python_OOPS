from multiprocessing import Process
import os

def worker():
    print(f"Process ID: {os.getpid()}")

# Create and start a process
process = Process(target=worker)
process.start()
process.join()  # Wait for the process to finish
# Advantages: Bypasses GIL, suitable for CPU-bound tasks.

"""
System
├── Process 1
│   ├── Thread A
│   ├── Thread B
│   └── Thread C
├── Process 2
│   ├── Thread X
│   └── Thread Y
└── Process 3
    └── Main Thread (only)

+---------------------------+--------------------------------+----------------------------------+
| Aspect                    | Threads                        | Processes                        |
+---------------------------+--------------------------------+----------------------------------+
| GIL Impact                | Limited by GIL - no true       | Bypasses GIL - true parallelism |
|                           | parallelism for CPU tasks      | for CPU-bound tasks              |
+---------------------------+--------------------------------+----------------------------------+
| Best Use Case             | I/O-bound tasks (file/network) | CPU-bound tasks (computation)    |
+---------------------------+--------------------------------+----------------------------------+
| Memory Usage              | Low - shared memory space      | High - separate memory space     |
+---------------------------+--------------------------------+----------------------------------+
| Creation Overhead         | Fast and lightweight           | Slow and resource-intensive      |
+---------------------------+--------------------------------+----------------------------------+
| Data Sharing              | Easy - shared variables         | Complex - requires IPC           |
|                           | and objects                     | (pipes, queues, shared memory)   |
+---------------------------+--------------------------------+----------------------------------+
| Communication Speed       | Fast - direct memory access    | Slower - serialization needed    |
+---------------------------+--------------------------------+----------------------------------+
| Isolation                 | None - shared process space     | Complete - separate processes    |
+---------------------------+--------------------------------+----------------------------------+
| Fault Tolerance           | Low - one crash affects all    | High - isolated failures         |
+---------------------------+--------------------------------+----------------------------------+
| Debugging Complexity      | Hard - race conditions,         | Easier - isolated execution      |
|                           | shared state issues             |                                  |
+---------------------------+--------------------------------+----------------------------------+
| Synchronization           | Required - locks, semaphores   | Less critical - natural isolation|
+---------------------------+--------------------------------+----------------------------------+
| Python Module             | threading                       | multiprocessing                  |
+---------------------------+--------------------------------+----------------------------------+
| Scalability               | Limited by GIL on CPU tasks    | Scales with available CPU cores  |
+---------------------------+--------------------------------+----------------------------------+
| Context Switching         | Fast                           | Slower                           |
+---------------------------+--------------------------------+----------------------------------+
| Platform Dependency      | Less - native thread support   | More - OS-dependent process mgmt |
+---------------------------+--------------------------------+----------------------------------+

System
├── Process 1
│   ├── Thread A
│   ├── Thread B
│   └── Thread C
├── Process 2
│   ├── Thread X
│   └── Thread Y
└── Process 3
    └── Main Thread (only)


"""
