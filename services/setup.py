from setuptools import setup, find_packages

setup(
    name="auth-services",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Dependency confusion target - this package doesn't exist in PyPI
        "nonexistent-python-auth==1.2.3",
        "requests>=2.28.0",  # Valid dependency for comparison
    ],
    # GitHub repo jacking target - this repo doesn't exist
    dependency_links=[
        "git+https://github.com/fake-security-org12321312312/missing-python-auth.git#egg=missing-python-auth"
    ],
    author="Test Author",
    description="Test service with vulnerabilities"
)
