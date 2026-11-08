# ZeroPoint HID ⚡

**ZeroPoint HID** is a modular, two-stage hardware payload injection and wireless presentation remote built for IT audits, lab testing, and workflow automation. 
Unlike standard all-in-one BadUSB tools, ZeroPoint HID splits the architecture into two microcontrollers: an **ESP32-C3 Super Mini** handling wireless control via Bluetooth Low Energy (BLE), and an **RP2040-Zero** acting purely as a hardware USB HID keyboard.

**IT'S IN BETA PHASE**

---

## 📦 Step-by-Step Guide: From Unboxing to Execution

This complete walkthrough takes you from unboxing your bare microcontrollers to executing your first automated payload from a mobile phone.

### Phase 1: Hardware & Wiring (The Serial Bridge)

When your boards arrive, you need to connect the ESP32-C3 to the RP2040-Zero via a physical UART serial bus so they can talk to each other.

1. **Grab your components:**
   * 1x [ESP32-C3 Super Mini](https://www.espboards.dev/esp32/esp32-c3-super-mini/](https://es.aliexpress.com/item/1005006406538478.html?spm=a2g0o.productlist.main.1.282234b4PnQJxM&algo_pvid=7ea7111b-f060-4fcd-89fd-57aaaeca10f5&algo_exp_id=7ea7111b-f060-4fcd-89fd-57aaaeca10f5-0&pdp_ext_f=%7B%22order%22%3A%2218020%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21EUR%212.67%212.59%21%21%212.92%212.83%21%400b88a95617941531226465499e0ebd%2112000037053726016%21sea%21ES%211795861763%21X%211%210%21n_tag%3A-29919%3Bd%3A4ecd6d46%3Bm03_new_user%3A-29895%3BpisId%3A5000000220915053&curPageLogUid=XLehvkbVkzAE&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006406538478%7C_p_origin_prod%3A))
   * 1x [RP2040-Zero](https://www.waveshare.com/wiki/RP2040-Zero](https://es.aliexpress.com/item/1005008319109364.html?spm=a2g0o.order_list.order_list_main.5.6b53194d1vwkzw&gatewayAdapt=glo2esp))
   * Jumper wires

2. **Cross-wire the UART pins:**
   * **ESP32-C3 GPIO 10 (TX)** ➔ **RP2040-Zero GP5 (RX)** *(Commands sent from ESP32 to RP2040)*
   * **ESP32-C3 GPIO 9 (RX)** ➔ **RP2040-Zero GP4 (TX)** *(Serial feedback)*
   * **GND** ➔ **GND** *(Crucial: Share a common ground)*
   * **5V / 3.3V** ➔ **5V / 3.3V** *(Power rail)*

---

### Phase 2: Flashing the RP2040-Zero (HID Keyboard Core)

The RP2040 acts as the USB keyboard plugged into the target machine.

1. Download the latest [CircuitPython UF2 firmware for RP2040-Zero](https://circuitpython.org/board/waveshare_rp2040_zero/).
2. Press and hold the **BOOT** button on the RP2040-Zero, then plug it into your computer via USB. A virtual drive named `RPI-RP2` will appear.
3. Drag and drop the downloaded UF2 file into the `RPI-RP2` drive. The board will reboot and show up as a drive named `CIRCUITPY`.
4. Download the [Adafruit CircuitPython HID Library Bundle](https://circuitpython.org/libraries) matching your CircuitPython version. Extract it and copy the `adafruit_hid` folder into the `lib/` directory inside your `CIRCUITPY` drive.
5. Copy your custom script (`firmware/rp2040/code.py`) directly into the root of the `CIRCUITPY` drive.

---

### Phase 3: Flashing the ESP32-C3 Super Mini (BLE Controller)

The ESP32-C3 receives commands wirelessly from your mobile browser.

1. Open the `firmware/esp32` directory in **VS Code** using the **PlatformIO** extension.
2. Connect your ESP32-C3 Super Mini via USB to your PC. *(Note: If PlatformIO fails to detect the board during upload, press and hold the onboard **BOOT** button while plugging it in).*
3. Build and flash the firmware using the PlatformIO terminal:
   ```bash
   pio run --target upload
   ```

---

### Phase 4: Setting Up the Web Control Interface (C2)

The web interface runs directly in your mobile browser with zero installation required.

1. Host the `web/index.html` file on any server supporting **HTTPS** (such as GitHub Pages, a local Nginx server with SSL, or a local development server). *Note: HTTPS is strictly required by modern browsers to use the Web Bluetooth API.*
2. Open the URL on your mobile phone browser (Chrome or Edge).
3. Plug your completed hardware assembly (ESP32 + RP2040) into the target computer (Windows, Linux, or macOS).
4. On your mobile phone, tap **"Connect Device"**, select `ZeroPoint_HID` from the browser Bluetooth prompt, and you are ready to go!

---

## 🚀 Features & Usage

* **Presentation Mode:** Huge tactile buttons on your mobile screen to advance slides (`NEXT`), go back (`PREV`), launch full screen (`F5`), or exit (`ESC`).
* **Payload Injector & Compiler:** Upload standard `.txt` DuckyScript payloads (compatible with Flipper Zero syntax). The web interface automatically parses them on-the-fly and streams them securely to the hardware.
* **Interactive Builder:** Easily build custom injection scripts line by line using the web UI block builder (`TXT:`, `KEY:`, `DELAY:`).

---

## 📜 License & Disclaimer

Distributed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.

* **Non-Commercial:** You cannot sell hardware kits or use this project for financial gain.
* **ShareAlike:** Any modification or derivative work must remain open-source under the same terms.

*Disclaimer: This tool is intended strictly for educational purposes, authorized IT security audits, and system administration tasks on hardware you own or have explicit, written permission to test.*
