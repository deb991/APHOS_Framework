#!/usr/bin/env python
import os
import sys
import PIL
from PIL import ImageGrab

ImageGrab.grab().save("SCREENSHOT.jpeg", "jpeg")