# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/arrangement.py
# Compiled at: 2018-04-23 20:27:04
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl, EncoderControl

class ArrangementComponent(Component):
    set_or_delete_cue_button = ButtonControl()
    jump_encoder = EncoderControl()

    @set_or_delete_cue_button.pressed
    def set_or_delete_cue_button(self, _):
        if self.application.view.focused_document_view == 'Arranger':
            self.song.set_or_delete_cue()

    @jump_encoder.value
    def jump_encoder(self, value, _):
        step = -1.0 if value < 0 else 1.0
        if self.song.is_playing:
            step *= 4.0
        self.song.jump_by(step)
