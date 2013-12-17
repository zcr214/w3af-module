import sys
import unittest

from tests.base import BaseInstallMixin


class TestSetupInstall(BaseInstallMixin, unittest.TestCase):

    INSTALL_CMD = '%s setup.py install --single-version-externally-managed' % sys.executable
