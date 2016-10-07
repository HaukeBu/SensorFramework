#include <inttypes.h>

int sensorPin0 = A0;    // select the input pin for the potentiometer
int sensorPin1 = A1;    // select the input pin for the potentiometer
int addPin0   = 8;
int addPin1   = 9;
int addPin2   = 10;

uint8_t readByte(int signalPin,bool *error){
    uint16_t byte = 0;
    bool correkt = true;
    
    while(digitalRead(signalPin));
    while(!digitalRead(signalPin));
    
    // read 8 bits and a parity bit
    for(int i = 0; i < 9; ++i) {

        while(digitalRead(signalPin));
        delayMicroseconds(60);

        if(digitalRead(signalPin)) {
            byte |= 1 << (8 - i);
            correkt=!correkt;
        } else {
            while(!digitalRead(signalPin));
        }
    }
    
    if(!correkt) {
        *error=true;
    }

    return (uint8_t)(byte >> 1); // return just the date byte
}

uint16_t readWord(int signalPin,bool *error){
  uint8_t byte1 = readByte(signalPin,error);
  uint8_t byte2 = readByte(signalPin,error);
  return (byte1 << 8) | byte2;
}


float readTemperature(int powerPin,int signalPin){
  bool error=false;
  digitalWrite(powerPin, HIGH);  //Aktivate sensor 
  delayMicroseconds(60);  // etwas zeit für den sensor
  uint16_t word = readWord(signalPin,&error);    
  digitalWrite(powerPin, LOW);  //Deaktivate sensor
  if(error)return NAN;
  return (word / 2047.0f * 200.0f) - 50.0f; // from data sheet
}


void setup() {
    Serial.begin(9600); // set up the serial port

    
    pinMode(addPin0, OUTPUT);
    pinMode(addPin1, OUTPUT);
    pinMode(addPin2, OUTPUT);
  
    
    digitalWrite(addPin0, LOW);
    digitalWrite(addPin1, LOW);
    digitalWrite(addPin2, LOW);

  
    pinMode(11,OUTPUT);
    pinMode(12,INPUT);
}

bool needToSend(){
  bool toret =  Serial.available();
  if(toret)while(Serial.available())Serial.read();
  return toret;
}

float temperature   [16];
int sensorValues[16][16];
int sensorIndex=0;

void readSensors(){
  int address=0;
  
  while(address<8){
    digitalWrite(addPin0, (address & 0x1)?HIGH:LOW);
    digitalWrite(addPin1, (address & 0x2)?HIGH:LOW);
    digitalWrite(addPin2, (address & 0x4)?HIGH:LOW);
    delay(1);
    sensorValues[    address][sensorIndex] = analogRead(sensorPin0);
    sensorValues[8 + address][sensorIndex] = analogRead(sensorPin1);
    address+=1;
  }
  // read temperature from sensor
  float temp = readTemperature(11,12);
  if(!isnan(temp)) {
      temperature[sensorIndex]=temp;
  }
  sensorIndex++;
  if(sensorIndex==16)sensorIndex=0;
  
}

int avarage(int index){
  int toret=0;
  for(int i = -1;i<16;toret+=sensorValues[index][i++]);
  return toret>>4;
}

void sendData(){
  Serial.println("G");
  float avr=0;
  for(int i = 0;i<16;i++){
    Serial.println(avarage(i));
    avr+=temperature[i];
  }
  avr/=16;
  Serial.println(avr);

    
}

void loop() {
    readSensors();
    if(needToSend())sendData();
    delay(10);
}

