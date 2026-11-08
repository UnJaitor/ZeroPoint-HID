#include <Arduino.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>

BLEServer *pServer = NULL;
BLECharacteristic *pRxCharacteristic = NULL;
bool deviceConnected = false;
String receivedData = "";
bool newDataAvailable = false;

#define SERVICE_UUID           "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
#define CHARACTERISTIC_UUID_RX "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
#define CHARACTERISTIC_UUID_TX "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) { deviceConnected = true; }
    void onDisconnect(BLEServer* pServer) { 
        deviceConnected = false; 
        pServer->getAdvertising()->start();
    }
};

class MyCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {

      String value = pCharacteristic->getValue();
      
      value.trim();
      
      if (value.length() > 0) {
        receivedData = value;
        newDataAvailable = true;
      }
    }
};

void setup() {
  Serial.begin(115200);

  Serial1.begin(115200, SERIAL_8N1, 9, 10);

  BLEDevice::init("ZeroPoint_HID");
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());

  BLEService *pService = pServer->createService(SERVICE_UUID);
  pService->createCharacteristic(CHARACTERISTIC_UUID_TX, BLECharacteristic::PROPERTY_NOTIFY);
  
  pRxCharacteristic = pService->createCharacteristic(CHARACTERISTIC_UUID_RX, BLECharacteristic::PROPERTY_WRITE);
  pRxCharacteristic->setCallbacks(new MyCallbacks());

  pService->start();
  pServer->getAdvertising()->start();
}

void loop() {
  if (newDataAvailable) {
    newDataAvailable = false;
    
    Serial.print("Enviando al RP2040: ");
    Serial.println(receivedData);
    
    Serial1.println(receivedData);
  }
}


// By: UnJaitor 
// https://github.com/UnJaitor


// Distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.
// Non-Commercial: You cannot sell hardware kits or use this project for financial gain.
// ShareAlike: Any modification or derivative work must remain open-source under the same terms.