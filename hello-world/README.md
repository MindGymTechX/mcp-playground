# MCP Playground – Hello World Samples

Welcome to **MCP Playground – Hello World**, a starter project demonstrating **MCP (Multi-Server Control Protocol)** usage with simple example apps. This repository provides a lightweight **server implementation** and example workflows such as **Weather Forecast** and **Calculator**, perfect for learning and experimentation.

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Getting Started](#getting-started)
* [Examples](#examples)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)

---

## Overview

MCP Playground is designed to help developers **experiment with agentic workflows** and **multi-server MCP clients**. The `hello-world` module focuses on **simple, easy-to-understand examples** to showcase server-client interactions.

Key goals of this project:

* Provide a minimal **MCP server setup** for local testing.
* Demonstrate **basic workflows** like calculations and weather lookups.
* Serve as a foundation for more complex **agentic AI workflows**.

---

## Features

* **Hello World server** running MCP endpoints.
* Sample apps demonstrating simple **MCP commands**:

  * **Weather Forecast** – Returns a sample weather report.
  * **Calculator** – Performs basic arithmetic operations.
* Lightweight and easy to extend with new samples.

---

## Getting Started

### Prerequisites

* Python 3.11+
* Virtual environment recommended

### Installation

1. Clone the repository:

```bash
git clone https://github.com/MindGymTechX/mcp-playground.git
cd mcp-playground/hello-world
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Server

```bash
python server.py
```

The server will start and listen for MCP client requests.

---

## Examples

### Weather Forecast

Send a request to the server to get a **sample weather forecast**:

```python
from client import MCPClient

client = MCPClient()
forecast = client.weather(city="New York")
print(forecast)
```

### Calculator

Perform basic arithmetic operations:

```python
from client import MCPClient

client = MCPClient()
result = client.calculate(expression="2 + 3 * 4")
print(result)  # Output: 14
```

---

## Project Structure

```
hello-world/
├── server.py          # MCP server with example endpoints
├── client.py          # Sample MCP client for testing
├── examples/          # Example scripts for Weather, Calculator
├── requirements.txt   # Python dependencies
└── README.md
```

---

## Contributing

We welcome contributions! You can:

* Add new sample workflows
* Improve server or client implementations
* Enhance documentation

Please fork the repo and create a PR with your changes.

---

## License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.
