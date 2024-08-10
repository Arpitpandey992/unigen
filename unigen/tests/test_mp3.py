from tests.test_unigen import IUnigenTester
from tests.test_utils import get_test_file_path
from unigen import AudioFactory
from unigen.wrapper.audio_manager import IAudioManager


class TestMp3(IUnigenTester):

    @classmethod
    def create_audio_manager(cls) -> IAudioManager:
        return AudioFactory.buildAudioManager(get_test_file_path(cls.get_extension()))

    @classmethod
    def get_extension(cls):
        return "mp3"

    def test_getInfo(self):
        info = self.audio.getMediaInfo()
        self.assertEqual(info.bit_rate, 320000)
        self.assertEqual(info.bits_per_sample, None)
        self.assertEqual(info.channels, 2)
        self.assertEqual(info.sample_rate, 44100)
