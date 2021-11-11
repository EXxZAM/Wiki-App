from tkinter import *
import tkinter.scrolledtext as scrolledtext
import wikipedia
import pyttsx3
import pygame
import pyperclip
import webbrowser

app = Tk()
app.title('Wiki-App')
app.geometry('400x300')
app.resizable(0,0)
background_color = '#121212'
app.config(bg=background_color)
pygame.init()
pauseStatus = False
stopStatus = False
#? Functions

def change_look():
    global background_color
    if background_color == '#121212':
        background_color = '#1F1B24'
        app.config(bg=background_color)
        searchEntry.configure(bg=background_color, fg='white')
        searchButton.configure(bg=background_color, fg='white')
        pauseButton.configure(bg=background_color, fg='white')
        stopButton.configure(bg=background_color, fg='white')
        copyButton.configure(bg=background_color, fg='white')
        webButton.configure(bg=background_color, fg='white')
        wikiResult.configure(bg=background_color, fg='white')
    else:
        background_color = '#121212'
        app.config(bg=background_color)
        searchEntry.configure(bg=background_color, fg='white')
        searchButton.configure(bg=background_color, fg='white')
        pauseButton.configure(bg=background_color, fg='white')
        stopButton.configure(bg=background_color, fg='white')
        copyButton.configure(bg=background_color, fg='white')
        webButton.configure(bg=background_color, fg='white')
        wikiResult.configure(bg=background_color, fg='white')


def search():
    global pauseStatus
    global wikiSearch
    global searchItem
    searchItem = searchEntry.get()
    wikiSearch = wikipedia.summary(searchItem, sentences=5)
    wikiResult.delete('1.0','end')
    wikiResult.insert(INSERT, wikiSearch)

    pauseButton.config(text='Pause')
    stopButton.config(text='Stop')
    pauseStatus = False
    stopStatus = False

    pygame.mixer.music.unload()
    engine = pyttsx3.init()
    engine.save_to_file(wikiSearch, 'wikiresult.wav')
    engine.runAndWait()
    
    pygame.mixer.music.load('wikiresult.wav')
    pygame.mixer.music.play(0)


    pauseButton.config(state='normal')
    stopButton.config(state='normal')
    copyButton.config(state='normal')
    webButton.config(state='normal')



def pause():
    global pauseStatus
    if pauseStatus == False:
        pygame.mixer.music.pause()
        pauseStatus = True
        pauseButton.config(text='Unpause')
    else:
        pygame.mixer.music.unpause()
        pauseStatus = False
        pauseButton.config(text='Pause')

def stop():
    global stopStatus
    global pauseStatus
    if stopStatus == False:
        pygame.mixer.music.stop()
        stopStatus = True
        stopButton.config(text='Play')
        pauseStatus = False
        pauseButton.config(text='Pause')
    else:
        pygame.mixer.music.play(0)
        stopStatus = False
        stopButton.config(text='Stop')


def copy():
    pyperclip.copy(wikiSearch)


def open_browser():
    webbrowser.open(wikipedia.page(searchItem).url)



#? menu-Bar
menubar = Menu(app)
menubar.add_command(label='Theme', command=change_look)
app.config(menu=menubar)


#? entry-Search
searchEntry = Entry(app, width=30, font=('arial',12) )
searchEntry.place(relx=0.05, rely=0.05)

#? button-Search
searchButton = Button(app, width=10, text="Search",command=search )
searchButton.place(relx=0.75, rely=0.05)

#? Pause-Button
pauseButton = Button(app, width=10, text="Pause", command=pause )
pauseButton.place(relx=0.05, rely=0.15)

#? Stop-Button
stopButton = Button(app, width=10, text="Stop", command=stop )
stopButton.place(relx=0.26, rely=0.15)

#? Copy-Button
copyButton = Button(app, width=10, text="Copy", command=copy )
copyButton.place(relx=0.47, rely=0.15)

#? web-Button
webButton = Button(app, text="Read on Wikipedia", command=open_browser)
webButton.place(relx=0.68, rely=0.15)

#? result-Text
wikiResult = scrolledtext.ScrolledText(app, height=12, width=44, padx=10, font=('Arial'))
wikiResult.pack(pady=(80,0))


#? Changing Colors
searchEntry.configure(bg=background_color, fg='white')
searchButton.configure(bg=background_color, fg='white')
pauseButton.configure(bg=background_color, fg='white', state='disabled')
stopButton.configure(bg=background_color, fg='white', state='disabled')
copyButton.configure(bg=background_color, fg='white', state='disabled')
webButton.configure(bg=background_color, fg='white', state='disabled')
wikiResult.configure(bg=background_color, fg='white')

app.mainloop()