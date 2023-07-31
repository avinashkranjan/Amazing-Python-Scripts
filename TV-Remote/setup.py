from setuptools import setup
setup(
    data_files=[
        ('lib/systemd/user', ['tv.service']),
        ('share/systemd/user', ['tv.service']),
    ],
)
