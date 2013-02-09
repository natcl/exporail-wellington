
void setup()
{
	int i;
	for (i = 3 ; i<70 ; i++)
	{
		pinMode(i, OUTPUT);
	}
}

void loop()
{
	int i;
	for (i = 3 ; i<70 ; i++)
	{
		digitalWrite(i, HIGH);   // sets the LED on
  		delay(200);                  // waits for a second
  		digitalWrite(i, LOW);    // sets the LED off
	}
}
