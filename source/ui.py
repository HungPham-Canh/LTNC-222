import pygame
from tkinter import *
from audioplayer import AudioPlayer


class UI:
    def __init__(self):
        # init application
        self.root = Tk()
        self.root.title('Music Player')
        self.root.geometry("500x300")
        self.auplr = AudioPlayer(self)
        # init player
        pygame.mixer.init()

        # init menubar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        organise_menu = Menu(menubar, tearoff=False)
        organise_menu.add_command(
            label='Select Folder', command=self.auplr.load_songs)
        menubar.add_cascade(label='Organise', menu=organise_menu)

        self.songlist = Listbox(self.root, bg="black",
                                fg="white", width=100, height=15)
        self.songlist.pack()

        # import images
        play_btn_image = PhotoImage(file='img/play.png')
        lock_btn_image = PhotoImage(file='img/lock.png')
        next_btn_image = PhotoImage(file='img/next.png')
        prev_btn_image = PhotoImage(file='img/previous.png')

        control_frame = Frame(self.root)
        control_frame.pack()

        # init buttons
        play_btn = Button(control_frame, image=play_btn_image,
                          borderwidth=0, command=self.auplr.click_play)
        lock_btn = Button(control_frame, image=lock_btn_image,
                          borderwidth=0, command=self.auplr.click_lock)
        next_btn = Button(control_frame, image=next_btn_image,
                          borderwidth=0, command=self.auplr.click_next)
        prev_btn = Button(control_frame, image=prev_btn_image,
                          borderwidth=0, command=self.auplr.click_prev)

        play_btn.grid(row=0, column=1, padx=7, pady=10)
        lock_btn.grid(row=0, column=2, padx=7, pady=10)
        next_btn.grid(row=0, column=3, padx=7, pady=10)
        prev_btn.grid(row=0, column=0, padx=7, pady=10)

        self.root.mainloop()
