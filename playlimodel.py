from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import database as db 

class PlaylistListModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(PlaylistListModel, self).__init__(*args, *kwargs)
        self._data = db.get_playlists()

    def updateData(self):
        self.layoutAboutToBeChanged.emit()
        self._data = db.get_playlists()
        self.layoutChanged.emit()

    def getid(self, index):
        return self._data[index.row()][0]
    def data(self, index, rl = Qt.DisplayRole):
        if rl == Qt.DisplayRole:
            return self._data[index.row()][1]
        
    def rowCount(self, tt=0):
        return len(self._data)
