# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating Pathogen models for testing."""

from random import choice

import factory

from ..models import PathogenResult


class PathogenFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for TaxaTree's Read Stats."""

    class Meta:
        """Factory metadata."""

        model = PathogenResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def cogem_score(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([0, 1, 2])
