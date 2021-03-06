"""CogemPathogenicity AnalysisModule."""

from analysis_packages.base import AnalysisModule

from .constants import MODULE_NAME
from .models import CogemPathogenicityResult


class CogemPathogenicityModule(AnalysisModule):
    """Read Stats AnalysisModule."""

    @staticmethod
    def name():
        """Return the name of the taxa tree module."""
        return MODULE_NAME

    @staticmethod
    def result_model():
        """Return the embedded result."""
        return CogemPathogenicityResult
