"""Test suite for HasAntimicrobialSusceptibility AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import HasAntimicrobialSusceptibilityResultFactory
from ..modules import HasAntimicrobialSusceptibilityModule # import this just to make sure no typos in module (not used otherwise)

class TestHasAntimicrobialSusceptibilityModels(TestCase):
    """Test suite for HasAntimicrobialSusceptibility AnalysisModule."""

    def test_add_has_antimicrobial_susceptibility(self):
        """Ensure HasAntimicrobialSusceptibility model is created correctly."""

        has_antimicrobial_susceptibility_result = HasAntimicrobialSusceptibilityResultFactory()

        try:
            has_antimicrobial_susceptibility_result.validate()
        except ValidationError:
            self.fail('HasAntimicrobialSusceptibilityResult validation raised unexpected ValidationError.')
