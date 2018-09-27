# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating CogemPathogenicity models for testing."""

from random import choice

import factory

from ..models import CogemPathogenicityResult


class CogemPathogenicityResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for TaxaTree's Read Stats."""
    class Meta:
        """Factory metadata."""
        model = CogemPathogenicityResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def cogem_pathogenicity(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([0, 1, 2])
