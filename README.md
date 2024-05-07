# networkscannerpy
This Python script utilizes the Scapy library to perform a network scan and identify devices connected to the same local network. Additionally, it includes malicious traffic detection to identify devices with suspicious behaviors.

## Requirements
- Python 3.x
- Scapy

## Installation
- Ensure you have Python 3 installed on your system.
- Install the Scapy library by running the following command:
```bash
pip install scapy
```

## Usage
1. Clone or download the repository locally.
2. Open a terminal and navigate to the directory containing the script (networkscanner.py).
3. Run the script by executing the following command:
```bash
python networkscanner.py
```
4. The script will prompt you to input the IP range you want to scan (e.g., 192.168.1.1/24).
5. Once the scan is complete, the script will display the scanned devices along with any suspicious devices detected.

## Customization
You can customize the script by modifying the <b>scan function</b> to include additional malicious traffic detection logic or by adjusting the output format in the <b>print_result</b> and <b>print_suspicious_devices</b> functions.

## Example
```bash
python networkscanner.py
```

## License
This project is licensed under the MIT License - see the <a href="https://opensource.org/license/mit">LICENSE</a> file for details.