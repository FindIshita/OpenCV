# include <Wire.h>
# include <Servo.h>
//importing libraries
Servo right_motor;
// Defining the right motor.
Servo left_motor;
//Defining the left motor.
String msg =" testing the serial monitor";
long accelX, accelY, accelZ;
//Created three long type variable which will store the value of accelaration read from the MPU itself.
float gForceX, gForceY, gForceZ;
//This is float type and will store the values of gForces acting in all three directions.
long gyroX, gyroY, gyroZ;
//This will store the raw data read from the gyro in X,Y and Z axis.
float rotX, rotY, rotZ;
//This will store the rotational velocity values in the three axis.
float accel_angle[2];
float gyro_angle[2];
float total_angle[2];
// These will store the values of accelaration angle, gyro angle and the total angle.
float elapsed_time, time_prev, time, pid, pid_p, pid_i, pid_d, pwm_left, pwm_right, error, prev_error;
// These are various variables we defined.
double kp = 3;
double ki = 0.004;
double kd = 3.01;
//These are kp, ki, kd values which will change when I take the actual reading
double throttle = 1300; 
// Initial throttle value of the motor.
float desired_angle = 0;
//We want to system to stabalise at 0 degree.
void setup() {
  Wire.begin();
  //This begins the transmission with the I2C slave. This is required before starting to read or write data.
  Serial.begin(9600);
  //This tells the arduino to prepare to exchange messages at the rate of 9600 bits per second with the monitor.9600 because that is the baud rate.
  right_motor.attach(3);
  //Attach the right motor to pin 3
  left_motor.attach(5);
  //Attach the left motor to pin 5
  time = millis();
  //This starts the counting in miliseconds.
  right_motor.writeMicroseconds(1000);
  //This 1000 here is the minimum of PWM that we send to the ESC.
  left_motor.writeMicroseconds(1000);
  //Same as above
  setupMPU();
  //This is a function we have used in the program further to establish communication with the MPU and to set up the registers which would allow us to read data back from MPU. 
}

void loop() {
  recordAccelRegisters();
  //This function is written below and would record the values from the Accelerometer.
  recordGyroRegisters();
  // This function is written below too and would record the values from gyroscope.
  printData();
  // This would print the data on the screen.
  delay(100);
  // This would create a delay of 100 miliseconds.
}

void setupMPU() {
  Wire.beginTransmission(0b1101000);
  // This is the I2C address of the slave. The end bit depends on the logic level on pin AD0, if it is high then 1 and low then 0.
  Wire.write(0x6B);
  //This is to specify that we are using the 6B register and we want to access it.
  Wire.write(0b00000000);
  //We are writing in the register and we want to set all value to 0 for now becasue we don't want the register to go to sleep mode or use any external clocks etc. 
  Wire.endTransmission();
  //Ending the transmission.
  Wire.beginTransmission(0b1101000);
  //Beginning the trasnmission again
  Wire.write(0x1C);
  //Using the 1C register which is the accelerometer configuration one.
  Wire.write(0b00000000);
  // Setting the values of the accelerometer at +/- 2g.
  Wire.endTransmission();
  //Ending the trasnmission.
  Wire.beginTransmission(0b1101000);
  //Beginning the transmission with the specified slave addresss.
  Wire.write(0x1B);
  //Using the 1B register which is for gyroscope configuration.
  Wire.write(0b00000000);
  //Setting the gyrocope at +/- 250 degree per second (thereby implying that it would be able to detect till 41.6 rpm only with highest sensitivity.
  Wire.endTransmission();
  //Ending the transmission.
}

void recordAccelRegisters() {
  Wire.beginTransmission(0b1101000);
  //The same I2C address of the slave.
  Wire.write(0x3B);
  //Using the 3B register for accelerometer reading
  Wire.endTransmission();
  //Ending the transmission
  Wire.requestFrom(0b1101000,6);
  //We are requesting the slave whose address is given above to provide 6 of the registers 3B (according to datasheet 3B-40)
  while(Wire.available() < 6);
  //Starting a while loop which will run as long as the 6th register is not exceeded.
  accelX = Wire.read()<<8|Wire.read();
  // This means that the the bytes present are ordered in such a way that the first two bytes are stored in the accelX.
  // This is done by using the operator above. Every two bytes of data are read and one of them is the MSB while the other one is the LSB.
  //Using the shift operator the first 8 bits are read and then shifted to the left so that the next 8 bits come to it's position and can be read.
  accelY = Wire.read()<<8|Wire.read();
  //The next two bytes are stored in the accelY using the same process as defined above.
  accelZ = Wire.read()<<8|Wire.read();
  // The last two bytes are stored in the accelZ and the same process is repeated.
  processAccelData();
  //This tells it to jump to the named function.
}

void processAccelData() {
  gForceX = accelX / 16384.0;
  //Calculating the gForce along x direction by dividing the accelerometer reading by the Accel sensitivity corresponding to the full range we chose.
  gForceY = accelY / 16384.0;
  //Doing the same along y direction.
  gForceZ = accelZ / 14384.0;
  //Doing the same along z direction.
  find_accelangle();
  //This tells it to jump to the anmed function.
}

void find_accelangle() {
  accel_angle[0] = atan(gForceY/sqrt(pow (gForceX,2)+ pow(gForceZ,2)))* 180/3.14159;
  accel_angle[1] = atan(-1*gForceX/sqrt(pow(gForceY,2) + pow(gForceZ,2)))*180/3.14159;
}

void recordGyroRegisters() {
  Wire.beginTransmission(0b1101000);
  //The same I2C address of the slave.
  Wire.write(0x43);
  //Using the 43 register for gyroscope reading
  Wire.endTransmission();
  //Ending the transmission
  Wire.requestFrom(0b1101000,6);
  //We are requesting the slave whose address is given above to provide 6 of the registers 3B (according to datasheet 43 - 48)
  while(Wire.available() < 6);
  //Starting a while loop which will run as long as the 6th register is not exceeded.
  accelX = Wire.read()<<8|Wire.read();
  // This means that the the bytes present are ordered in such a way that the first two bytes are stored in the accelX.
  // This is done by using the operator above. Every two bytes of data are read and one of them is the MSB while the other one is the LSB.
  //Using the shift operator the first 8 bits are read and then shifted to the left so that the next 8 bits come to it's position and can be read.
  accelY = Wire.read()<<8|Wire.read();
  //The next two bytes are stored in the accelY using the same process as defined above.
  accelZ = Wire.read()<<8|Wire.read();
  // The last two bytes are stored in the accelZ and the same process is repeated.
  processGyroData();
  //This tells it to jump to the named function.
}

void processGyroData() {
  rotX = gyroX/131.0;
  //This finds the rotational velocity in the x-direction by dividing the gyroscope reading by the gyro sensitivity.
  rotY = gyroY/131.0;
  //This finds the same in Y-direction.
  rotZ = gyroZ/131.0;
  //This finds the same in Z direction.
}


void printData() {
  Serial.println(msg);
  Serial.println("Accel (in 'g')");
  //Prints the words in double quotes
  Serial.print("X =");
  Serial.print(gForceX);
  //Prints the gForceX value on the side of the words within double quotes.
  Serial.print("y =");
  Serial.print(gForceY);
  //Prints the gForceY value on the side of the words within double quotes.
  Serial.print("Z =");
  Serial.print(gForceZ);
  //Prints the gForceZ value on the side of the words within double quotes.
  Serial.print("Gryro (in 'degree')");
  //Prints the words in double quotes.
  Serial.print("X =");
  Serial.print(rotX);
  //Prints the rotX value on the side of the words within double quotes.
  Serial.print("Y =");
  Serial.print(rotY);
  //Prints the rotY value on the side of the words within double quotes.
  Serial.print("Z =");
  Serial.print(rotZ);
  //Prints the rotZ value on the side of the words within double quotes.
}

void sigma_angle() {
  total_angle[0] = 0.98 *(total_angle[0] + gyro_angle[0]*elapsed_time) + 0.02*accel_angle[0];
  total_angle[1] = 0.98 *(total_angle[1] + gyro_angle[1]*elapsed_time) + 0.02*accel_angle[1];
}

void pid_code() {
  error = total_angle[1] - desired_angle;
  //Because the error given in the feedback would be as explained above.
  pid_p = kp*error;
  //The formula we read previously.
  if(-2<error<2)
  {
    pid_i = pid_i + (ki*error);
  }
  //We use if loop here because we want the integral controller to work only when we are close to the set-point within a range of +/- 2 degrees. The function itself is just integrating the values with the previous values.
  pid_d = kd*((error - prev_error)/elapsed_time);
  //As we know the speed is the amount of error that produced in a certain period divided by that time. For thatt we will use a variable called prev_error. We substract that value from the actual error and divide all by the elapsed time. Finally we multiply the result by the derivate constant
  pid = pid_p + pid_i + pid_d;
  if(pid < -1000) {
    pid = -1000;
  }
  if(pid > 1000)
  {
    pid = 1000;
  }
  pwm_left = throttle + pid;
  pwm_right = throttle - pid;
  if(pwm_right < 1000)
  {
    pwm_right = 1000;
  }
  if(pwm_right > 2000)
  {
    pwm_right = 2000;
  }
  if(pwm_left < 1000)
  {
    pwm_left = 1000;
  }
  if(pwm_left > 2000)
  {
    pwm_left = 2000; 
  }
  left_motor.writeMicroseconds(pwm_left);
  right_motor.writeMicroseconds(pwm_right);
  prev_error = error;
}
 
