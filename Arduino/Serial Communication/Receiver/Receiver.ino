char hello[20]; //Initialized variable to store received data

void setup()
{
  Serial.begin(9600);
}

void loop() 
{
  Serial.readBytes(hello,11); //Read the data and store in hello
  Serial.println(hello); //Display on Serial Monitor
  delay(1000);
}
