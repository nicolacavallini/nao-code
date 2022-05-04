from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.12.103", 9559)
tts.say("Hello, world!")
