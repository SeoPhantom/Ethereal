# 📖 Ethereal SDK API Reference

Welcome to the **Ethereal SDK API Reference**! This document provides an in-depth look at the core components and their functionalities within the SDK. 🛠️

---

## 📌 Table of Contents
1. [Core Modules](#core-modules)
2. [Integrations](#integrations)
3. [Utilities](#utilities)
4. [Examples](#examples)

---

## 🏗 Core Modules
These are the fundamental building blocks of **Ethereal SDK**.

### 🔹 `Agent`
Manages AI-driven agents and their behaviors.
```python
from openmeta.core.agent import Agent
agent = Agent("EtherealAI", memory)
agent.process_task("Analyze dataset")
```
💡 **Key Methods:**
- `process_task(task: str) -> str`: Processes a task and stores it in memory.

### 🔹 `Memory`
Handles agent memory operations.
```python
from openmeta.core.memory import Memory
memory = Memory()
memory.store("Data item")
print(memory.retrieve())
```
💡 **Key Methods:**
- `store(data: any)`: Stores data in memory.
- `retrieve(index: int = None) -> any`: Retrieves stored data.

### 🔹 `Workflow`
Defines workflow patterns for AI agents.
```python
from openmeta.core.workflows import Workflow
workflow = Workflow([step1, step2, step3])
workflow.execute()
```
💡 **Key Methods:**
- `execute() -> list`: Runs each step in sequence and returns results.

---

## 🔗 Integrations
Extend functionality with external APIs and Web3 technologies.

### 🌐 `ExternalAPI`
Fetches data from third-party APIs.
```python
from openmeta.integrations.external_api import ExternalAPI
api = ExternalAPI("https://api.example.com")
print(api.fetch_data("/endpoint"))
```
💡 **Key Methods:**
- `fetch_data(endpoint: str) -> dict`: Fetches data from an external API.

### ⛓ `BlockchainConnector`
Integrates AI agents with blockchain networks.
```python
from openmeta.integrations.blockchain import BlockchainConnector
blockchain = BlockchainConnector("Ethereum")
print(blockchain.connect())
```
💡 **Key Methods:**
- `connect() -> str`: Connects to a blockchain network.

---

## ⚙ Utilities
Helper functions for logging, validation, and debugging.

### 📜 `Logger`
Handles logging across modules.
```python
from openmeta.utils.logging_utils import Logger
logger = Logger(level="DEBUG")
logger.log("This is a debug message")
```
💡 **Key Methods:**
- `log(message: str) -> None`: Logs messages with a specified level.

### ✅ `Validator`
Ensures correct data formats and integrity.
```python
from openmeta.utils.validators import Validator
valid = Validator.validate_data({"key": "value"})
```
💡 **Key Methods:**
- `validate_data(data: any) -> bool`: Checks if data is in the correct format.

---

## 🎯 Examples
Want to see **Ethereal SDK** in action? Check out the **[Example Scripts](../examples)** for practical implementations!

📄 **Minimal Agent:** [View Code](../examples/minimal_agent.py)  
🔁 **Workflow Demo:** [View Code](../examples/workflow_demo.py)  
🌐 **Integration Example:** [View Code](../examples/integration_example.py)  

📖 For advanced concepts, visit **[Advanced Usage](examples/advanced_usage.md)**.

---

🚀 **Start building with Ethereal SDK today!** 🚀