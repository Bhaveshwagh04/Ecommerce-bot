from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="Bhavesh",
    author_email="bhaveshwaghbw.49@gmail.com",
    packages=find_packages(),
    install_requires=[
        "langchain-astradb",
        "langchain ",
        "langchain-openai",
        "langchain-groq",
        "datasets",
        "pypdf",
        "python-dotenv",
        "flask",
    ],
)
