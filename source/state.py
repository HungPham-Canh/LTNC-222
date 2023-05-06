from abc import ABC


class State(ABC):
    def __init__(self, player):
        self._player = player

    def click_play(self): pass
    def click_lock(self): pass
    def click_next(self): pass
    def click_prev(self): pass


class LockedState(State):
    def click_lock(self):
        if self._player.started and not self._player.paused:
            self._player.change_state(PlayingState(self._player))
        else:
            self._player.change_state(ReadyState(self._player))

    def click_play(self): pass
    def click_next(self): pass
    def click_prev(self): pass


class ReadyState(State):
    def click_lock(self):
        self._player.change_state(LockedState(self._player))

    def click_play(self):
        self._player.play_music()
        self._player.change_state(PlayingState(self._player))

    def click_next(self):
        self._player.next_music()

    def click_prev(self):
        self._player.prev_music()


class PlayingState(State):
    def click_lock(self):
        self._player.change_state(LockedState(self._player))

    def click_play(self):
        self._player.pause_music()
        self._player.change_state(ReadyState(self._player))

    def click_next(self):
        self._player.next_music()
        self._player.play_music()

    def click_prev(self):
        self._player.prev_music()
        self._player.play_music()
