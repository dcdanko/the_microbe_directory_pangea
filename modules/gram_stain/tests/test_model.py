"""Test suite for GramStain AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import GramStainResultFactory
from ..modules import GramStainModule # import this just to make sure no typos in module (not used otherwise)

class TestGramStainModels(TestCase):
    """Test suite for GramStain AnalysisModule."""

    def test_add_is_animal_pathogen(self):
        """Ensure GramStain model is created correctly."""

        gram_stain_result = GramStainResultFactory()

        try:
            gram_stain_result.validate()
        except ValidationError:
            self.fail('GramStainResult validation raised unexpected ValidationError.')
