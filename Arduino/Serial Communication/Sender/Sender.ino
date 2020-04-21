char hello[11] = "Hello World"; 

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  Serial.write(hello,11); //Write the serial data
  delay(1000);
}
