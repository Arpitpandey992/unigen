from unigen.tests.test_unigen import IUnigenTester
from unigen.tests.test_utils import get_test_file_path
from unigen import AudioFactory
from unigen.wrapper.audio_manager import IAudioManager


class TestOpus(IUnigenTester):

    @classmethod
    def create_audio_manager(cls) -> IAudioManager:
        return AudioFactory.buildAudioManager(get_test_file_path(cls.get_extension()))

    @classmethod
    def get_extension(cls):
        return "opus"

    def test_getInfo(self):
        info = self.audio.getMediaInfo()
        self.assertEqual(info.bit_rate, None)  # unable to get any meaningful info from opus sadly
        self.assertEqual(info.bits_per_sample, None)
        self.assertEqual(info.channels, 2)
        self.assertEqual(info.sample_rate, None)
