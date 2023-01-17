import string
from tkinter import filedialog
import os
import speech_recognition as s
from io import TextIOWrapper


class File_Model:

    def __init__(self):
        self.url = ""
        self.key = string.ascii_letters+''.join([str(x) for x in range(0, 10)])
        self.offset=5

    def encrypt(self,plaintext):
        result=""
        for ch in plaintext:
            try:
                ind=self.key.index(ch)
                ind=(ind+self.offset)%62
                result+=self.key[ind]
            except ValueError:
                result+=ch
        return result

    def decrypt(self,ciphertext):
        result=""
        for ch in ciphertext:
            try:
                ind=self.key.index(ch)
                ind=(ind-self.offset)%62
                result+=self.key[ind]
            except ValueError:
                result+=ch
        return result

    def open_file(self):
        self.url=filedialog.askopenfilename(title="select file",filetypes=[("Text Documents","*.*")])

    def new_file(self):
        self.url = ""

    #def save_as(self,msg):
        #enc_text=self.encrypt(msg)
        #self.url=filedialog.asksaveasfile(mode="w",defaultextention=".ntxt",filetypes=[("")])
        #self.url.write(enc_text)

        #filepath = self.url.name
        #self.url.close()
        #self.url = filepath

    def save_file(self, msg):

        if self.url == "":
            self.url = filedialog.asksaveasfilename(title='Select File', defaultextension='.ntxt',
                                                    filetypes=[("Text Documents", "*.*")])
        filename, file_extension = os.path.splitext(self.url)
        content = msg
        if file_extension in '.ntxt':
            content = self.encrypt(content)
        with open(self.url, 'w', encoding='utf-8') as fw:
            fw.write(content)

    def read_file(self, url=''):
        if url != '':
            self.url = url
        else:
            self.open_file()
        base = os.path.basename(self.url)
        file_name, file_extension = os.path.splitext(self.url)
        fr = open(self.url, "r")
        contents = fr.read()
        if file_extension == '.ntxt':
            contents = self.decrypt(contents)
        fr.close()
        return contents, base
    def takeQuery(self):
        sr=s.Recognizer()
        sr.pause_threshold = 1
        print("Speak")
        with s.Microphone() as m:
            # sr.adjust_for_ambient_noise(m)
            audio=sr.listen(m)
            query = sr.recognize_google(audio)
            return query

    def save_as(self, msg):

        content = msg
        encrypted = self.encrypt(content)

        self.url = filedialog.asksaveasfile(mode='w', defaultextension='.ntxt',
                                            filetypes=([("All Files", "*.*"), ("Text Documents", "*.txt")]))
        self.url.write(encrypted)

        filepath = self.url.name
        self.url.close()
        self.url = filepath
#obj=File_Model()
#plaintext="BHOPAL"
#cipher=obj.encrypt(plaintext)
#print(cipher)
#print(obj.decrypt(cipher))



