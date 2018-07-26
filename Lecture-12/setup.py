from setuptools import find_packages

from setuptools import setup

packs = find_packages()

print(packs)

setup(
    name = "Facebook meme chatbot",
    version = "1.0.0-snapshot",
    install_requires=['flask',
                      'pymessenger',
                      'gunicorn',
                      'opencv-python'
                      ],
    packages=find_packages(),
)

