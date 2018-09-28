"""Test suite for HasExtremeEnvironment AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import HasExtremeEnvironmentResultFactory
from ..modules import HasExtremeEnvironmentModule # import this just to make sure no typos in module (not used otherwise)

class TestHasExtremeEnvironmentModels(TestCase):
    """Test suite for HasExtremeEnvironment AnalysisModule."""

    def test_add_is_animal_pathogen(self):
        """Ensure HasExtremeEnvironment model is created correctly."""

        gram_stain_result = HasExtremeEnvironmentResultFactory()

        try:
            gram_stain_result.validate()
        except ValidationError:
            self.fail('HasExtremeEnvironmentResult validation raised unexpected ValidationError.')
