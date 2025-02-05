# 🔬 Advanced Usage of Ethereal SDK

Welcome to the **Advanced Usage** guide for Ethereal SDK! 🚀 This guide will help you unlock the full potential of the SDK by covering advanced concepts and techniques.

---

## 📌 Table of Contents
1. [Customizing Agent Memory](#customizing-agent-memory)
2. [Creating Dynamic Workflows](#creating-dynamic-workflows)
3. [Real-Time API Integrations](#real-time-api-integrations)
4. [Task Queue and Execution](#task-queue-and-execution)
5. [Enhancing Performance](#enhancing-performance)
6. [Web3 Integration for Transparent Logging](#web3)
---

## 🧠 Customizing Agent Memory
By default, **Ethereal SDK** provides a simple memory system, but you can extend it to add persistence or complex data handling.

### 🔹 Example: Implementing Persistent Memory
```python
from openmeta.core.memory import Memory

class PersistentMemory(Memory):
    def save_to_file(self, filename="memory.json"):
        import json
        with open(filename, "w") as f:
            json.dump(self.storage, f)

    def load_from_file(self, filename="memory.json"):
        import json
        with open(filename, "r") as f:
            self.storage = json.load(f)
```
💡 **Usage:** Store and retrieve agent memory across sessions!

---

## 🔄 Creating Dynamic Workflows
Workflows allow agents to execute complex sequences of actions dynamically.

### 🔹 Example: Conditional Workflow Execution
```python
from openmeta.core.workflows import Workflow

def step1():
    return "Collecting data..."

def step2():
    return "Processing data..."

def conditional_step():
    return "Performing advanced analytics..."

steps = [step1, step2]
if True:  # Condition can be dynamically set
    steps.append(conditional_step)

workflow = Workflow(steps)
print(workflow.execute())
```
💡 **Use case:** Modify agent workflows based on external conditions or real-time data.

---

## 🌐 Real-Time API Integrations
Integrating with real-time APIs enables AI agents to interact dynamically with external services.

### 🔹 Example: Fetching Live Data
```python
from openmeta.integrations.external_api import ExternalAPI

api = ExternalAPI("https://api.example.com")
data = api.fetch_data("/live-endpoint")
print(data)
```
💡 **Use case:** Enable AI agents to access up-to-date information from online sources.

---

## 📌 Task Queue and Execution
Efficient task management is crucial for AI-driven applications. The `TaskQueue` module provides structured task handling with priority-based execution.

### 🔹 Example: Using TaskQueue for Prioritized Processing
```python
from openmeta.core.task_queue import TaskQueue

task_queue = TaskQueue()

task1 = {"id": 1, "priority": 2, "task_type": "analysis"}
task2 = {"id": 2, "priority": 1, "task_type": "data_cleaning"}

task_queue.add_to_queue(task1)
task_queue.add_to_queue(task2)
task_queue.process_queue()
```
💡 **Use case:** Manage and execute tasks based on priority.

### 🔹 Example: Task Execution Mechanism
```python
def execute_task(task: dict):
    print(f"Executing task {task['id']}...")
```
💡 **Use case:** Define custom execution logic for tasks in the queue.

---

## ⚡ Enhancing Performance
For large-scale applications, optimizing execution speed is crucial.

### 🔹 Example: Running Tasks in Parallel
```python
import concurrent.futures
from openmeta.core.agent import Agent
from openmeta.core.memory import Memory

def run_agent_task(task):
    memory = Memory()
    agent = Agent("ParallelAgent", memory)
    return agent.process_task(task)

tasks = ["Task A", "Task B", "Task C"]
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(run_agent_task, tasks))

print(results)
```
💡 **Use case:** Run multiple agent processes in parallel to reduce execution time.

---
## Web3 Integration for Transparent Logging

With **Ethereal SDK v0.0.5**, you can now integrate **Web3** to log agent actions transparently on the blockchain. This integration helps in enhancing traceability and accountability, by storing agent actions on the blockchain in an immutable ledger. 

### 🔹 Example: Setting Up Web3 Logging

To use Web3 logging, you need to configure the `Web3Logger` class. Here's how you can initialize and use Web3 for logging agent actions:

```python
from openmeta.core.web3_logger import Web3Logger

# Initialize Web3Logger with Ethereum network and provider URL
web3_logger = Web3Logger(network="ethereum", provider_url="https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID")

# Log an action to the blockchain
agent_id = "agent_1"
action = "perform_action"
tx_hash = web3_logger.log_to_blockchain(agent_id, action)

print(f"Transaction Hash: {tx_hash.hex()}")
```

💡 **Use case:** Log and trace actions of your agents on the blockchain to ensure complete transparency and accountability.

---

### 🔹 Example: Retrieving Logs from the Blockchain

You can also retrieve logs from the blockchain to analyze the actions performed by agents. Here's an example of how to do that:

```python
# Retrieve logs for a specific agent from the blockchain
agent_id = "agent_1"
log_data = web3_logger.retrieve_log(agent_id)

print(f"Retrieved log data: {log_data}")
```

💡 **Use case:** Retrieve agent logs to monitor actions or verify transactions on the blockchain.

---

### 🔹 Example: Enabling or Disabling Web3 Logging

You can easily enable or disable Web3 logging by modifying the configuration in your settings:

```python
from openmeta.config.settings import Settings

settings = Settings()

# Enable Web3 logging
settings.set("use_web3_logging", True)

# Disable Web3 logging
settings.set("use_web3_logging", False)
```

💡 **Use case:** Toggle Web3 logging based on different environments (e.g., enabling it in production for transparency and disabling in testing environments).

---

### 🔹 Example: Handling Web3 Errors and Failures

Since blockchain transactions can sometimes fail or encounter errors (e.g., network issues, insufficient funds, etc.), it's important to handle these errors gracefully. Here's how you can catch and handle errors:

```python
try:
    tx_hash = web3_logger.log_to_blockchain(agent_id, action)
    print(f"Transaction Hash: {tx_hash.hex()}")
except Exception as e:
    print(f"Error logging action to blockchain: {e}")
```

💡 **Use case:** Ensure that your application can gracefully handle Web3-related errors and provide fallback mechanisms when necessary.

---


🚀 **Congratulations!** You've now explored the advanced capabilities of **Ethereal SDK**. Start building smarter AI agents today! 🎉

