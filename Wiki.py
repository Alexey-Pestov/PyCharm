import  wikipedia
import tkinter

def wiki(event):
    title = wikipedia.random()
    try:
        page = wikipedia.summary(title)
    except wikipedia.DisambiguationError:
        print('ERROR')
        #wiki(event)
        

    #print(len(page))
    #print((page))
    x = 75 # длина строки
    if len(page) < x:
        lbl.config(text=page)
    else:
        n = len(page)
        while True:
            m = page[n-x:].find(' ')
            page = page[:n-x+m] + '\n' + page[n-x+m+1:len(page)]
            n = n - x + m
            #print((page))
            #rint(len(page))
            #print(n, m)
            if n < x:
                break
        lbl.config(text=page)

wikipedia.set_lang('ru')

root = tkinter.Tk()
root.title('Wiki API')
root.geometry('600x600')

lbl = tkinter.Label(root, text='Получи статью с Wikipedia')
lbl.pack()

btn = tkinter.Button(root, text='Случайная статья')
btn.pack()
btn.bind('<Button-1>', wiki)


root.mainloop()