# 🏁 Getting Started with Ethereal SDK

Welcome to **Ethereal SDK**! This guide will walk you through the installation, setup, and first steps to building agentic AI systems. 🚀

---

## 📥 Prerequisites
Before you begin, make sure you have the following installed:

✅ **Python 3.8+** (Check your version with `python --version`)
✅ **Git** (For cloning the repository, optional)
✅ **pip** or **Poetry** (For managing dependencies)

If you don’t have Python installed, download it from [Python.org](https://www.python.org/downloads/).

---

## ⚡ Installation

### **1️⃣ Clone the Repository** *(Optional)*
If you want the latest version from GitHub, run:
```sh
git clone https://github.com/your-repo/ethereal-sdk.git
cd ethereal-sdk
```

### **2️⃣ Set Up a Virtual Environment** *(Recommended)*
To avoid dependency conflicts, create a virtual environment:
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
#### Using `pip`
```sh
pip install -r requirements.txt
```
#### Using `Poetry`
```sh
poetry install
```

---

## 🚀 Running the Examples
After installation, try running a sample agent to ensure everything is working:

### **Run Minimal Agent**
```sh
python -m examples.minimal_agent
```
💡 **Expected Output:**
```
Processing task: Analyze data stream
```

### **Run Workflow Demo**
```sh
python -m examples.workflow_demo
```
💡 **Expected Output:**
```
['Step 1: Data preprocessing', 'Step 2: Model training', 'Step 3: Evaluation']
```

### **Run API & Blockchain Integration**
```sh
python -m examples.integration_example
```
💡 **Expected Output:**
```
{'status': 'success', 'data': 'Mock data from https://example.com/api/test-endpoint'}
Connected to Ethereum blockchain
```

---

## 🔍 Next Steps
📖 Check out the [API Reference](api_reference.md) for a deep dive into each module.
🛠 Modify the [example scripts](../examples) to fit your own use case.
🌍 Explore [Advanced Usage](examples/advanced_usage.md) for complex implementations.

Now you're all set! Happy coding with **Ethereal SDK**! 🚀🎉