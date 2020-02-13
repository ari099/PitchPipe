import sys, string
from PyQt5 import QtWidgets, uic
from synthesizer import Player, Synthesizer, Waveform

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('pitch_pipe_ui.ui', self)

      # Set up the synthesizer
      self.player = Player()
      self.player.open_stream()
      self.synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

      # Note Frequencies
      self.noteFrequencies = {
         "C" : 261.626,
         "E" : 329.628,
         "G" : 391.996,
         "A" : 440.0
      }

      # Find the pitch pipe dial with the name 'pitch_dial'
      self.dial = self.findChild(QtWidgets.QDial, 'pitch_dial')
      self.dial.valueChanged.connect(self.dialMoved)

      # Find the label 'note_label'
      self.noteLabel = self.findChild(QtWidgets.QLabel, 'note_label')

      # Find the label 'position_label'
      self.positionLabel = self.findChild(QtWidgets.QLabel, 'position_label')

      # Find the button 'play_note'
      self.button = self.findChild(QtWidgets.QPushButton, 'play_note')
      self.button.clicked.connect(self.playNote)

      # Show the GUI
      self.show()
   
   # ############################# UI CONTROL METHODS #############################
   def playNote(self):
      self.player.play_wave(self.synthesizer.generate_constant_wave(self.noteFrequencies[self.noteLabel.text()], 0.5))

   def dialMoved(self):
      pass

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()