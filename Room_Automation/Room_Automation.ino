// Uncomment the following line to enable serial debug output
//#define ENABLE_DEBUG

#ifdef ENABLE_DEBUG
  #define DEBUG_ESP_PORT Serial
  #define NODEBUG_WEBSOCKETS
  #define NDEBUG
#endif

#include <Arduino.h>
#ifdef ESP8266
  #include <ESP8266WiFi.h>
#endif
#ifdef ESP32
  #include <WiFi.h>
#endif

#include "SinricPro.h"
#include "SinricProSwitch.h"

#define WIFI_SSID   "DP"
#define WIFI_PASS   "Welcome987*"
#define APP_KEY     "acd95146-df5d-42a9-974a-fc9150ba289c"
#define APP_SECRET  "23cb7947-017d-4dd2-b0c1-9919bc1152ba-39f3f3d7-3e65-45e5-ba28-f07130ee9a41"
#define SWITCH_ID1  "655c5a3ef91e7429522e3dee"
#define SWITCH_ID2  "655c75f6eaee7d403c79d095"
#define SWITCH_ID3  "655c761eeaee7d403c79d0b9"

#define BAUD_RATE         9600
#define EVENT_WAIT_TIME   60000

#ifdef ESP32
  #define RELAY_PIN_1 12
  #define RELAY_PIN_2 14
  #define RELAY_PIN_3 27
#endif

bool deviceIsOn1, deviceIsOn2, deviceIsOn3;
unsigned long lastEvent = (-EVENT_WAIT_TIME);

bool onPowerState(const String &deviceId, bool &state) {
  Serial.printf("Switch %s turned %s (via SinricPro) \r\n", deviceId.c_str(), state ? "on" : "off");

  if (deviceId == SWITCH_ID1) {
    deviceIsOn1 = state;
    digitalWrite(RELAY_PIN_1, state);
  } else if (deviceId == SWITCH_ID2) {
    deviceIsOn2 = state;
    digitalWrite(RELAY_PIN_2, state);
  } else if (deviceId == SWITCH_ID3) {
    deviceIsOn3 = state;
    digitalWrite(RELAY_PIN_3, state);
  }

  return true;
}

void setupWiFi() {
  Serial.printf("\r\n[Wifi]: Connecting");
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.printf(".");
    delay(250);
  }

  IPAddress localIP = WiFi.localIP();
  Serial.printf("connected!\r\n[WiFi]: IP-Address is %d.%d.%d.%d\r\n", localIP[0], localIP[1], localIP[2], localIP[3]);
}

void setupSinricPro() {
  SinricProSwitch& mySwitch1 = SinricPro[SWITCH_ID1];
  SinricProSwitch& mySwitch2 = SinricPro[SWITCH_ID2];
  SinricProSwitch& mySwitch3 = SinricPro[SWITCH_ID3];

  mySwitch1.onPowerState(onPowerState);
  mySwitch2.onPowerState(onPowerState);
  mySwitch3.onPowerState(onPowerState);

  SinricPro.onConnected([]() { Serial.printf("Connected to SinricPro\r\n"); });
  SinricPro.onDisconnected([]() { Serial.printf("Disconnected from SinricPro\r\n"); });
  SinricPro.begin(APP_KEY, APP_SECRET);
}

void setup() {
  Serial.begin(BAUD_RATE);
  Serial.printf("\r\n\r\n");

  pinMode(RELAY_PIN_1, OUTPUT);
  pinMode(RELAY_PIN_2, OUTPUT);
  pinMode(RELAY_PIN_3, OUTPUT);

  SinricProSwitch& mySwitch1 = SinricPro[SWITCH_ID1];
  SinricProSwitch& mySwitch2 = SinricPro[SWITCH_ID2];
  SinricProSwitch& mySwitch3 = SinricPro[SWITCH_ID3];

  mySwitch1.onPowerState(onPowerState);
  mySwitch2.onPowerState(onPowerState);
  mySwitch3.onPowerState(onPowerState);

  setupWiFi();
  setupSinricPro();
}

void loop() {
  SinricPro.handle();
}
