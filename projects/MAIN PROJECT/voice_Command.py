import os
import time
import speech_recognition as sr

def getaud():
    r = sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Please wait. Calibrating microphone...")  
    # listen for 5 seconds and create the ambient noise energy level  
        r.adjust_for_ambient_noise(source, duration=5)  
        print("Say something!")  
        audio = r.listen(source)  
    
    # recognize speech using google  
    try:  
        text = r.recognize_google(audio,language="en-US")
        print("SR thinks you said '" + text + "'")  
    except sr.UnknownValueError:  
        print("SR could not understand audio")  
    except sr.RequestError as e:  
        print("SR error; {0}".format(e))
        
    return text.lower()


# To specify the shape name with the voice command
def audioFilter(text):
    try:
        if text.count('prism'):
            return '2','prism'
        elif text.count('cuboid'):
            return '0','cuboid'
        elif text.count('cylinder'):
            return '1','cyclinder'
        else:
            pass
    except:
        audioFilter(text)


# starting of the program
if __name__ == '__main__':

    shape_name = getaud()
    text = audioFilter(shape_name)
    print(f"Detecting shape: {text[1]}")
    
    command = "python detect2.py --weights runs/train/3D_Shapes1/weights/best.pt --class {txt} --source 0".format(txt = text[0])
    
    command2 = 'cmd /k \"{cmd}\"'.format(cmd = command)
    #print(command2)
    
    os.system(command2)
