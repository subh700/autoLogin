#!/usr/bin/env bash
# ==============================================================================
# NIT Sikkim Captive Portal - Direct Linux Installer (Kali / Debian / Ubuntu)
# ==============================================================================

if [ "$EUID" -ne 0 ]; then
    echo "[!] Please run with root privileges: sudo ./install_linux.sh"
    exit 1
fi

echo "[+] Installing NIT Sikkim Portal..."

# 1. Install dependencies
if command -v apt-get >/dev/null 2>&1; then
    echo "[+] Verifying python3-tk dependency..."
    apt-get update -qq && apt-get install -y -qq python3 python3-tk curl >/dev/null 2>&1 || true
fi

# 2. Create directories
mkdir -p /usr/share/nit-portal
mkdir -p /usr/share/applications
mkdir -p /usr/bin

# 3. Copy application files
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_SOURCE="$DIR/../"

if [ -f "$APP_SOURCE/gui_app.py" ]; then
    cp "$APP_SOURCE/gui_app.py" /usr/share/nit-portal/
    cp "$APP_SOURCE/portal_core.py" /usr/share/nit-portal/
    [ -f "$APP_SOURCE/.env" ] && cp "$APP_SOURCE/.env" /usr/share/nit-portal/
fi

# 4. Create launcher script
cat << 'EOF' > /usr/bin/nit-portal-gui
#!/usr/bin/env bash
exec /usr/bin/python3 /usr/share/nit-portal/gui_app.py "$@"
EOF

# 5. Create Desktop Menu entry
cat << 'EOF' > /usr/share/applications/nit-portal.desktop
[Desktop Entry]
Name=NIT Sikkim Portal
Comment=Sophos Captive Portal Auto-Keeper
Exec=/usr/bin/nit-portal-gui
Icon=network-wireless
Terminal=false
Type=Application
Categories=Network;Utility;
Keywords=internet;portal;login;wifi;nit;
EOF

# Set permissions
chmod 755 /usr/bin/nit-portal-gui
chmod 755 /usr/share/nit-portal/gui_app.py
chmod 644 /usr/share/nit-portal/portal_core.py
chmod 666 /usr/share/nit-portal/.env 2>/dev/null || true

if command -v update-desktop-database > /dev/null 2>&1; then
    update-desktop-database -q || true
fi

echo "[✓] Installation complete!"
echo "You can now open 'NIT Sikkim Portal' from your Application Menu or run: nit-portal-gui"
