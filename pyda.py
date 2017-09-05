import wx
import wikipedia
import wolframalpha
import pyttsx
import speech_recognition as sr

engine = pyttsx.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-15)
engine.say('welcome sir ugo')
engine.say('what can i help you with?')
engine.runAndWait()

#set a main class for the app frame
class MyFrame(wx.Frame):
    def __init__(self):        
        #set some basic gui info about the app
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Bruce v1")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, 
        label="Hello I am Bruce the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        #set up a simple text box with the following properties
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()    

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()

        #if input field is empty, try to get users speech
        if input == '':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service;{0}".format(e))
        
        else:            
            try:
                #wolframalpha:
                app_id = "Q2HXJ5-GYYYX6PYYP"
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text 
                print(answer)
                say("The answer is '" +answer+ "' ")
                
            except:
                #wikipedia:
                '''
                making the app more intuitive
                1. we take the input and divide every word into its own separate string
                2. after that, we take out the first two words of that string and leave 
                the rest to be the input
                '''
                input = input.split(' ')            # ~ split input by spacing
                input = " ".join(input[2:])         # ~ join it, except for the first two words
                print(wikipedia.summary(input))
                say("Searching for "+input)
                summary = wikipedia.summary(input)
                say(" '" +summary+ "' ")

def say(text):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+10)
    engine.say(text)
    engine.runAndWait()

#run the app with the below code
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()



