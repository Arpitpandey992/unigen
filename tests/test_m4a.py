from tests.test_unigen import IUnigenTester
from tests.test_utils import get_test_file_path
from unigen import AudioFactory
from unigen.audio_manager import IAudioManager


class TestM4a(IUnigenTester):

    @classmethod
    def create_audio_manager(cls) -> IAudioManager:
        return AudioFactory.buildAudioManager(get_test_file_path(cls.get_extension()))

    @classmethod
    def get_extension(cls):
        return "m4a"
