# ZeroPoint HID ⚡

**ZeroPoint HID** is an open-source, two-stage hardware payload injection and presentation control platform designed for IT security audits, infrastructure testing, and automated workflows. 

Unlike traditional all-in-one BadUSB devices, ZeroPoint HID separates the wireless reception layer from the USB Human Interface Device (HID) emulation layer, ensuring high stability, modularity, and precise timing control.

---

## 🚀 Architecture

The system is decoupled into three independent layers:
1. **Web Control Center (C2):** A responsive, mobile-first Single Page Application (SPA) utilizing the Web Bluetooth API. It features a full-screen presentation remote and an in-browser DuckyScript compiler.
2. **BLE Receiver (ESP32-C3):** Acts as a secure BLE server, receiving commands from the mobile interface and forwarding them via a physical high-speed UART link.
3. **HID Injector (Raspberry Pi RP2040):** Runs CircuitPython to interpret incoming serial data and emulate a universal, hardware-level USB keyboard across Windows, Linux, and macOS.

---

## 🛠️ Hardware Requirements & Pinout

* **1x ESP32-C3** development board (BLE/Wi-Fi Controller)
* **1x Raspberry Pi RP2040** (e.g., RP2040-Zero, acting as the USB HID Device)

### Physical UART Wiring:
| ESP32-C3 Pin | Function | RP2040 Pin | Function |
| :--- | :--- | :--- | :--- |
| **Pin 10** | TX (Transmit) | **GP5** | RX (Receive) |
| **Pin 9** | RX (Receive) | **GP4** | TX (Transmit) |
| **GND** | Ground | **GND** | Ground |

---

## 💻 Installation & Setup

### 1. ESP32-C3 Firmware (PlatformIO)
Open the `firmware/esp32` folder in VSCode with the PlatformIO extension. Ensure your `platformio.ini` includes USB CDC flags if required, then compile and flash:
```bash
pio run --target upload
```

### 2. RP2040 Firmware (CircuitPython)
1. Flash **CircuitPython** onto your RP2040.
2. Download and place the `adafruit_hid` library inside the `lib/` folder on your `CIRCUITPY` drive.
3. Copy the contents of `firmware/rp2040/code.py` to the root of the drive.

### 3. Web Control Interface
Because the Web Bluetooth API requires a secure context, host the `web/index.html` file on an **HTTPS** server (such as GitHub Pages or a local proxy). Open the URL on a compatible mobile browser (like Chrome for Android), tap **"Vincular Dispositivo"**, and select `ZeroPoint_HID`.

---

## 📜 License

This project is distributed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.

You are free to **share** and **adapt** the material under the terms of proper **attribution**, **non-commercial** use, and **share-alike** conditions. See the [LICENSE](LICENSE) file for full details.
