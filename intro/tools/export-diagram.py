"""Export the editable SVG as vector PDF for XeLaTeX (PyGObject/Rsvg + Cairo)."""
from pathlib import Path

import cairo
import gi

gi.require_version("Rsvg", "2.0")
from gi.repository import Rsvg

image_dir = Path(__file__).resolve().parents[1] / "image"
source = image_dir / "c-python-execution.svg"
target = source.with_suffix(".pdf")
handle = Rsvg.Handle.new_from_file(str(source))
width, height = 1440, 590
surface = cairo.PDFSurface(str(target), width, height)
context = cairo.Context(surface)
viewport = Rsvg.Rectangle()
viewport.x, viewport.y, viewport.width, viewport.height = 0, 0, width, height
handle.render_document(context, viewport)
surface.finish()
print(target)
