# Accessing file using relative file path
import os
import __root__

# ways to access project root in relative style
d = os.path.join(__root__.ROOT_DIR, 'files/')
print(d)

PROJECT_ROOT = os.path.split(os.environ['VIRTUAL_ENV'])[0]
print(PROJECT_ROOT)


