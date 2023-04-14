
import cv2
import time
# Set delay time in seconds
delay = 2

# Delay for specified time
time.sleep(delay)

# Open default camera
webCam = cv2.VideoCapture(0)

# Read a single frame
success, frame = webCam.read()

# Check if frame was read successfully
if success:
	cv2.imwrite('frame1.jpg', frame)
	# cv2.imshow('Frame', frame)

# cv2.waitKey(0)

# Release camera resources
webCam.release()
cv2.destroyAllWindows()

#detect emotion
import cv2
img=cv2.imread('frame1.jpg')
from pprint import pprint
import matplotlib.pyplot as plt
plt.imshow(img)
from deepface import DeepFace
plt.imshow (cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
predictions=DeepFace.analyze(img)
print(f"The dominant emotion is {predictions[0]['dominant_emotion']}")



#Action of Speaking bot according to emotion of user
import openai
import pyttsx3
import speech_recognition as sr
import time
# Set your OpenAI API key
openai.api_key="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"
# Initialize the text-to-speech engine
engine=pyttsx3.init()

def transcribe_audio_to_text(filename):
	recognizer=sr.Recognizer()
	with sr.AudioFile(filename) as source:
		audio = recognizer.record(source)
	try:
		return recognizer.recognize_google(audio)
	except:
		print("Skipping unknown error")

def generate_response(prompt):
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=prompt,
		max_tokens=4000,
		n=1,
		stop=None,
		temperature=0.5,
	)
	return response["choices"][0]["text"]

def speak_text (text):
	engine.say(text)
	engine.runAndWait()

if predictions[0]['dominant_emotion']!="happy":
    text = "I am an autistic child trying to focus on my vocational subject coures video and i am feeling {predictions[0]['dominant_emotion']}. Please tell me or suggest me something stay foccused"
    response = generate_response (text)
    print (f"GPT-3 says: {response}")
    speak_text(response)

# animative action to be taken according to the emotion user

if predictions[0]['dominant_emotion'].lower()=="anger":
	print("Angry")
elif predictions[0]['dominant_emotion'].lower()=="fear":
	print("Happy")
elif predictions[0]['dominant_emotion'].lower() == "disgust":
	print("Disgust")
elif predictions[0]['dominant_emotion'].lower()=="sad":
	print("sad")
elif predictions[0]['dominant_emotion'].lower() == "surprise":
	print("Surprise")
elif predictions[0]['dominant_emotion'].lower()=="neutral":
	print("Neutral")
elif predictions[0]['dominant_emotion'].lower() == "contempt":
	print("contempt")




