"""IsSporeForming AnalysisModule."""

from analysis_packages.base import AnalysisModule

from .constants import MODULE_NAME
from .models import IsSporeFormingResult


class IsSporeFormingModule(AnalysisModule):
    """IsSporeForming AnalysisModule."""
    @staticmethod
    def name():
        """Return the name of the module."""
        return MODULE_NAME

    @staticmethod
    def result_model():
        """Return the embedded result."""
        return IsSporeFormingResult
