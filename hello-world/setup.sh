#!/usr/bin/env bash
set -e

echo "🚀 Setting up MCP Playground (client + server)"

VENV_DIR=".venv"

# -----------------------------
# Detect Python
# -----------------------------
if command -v python3.11 &>/dev/null; then
  PYTHON_CMD="python3.11"
elif command -v python3 &>/dev/null; then
  PYTHON_CMD="python3"
else
  echo "❌ Python not found. Please install Python 3.11+"
  exit 1
fi

PY_VERSION=$($PYTHON_CMD -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✅ Using Python ${PY_VERSION}"

# -----------------------------
# Warn for newer Python versions
# -----------------------------
PY_MINOR=$($PYTHON_CMD -c 'import sys; print(sys.version_info.minor)')
if [ "$PY_MINOR" -gt 11 ]; then
  echo "⚠️  Warning: Python 3.$PY_MINOR detected"
  echo "⚠️  Agentic / MCP ecosystem is most stable on Python 3.10–3.11"
  echo "⚠️  Continuing anyway..."
fi

# -----------------------------
# Create virtual environment
# -----------------------------
if [ ! -d "$VENV_DIR" ]; then
  echo "📦 Creating virtual environment..."
  $PYTHON_CMD -m venv "$VENV_DIR"
else
  echo "📦 Virtual environment already exists"
fi

# -----------------------------
# Activate venv
# -----------------------------
echo "🔌 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# -----------------------------
# Upgrade pip
# -----------------------------
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# -----------------------------
# Install server dependencies
# -----------------------------
if [ -f "server/requirements.txt" ]; then
  echo "📥 Installing server dependencies..."
  pip install -r server/requirements.txt
else
  echo "⚠️ server/requirements.txt not found"
fi

# -----------------------------
# Install client dependencies
# -----------------------------
if [ -f "client/requirements.txt" ]; then
  echo "📥 Installing client dependencies..."
  pip install -r client/requirements.txt
else
  echo "⚠️ client/requirements.txt not found"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  source .venv/bin/activate"
echo "  export OPENWEATHER_API_KEY=your_api_key_here"
echo ""
echo "Run servers:"
echo "  python server/math_server.py"
echo "  python server/weather_server.py"
echo ""
echo "Run client:"
echo "  python client/main.py"
