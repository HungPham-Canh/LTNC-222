from tkinter import filedialog
from tkinter import *
import os
import pygame
from state import ReadyState


class AudioPlayer:
    def __init__(self, ui):
        self.songs = []
        self.current_song = ""
        self.paused = False
        self.started = False
        self.ui = ui
        self.state = ReadyState(self)

    def change_state(self, state):
        self.state = state

    def click_lock(self):
        self.state.click_lock()

    def click_play(self):
        self.state.click_play()

    def click_prev(self):
        self.state.click_prev()

    def click_next(self):
        self.state.click_next()

    def load_songs(self):
        self.ui.root.directory = filedialog.askdirectory()

        for song in os.listdir(self.ui.root.directory):
            name, ext = os.path.splitext(song)
            if ext == '.mp3':
                self.songs.append(song)

        for song in self.songs:
            self.ui.songlist.insert("end", song)

        self.ui.songlist.selection_set(0)
        self.current_song = self.songs[self.ui.songlist.curselection()[0]]
        self.load_music()

    def load_music(self):
        pygame.mixer.music.load(os.path.join(
            self.ui.root.directory, self.current_song))
        self.started = False
        self.paused = False

    def pause_music(self):
        try:
            pygame.mixer.music.pause()
            self.paused = True
        except:
            print("Error pausing music")

    def play_music(self):
        try:
            if not self.started:
                pygame.mixer.music.play()
                self.started = True
            elif self.paused:
                pygame.mixer.music.unpause()
                self.paused = False

        except:
            print("error while playing")

    def next_music(self):
        try:
            self.ui.songlist.selection_clear(0, END)
            self.ui.songlist.selection_set(
                self.songs.index(self.current_song) + 1)
            self.current_song = self.songs[self.ui.songlist.curselection()[0]]
            self.load_music()
        except:
            print("Error next music")

    def prev_music(self):
        try:
            self.ui.songlist.selection_clear(0, END)
            self.ui.songlist.select_set(
                self.songs.index(self.current_song) - 1)
            self.current_song = self.songs[self.ui.songlist.curselection()[
                0]]
            self.load_music()
        except:
            print("Error prev music")
