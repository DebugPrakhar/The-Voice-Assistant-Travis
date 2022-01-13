import pyttsx3
import operator
import speech_recognition as s_r
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

try:
   r = s_r.Recognizer()
   my_mic_device = s_r.Microphone(device_index=1)
   with my_mic_device as source:
       print("Say what you want to calculate, example: 5 plus 8")
       speak("Say what you want to calculate, example: 5 plus 8")
       print("Listening...")
       r.adjust_for_ambient_noise(source, duration=1)
       audio = r.listen(source)
   my_string=r.recognize_google(audio)
   speak("The result is")
   print(my_string)
   def get_operator_fn(op):
       return {
           '+' : operator.add,
           '-' : operator.sub,
           'x' : operator.mul,
           'divided' :operator.__truediv__,
           'Mod' : operator.mod,
           'mod' : operator.mod,
           '^' : operator.xor,
           }[op]
   def eval_binary_expr(op1, oper, op2):
       op1,op2 = int(op1), int(op2)
       return get_operator_fn(oper)(op1, op2)  
   speak(eval_binary_expr(*(my_string.split())))
   print("The result is")
   print(eval_binary_expr(*(my_string.split())))

except Exception as e:
    speak("Sir, Please try again I cannot recognised that properly")