#!/bin/bash

echo "================================================"
echo "🚀 NAMELESS - SMART INSTALLER"
echo "Created by: @ERROR0101risback | fahad0101r"
echo "================================================"

# FUNCTION: Check if Python is installed
check_python() {
    if command -v python3 &>/dev/null; then
        echo "✅ Python already installed: $(python3 --version)"
        return 0
    else
        return 1
    fi
}

# FUNCTION: Install Python (based on OS)
install_python() {
    echo "📦 Python not found! Installing Python..."
    
    # Detect OS
    if [[ -f /etc/debian_version ]]; then
        # Debian/Ubuntu
        sudo apt update
        sudo apt install -y python3 python3-pip
    elif [[ -f /etc/redhat-release ]]; then
        # RedHat/CentOS
        sudo yum install -y python3 python3-pip
    elif [[ -d /data/data/com.termux ]]; then
        # Termux (Android)
        pkg update
        pkg install -y python
    else
        echo "❌ Cannot detect OS. Please install Python manually"
        echo "   Download from: https://www.python.org/downloads/"
        exit 1
    fi
}

# FUNCTION: Check if package is installed
check_package() {
    python3 -c "
import importlib.util
import sys

package = '$1'
spec = importlib.util.find_spec(package)
if spec is None:
    print(f'❌ {package} not installed')
    sys.exit(1)
else:
    print(f'✅ {package} already installed')
    sys.exit(0)
"
    return $?
}

# FUNCTION: Install Python package
install_package() {
    echo "📦 Installing $1..."
    pip3 install $1
}

# MAIN SCRIPT STARTS HERE
echo ""
echo "🔍 STEP 1: Checking Python installation..."
if ! check_python; then
    install_python
else
    echo "   ✓ Python OK"
fi

echo ""
echo "🔍 STEP 2: Checking pip..."
pip3 --version &>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing pip..."
    python3 -m ensurepip --upgrade
else
    echo "   ✓ pip OK"
fi

echo ""
echo "🔍 STEP 3: Checking embedchain package..."
if ! check_package "embedchain"; then
    install_package "embedchain"
else
    echo "   ✓ embedchain OK"
fi

echo ""
echo "================================================"
echo "✅ ALL CHECKS COMPLETE! Starting Nameless..."
echo "================================================"
echo ""

# RUN THE PYTHON SCRIPT
python3 app.py
