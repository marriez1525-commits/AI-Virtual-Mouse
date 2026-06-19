from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class VolumeController:

    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        self.volume = cast(interface, POINTER(IAudioEndpointVolume))

    def set_volume(self, level):
        """
        Set system volume
        level: 0.0 to 1.0
        """
        level = max(0.0, min(1.0, level))
        self.volume.SetMasterVolumeLevelScalar(level, None)

    def increase_volume(self, step=0.05):
        current = self.volume.GetMasterVolumeLevelScalar()
        self.set_volume(current + step)

    def decrease_volume(self, step=0.05):
        current = self.volume.GetMasterVolumeLevelScalar()
        self.set_volume(current - step)