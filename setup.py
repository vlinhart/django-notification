from setuptools import setup, find_packages


setup(
    name="django-notification",
    version="1.0",
    description="User notification management for the Django web framework",
    long_description=open("docs/usage.rst").read(),
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    url="https://github.com/pinax/django-notification",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
    zip_safe=False,
)
