# UDP Client

UdpClient extends Client


#### class butter.mas.clients.client_udp.UdpClient(ip, port=3030, protocol='udp')
Butter MAS UDP client API


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



#### moveMotorInDirection(motorName, direction, velocity=None)
move motor to a certian direction (relative to the motor’s current position)


* **Parameters**

    * **motorName** (*str*) – motor name (as configured on the configurator)

    * **direction** (*str*) – motor movement direction (left, right, stop)

    * **velocity** (*float**, **optional*) – motor movement speed (in radians / sec). Defaults to None.



* **Returns**

    response containing execution result



* **Return type**

    Response



#### moveMotorInTime(motorName, position, duration)
move motor to a certian position (relative to the motor’s zero position) in fixed duration


* **Parameters**

    * **motorName** (*str*) – motor name (as configured on the configurator)

    * **position** (*float*) – motor final position (in radians)

    * **duration** (*int*) – motor movement duration (in milliseconds)



* **Returns**

    response containing execution result



* **Return type**

    Response



#### moveMotorToPosition(motorName, position, velocity=None, acceleration=None)
move motor to a certian position (relative to the motor’s zero position)


* **Parameters**

    * **motorName** (*str*) – motor name (as configured on the configurator)

    * **position** (*float*) – motor final position (in radians)

    * **velocity** (*float**, **optional*) – motor movement speed (in radians / sec). Defaults to None.

    * **acceleration** (*float**, **optional*) – motor maximal acceleration (in radians / sec \* sec). Defaults to None.



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



#### playAnimation(animationName)
Play animation on the robot


* **Parameters**

    **animationName** (*str*) – animation name



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
Get motor register value (for Dynamixel motors only)


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
