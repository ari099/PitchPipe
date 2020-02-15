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
      self.noteFrequencies = [
         {"D" : 293.66},
         {"E" : 329.63},
         {"F" : 349.23},
         {"G" : 392.0},
         {"A" : 440.0},
         {"B" : 493.88},
         {"C" : 261.63}
      ]

      # Find the pitch pipe dial with the name 'pitch_dial'
      self.dial = self.findChild(QtWidgets.QDial, 'pitch_dial')
      self.dial.valueChanged.connect(self.dialMoved)
      self.pitch = list(self.noteFrequencies[self.dial.value()-2].keys())[0]

      # Find the label 'note_label'
      self.noteLabel = self.findChild(QtWidgets.QLabel, 'note_label')
      self.noteLabel.setText(self.pitch)

      # Find the label 'position_label'
      self.positionLabel = self.findChild(QtWidgets.QLabel, 'position_label')

      # Find the button 'play_note'
      self.button = self.findChild(QtWidgets.QPushButton, 'play_note')
      self.button.clicked.connect(self.playNote)

      # Show the GUI
      self.show()
   
   # ############################# UI CONTROL METHODS #############################
   def playNote(self):
      self.player.play_wave(
         self.synthesizer.generate_constant_wave(
            self.noteFrequencies[self.dial.value()-2][self.pitch], 0.5)
         )

   def dialMoved(self):
      self.pitch = list(self.noteFrequencies[self.dial.value()-2].keys())[0]
      self.noteLabel.setText(self.pitch)
      # print(self.dial.value())

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()