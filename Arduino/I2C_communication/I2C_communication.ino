#include<Wire.h>;
const int MPUadd = 0x68;
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
void setup() 
{
  Serial.begin(9600);
  Wire.begin();
  Wire.beginTransmission(MPUadd);
  Wire.write(0x6B);
  Wire.write(0x00);
  Wire.endTransmission(true);
  delay(50);
}
void loop() 
{
  Wire.beginTransmission(MPUadd);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPUadd, 14, true);
  AcX = Wire.read()<<8 | Wire.read();
  AcY = Wire.read()<<8 | Wire.read();
  AcZ = Wire.read()<<8 | Wire.read(); 
  Tmp = Wire.read()<<8 | Wire.read();
  GyX = Wire.read()<<8 | Wire.read();
  GyY = Wire.read()<<8 | Wire.read();
  GyZ = Wire.read()<<8 | Wire.read();
  Serial.print("AcX="); 
  Serial.println(AcX);
  Serial.print("AcY="); 
  Serial.println(AcY);
  Serial.print("AcZ="); 
  Serial.println(AcZ);
  Serial.print("Temp="); 
  Serial.println(Tmp);
  Serial.print("GyX="); 
  Serial.println(GyX);
  Serial.print("GyY="); 
  Serial.println(GyY);
  Serial.print("GyZ="); 
  Serial.println(GyZ);
  delay(500);
}
