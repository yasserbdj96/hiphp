#!/bin/sh

find . -type d -name __pycache__ -prune -exec rm -rf {} \;
find . -type d -name venv -prune -exec rm -rf {} \;

appname="hiphp"  # Replace with your app name
file_path="version.txt"
version=$(head -n 1 "$file_path")

script_path=$(dirname "$(readlink -f "$0")")

#version="2.0"    # Replace with your app version

# Create a temporary directory to build the .deb package
tmp_dir="$(mktemp -d)"
deb_dir="$tmp_dir/$appname-$version"
mkdir -p "$deb_dir/DEBIAN"
mkdir -p "$deb_dir/usr/share/$appname"
mkdir -p "$deb_dir/usr/share/applications"
mkdir -p "$deb_dir/usr/local/bin"
mkdir -p "$deb_dir/usr/share/hiphp/hiphp/"
mkdir -p "$deb_dir/usr/share/hiphp/hiphp-desktop/"
mkdir -p "$deb_dir/usr/share/hiphp/hiphp-tk/"
mkdir -p "$deb_dir/usr/share/hiphp/hiphp-linux/"
mkdir -p "$deb_dir/usr/share/hiphp/install/"

# Copy necessary files and folders to the .deb package directory
cp -r ./hiphp/* "$deb_dir/usr/share/hiphp/hiphp/"
cp -r ./hiphp-desktop/* "$deb_dir/usr/share/hiphp/hiphp-desktop/"
cp -r ./hiphp-tk/* "$deb_dir/usr/share/hiphp/hiphp-tk/"
cp ./hiphp-linux/requirements-linux.txt "$deb_dir/usr/share/hiphp/hiphp-linux/"
cp ./main.py "$deb_dir/usr/share/hiphp/main.py"
cp -r ./install/* "$deb_dir/usr/share/hiphp/install/"
cp ./requirements.txt "$deb_dir/usr/share/hiphp/requirements.txt"

# Generate the control file for the .deb package
control_file="$deb_dir/DEBIAN/control"
echo "Package: $appname" > "$control_file"
echo "Version: $version" >> "$control_file"
echo "Architecture: all" >> "$control_file"
echo "Maintainer: Your Name <your@email.com>" >> "$control_file"
echo "Description: Your application description" >> "$control_file"

# Add post-installation script to install dependencies and perform additional operations
postinst_file="$deb_dir/DEBIAN/postinst"
echo "#!/bin/sh" > "$postinst_file"
echo "set -e" >> "$postinst_file"
echo "" >> "$postinst_file"
echo "mkdir -p /usr/share/$appname" >> "$postinst_file"
echo "# Perform additional operations" >> "$postinst_file"
echo "cp /usr/share/$appname/install/hiphp.desktop /usr/share/applications/$appname.desktop" >> "$postinst_file"
echo "cp /usr/share/$appname/install/hiphp.sh /usr/local/bin/$appname" >> "$postinst_file"
echo "cp /usr/share/$appname/main.py /usr/share/$appname/hiphp.py" >> "$postinst_file"
echo "cp /usr/share/$appname/install/$appname.png /usr/share/$appname/$appname.png" >> "$postinst_file"
echo "" >> "$postinst_file"
echo "# Install dependencies" >> "$postinst_file"
echo "pip install -r /usr/share/$appname/requirements.txt" >> "$postinst_file"
echo "pip install -r /usr/share/$appname/hiphp-linux/requirements-linux.txt" >> "$postinst_file"
echo "" >> "$postinst_file"
echo "exit 0" >> "$postinst_file"

# Make post-installation script executable
chmod +x "$postinst_file"

# Build the .deb package
cd "$tmp_dir"
deb_file="$appname-$version.deb"
dpkg-deb --build "$appname-$version"

cp "$appname-$version.deb" "$script_path"

# Clean up temporary files and directories
rm -rf "$tmp_dir"

echo "The .deb package has been created: $deb_file"
