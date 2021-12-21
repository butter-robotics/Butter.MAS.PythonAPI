# TCP Client

TcpClient extends Client


### class butter.mas.clients.client_tcp.TcpClient(ip, port=3003, protocol='tcp')
Butter MAS TCP client API


#### clearAnimation()
Clear animation queue (if available)


* **Returns**

    response containing execution result



* **Return type**

    Response



#### getAvailableAnimations(reload=False)
Get available (loaded) robot animations


* **Parameters**

    **reload** (*bool**, **optional*) – reload all animations. Defaults to False.



* **Returns**

    response containing all the available (loaded) robot animations



* **Return type**

    Response



#### getAvailableHandlers()
Get available robot handlers


* **Returns**

    response containing all the available robot handlers



* **Return type**

    Response



#### getAvailableMotorRegisters(motorName, readableOnly=False)
Get all available motor registers (for Dynamixel motors only)


* **Parameters**

    
    * **motorName** (*str*) – motor name (as configured on the configurator)


    * **readableOnly** (*bool**, **optional*) – get readable registers only. Defaults to False.



* **Returns**

    response containing all the available motor registers



* **Return type**

    Response



#### getAvailableSounds(reload=False)
Get available (loaded) robot sound assets


* **Parameters**

    **reload** (*bool**, **optional*) – reload all sound assets. Defaults to False.



* **Returns**

    response containing all the available (loaded) robot sound assets



* **Return type**

    Response



#### getMotorRegister(motorName, registerName)
Get motor register value (for Dynamixel motors only)


* **Parameters**

    
    * **motorName** (*str*) – motor name (as configured on the configurator)


    * **registerName** (*str*) – motor register name



* **Returns**

    response containing register value



* **Return type**

    Response



#### getMotorRegisterRange(motorName, registerName)
Get motor register value range (for Dynamixel motors only)


* **Parameters**

    
    * **motorName** (*str*) – motor name (as configured on the configurator)


    * **registerName** (*str*) – motor register name



* **Returns**

    response containing register range value



* **Return type**

    Response



#### moveMotorInDirection(motorName, direction, velocity=None, units=RotationUnits.RADIANS)
move motor to a certain direction (relative to the motor’s current position)


* **Parameters**

    
    * **motorName** (*str*) – motor name (as configured on the configurator)


    * **direction** (*str*) – motor movement direction (left, right, stop)


    * **velocity** (*float**, **optional*) – motor movement speed (in units / sec). Defaults to None.


    * **units** (*RotationUnits**, **optional*) – rotation units. Defaults to ‘radians’.



* **Returns**

    response containing execution result



* **Return type**

    Response



#### moveMotorInTime(motorName, position, duration, units=RotationUnits.RADIANS)
move motor to a certain position (relative to the motor’s zero position) in fixed duration


* **Parameters**

    
    * **motorName** (*str*) – motor name (as configured on the configurator)


    * **position** (*float*) – motor final position (in units)


    * **duration** (*int*) – motor movement duration (in milliseconds)


    * **units** (*RotationUnits**, **optional*) – rotation units. Defaults to ‘radians’.



* **Returns**

    response containing execution result



* **Return type**

    Response



#### moveMotorToPosition(motorName, position, velocity=None, acceleration=None, units=RotationUnits.RADIANS)
move motor to a certain position (relative to the motor’s zero position)


* **Parameters**

    
    * **motorName** (*str*) – motor name (as configured on the configurator)


    * **position** (*float*) – motor final position (in units)


    * **velocity** (*float**, **optional*) – motor movement speed (in units / sec). Defaults to None.


    * **acceleration** (*float**, **optional*) – motor maximal acceleration (in units / sec \* sec). Defaults to None.


    * **units** (*RotationUnits**, **optional*) – rotation units. Defaults to ‘radians’.



* **Returns**

    response containing execution result



* **Return type**

    Response



#### pauseAnimation()
Pause currently playing animation (if available) on the robot


* **Returns**

    response containing execution result



* **Return type**

    Response



#### pauseAudio()
Pause current audio playback (if available) on the robot


* **Returns**

    response containing execution result



* **Return type**

    Response



#### playAnimation(animationName, lenient=False, relative=False)
Play animation on the robot


* **Parameters**

    
    * **animationName** (*str*) – animation name


    * **lenient** (*bool**, **optional*) – wait for current playing animation (if present) to finish . Defaults to False.


    * **relative** (*bool**, **optional*) – play animation relative to the current robot position. Defaults to False.



* **Returns**

    response containing execution result



* **Return type**

    Response



#### playAudio(fileName)
Play audio on the robot


* **Parameters**

    **fileName** (*str*) – audio asset name



* **Returns**

    response containing execution result



* **Return type**

    Response



#### resumeAnimation()
Resume currently paused animation (if available) on the robot


* **Returns**

    response containing execution result



* **Return type**

    Response



#### resumeAudio()
Resume currently paused audio playback (if available) on the robot


* **Returns**

    response containing execution result



* **Return type**

    Response



#### setMotorRegister(motorName, registerName, value)
Set motor register value (for Dynamixel motors only)


* **Parameters**

    
    * **motorName** (*str*) – motor name (as configured on the configurator)


    * **registerName** (*str*) – motor register name


    * **value** (*str*) – register value



* **Returns**

    response containing execution result



* **Return type**

    Response



#### stopAnimation()
Stop currently playing animation (if available) on the robot


* **Returns**

    response containing execution result



* **Return type**

    Response



#### stopAudio()
Stop current audio playback (if available) on the robot


* **Returns**

    response containing execution result



* **Return type**

    Response



#### property timeout()
Get command execution timeout


* **Returns**

    command execution timeout in milliseconds



* **Return type**

    integer
