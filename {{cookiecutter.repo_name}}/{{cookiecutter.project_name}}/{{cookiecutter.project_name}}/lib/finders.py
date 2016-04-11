"""
Custom Django finders with ignore setting
https://stackoverflow.com/questions/12082902/how-do-i-ignore-static-files-of-a-particular-app-only-with-collectstatic
"""

from pipeline.finders import FileSystemFinder, AppDirectoriesFinder
from django.conf import settings


def add_ignores(ignore_patterns):
    ignore = settings.STATICFILES_FINDERS_IGNORE

    if ignore:
        if ignore_patterns:
            ignore_patterns.extend(ignore)
        else:
            ignore_patterns = ignore

    return ignore_patterns


class FileSystemFinderIgnore(FileSystemFinder):
    def list(self, ignore_patterns):
        return super(FileSystemFinderIgnore, self).list(add_ignores(ignore_patterns))


class AppDirectoriesFinderIgnore(AppDirectoriesFinder):
    def list(self, ignore_patterns):
        return super(AppDirectoriesFinderIgnore, self).list(add_ignores(ignore_patterns))