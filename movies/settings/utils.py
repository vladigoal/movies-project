import os


__all__ = ('PROJECT_ROOT', 'here', 'root', 'proj')

here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here('..')
proj = lambda *x: os.path.abspath(os.path.join(os.path.abspath(PROJECT_ROOT),
    *x))
root = lambda *x: os.path.abspath(os.path.join(proj('..'), *x))