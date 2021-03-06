from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class PlayListModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlayListModel, self).__init__(*args, *kwargs)
        self.playlist = playlist

    def data(self, index, rl = Qt.DisplayRole):
        if rl == Qt.DisplayRole:
            dt = self.playlist.media(index.row())
            return dt.canonicalUrl().fileName()
    
    def rowCount(self, tt=0):
        return self.playlist.mediaCount()