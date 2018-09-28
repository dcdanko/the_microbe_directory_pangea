"""Test suite for CogemPathogenicity AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import CogemPathogenicityResultFactory
from ..modules import CogemPathogenicityModule # import this just to make sure no typos in module (not used otherwise)

class TestCogemPathogenicityModels(TestCase):
    """Test suite for CogemPathogenicity AnalysisModule."""

    def test_add_cogem_pathogenicity(self):
        """Ensure CogemPathogenicity model is created correctly."""

        cogem_pathogenicity_result = CogemPathogenicityResultFactory()

        try:
            cogem_pathogenicity_result.validate()
        except ValidationError:
            self.fail('CogemPathogenicityResult validation raised unexpected ValidationError.')
