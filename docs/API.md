# Butter MAS HTTP Python API

## class Client(ip, port):
| Param | Type | Default | Description |
| --- | --- | --- | --- |
| ip | <code>string</code> |  | robot server ip. |
| port | <code>integer</code> | <code>5555</code> | robot server port. |

###    getAvailableHandlers(): ⇒ <code>Response</code>
Gets all the available handlers

###    getAvailableAnimations(reload=False): ⇒ <code>Response</code>
Gets all the available animation gestures

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| reload | <code>boolean</code> | <code>false</code> | reload animations. |

###    getAvailableSounds(reload=False): ⇒ <code>Response</code>
Gets all the available audio playbacks

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| reload | <code>boolean</code> | <code>false</code> | reload audio playbacks. |

###    getAvailableMotorRegisters(motorName, readableOnly=False): ⇒ <code>Response</code>
Gets all the available motor registers

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| motorName | <code>string</code> |  | dof motor name. |
| readableOnly | <code>boolean</code> | <code>false</code> | get only readable registers (ignore R/W registers). |

###    getMotorRegister(motorName, registerName): ⇒ <code>Response</code>
Gets motor register value

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| motorName | <code>string</code> |  | dof motor name. |
| registerName | <code>string</code> |  | dof register name. |

###    setMotorRegister(motorName, registerName, value): ⇒ <code>Response</code>
Sets motor register value

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| motorName | <code>string</code> |  | dof motor name. |
| registerName | <code>string</code> |  | dof register name. |
| value | <code>integer</code> |  | dof register value. |

###    playAnimation(animationName): ⇒ <code>Response</code>
Plays animation gesture

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| fileName | <code>string</code> |  | animation name. |

###    pauseAnimation(): ⇒ <code>Response</code>
Pauses animation playback

###    resumeAnimation(): ⇒ <code>Response</code>
Resumes animation playback

###    stopAnimation(): ⇒ <code>Response</code>
Stops animation playback

###    playAudio(fileName): ⇒ <code>Response</code>
Plays audio file

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| fileName | <code>string</code> |  | audio file name. |

###    pauseAudio(): ⇒ <code>Response</code>
Pauses audio playback

###    resumeAudio(): ⇒ <code>Response</code>
Resumes audio playback

###    stopAudio(): ⇒ <code>Response</code>
Stops audio playback
