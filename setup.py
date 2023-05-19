from setuptools import setup, find_packages
# Call setup function
setup(
    author="Rob",
    description="FOr use with private repository",
    name="grades_packages",
    packages=find_packages(include=['grades_packages', 'grades_packages.*']),
    version="____",
)
