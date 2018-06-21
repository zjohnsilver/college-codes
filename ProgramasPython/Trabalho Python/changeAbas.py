from tkinter import *


def raise_frame(frame):
    frame.tkraise()

root = Tk()

frames ={}

for x in range(1, 5):
	frames['f%i'%(x)] = Frame(root)



for frame in frames.values():
    frame.grid(row=0, column=0, sticky='news')

Button(frames['f1'], text='Go to frame 2', command=lambda	:raise_frame(frames['f2'])).pack()
Label(frames['f1'], text='FRAME 1').pack()

Label(frames['f2'], text='FRAME 2').pack()
Button(frames['f2'], text='Go to frame 3', command=lambda:raise_frame(frames['f3'])).pack()

Label(frames['f3'], text='FRAME 3').pack(side='left')
Button(frames['f3'], text='Go to frame 4', command=lambda:raise_frame(frames['f4'])).pack(side='left')

Label(frames['f4'], text='FRAME 4').pack()
Button(frames['f4'], text='Goto to frame 1', command=lambda:raise_frame(frames['f1'])).pack()

raise_frame(frames['f1'])
root.mainloop()