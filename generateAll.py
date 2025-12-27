#!/usr/bin/python
#
# Please run this script from your checkout directory of
# the Frank!Runner. See CONTRIBUTING.md for details on what it does.
#
# This script is needed to build the manual for the Frank!Framework.
# It does two things:
#
# i)
# Run TutorialSteps. See the comments in createAllSnippets.py for details.
#
# ii)
# Build download zips. See the comments in file "buildDownloadZips.py"
# for details.
#
# Please run this script before doing the Sphinx build. Sphinx
# needs the output produced by this script.
#

# These lines are needed if Python has not been installed with an installer.
import sys
sys.path.append("src")

from createSnippets import createAllSnippets
from createSnippets import META_YML

import os

# Root directory for all version histories of all
# Frank configs
tutorialStepsDir = "examples"

# Output directory in which generated reStructuredText snippets
# are stored.
snippetsDir = "includes"

createAllSnippets(tutorialStepsDir, snippetsDir, [])
