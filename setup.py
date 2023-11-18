from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()



setup(
    name="sentence-transformers",
    version="1.1.0",
    description="Sentence Embeddings using BERT / RoBERTa / XLM-R",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    download_url="https://github.com/mrpeerat/SCT",
    packages=find_packages(),
    # install_requires=[
    #     'transformers>=4.6.0,<5.0.0',
    #     'tokenizers>=0.10.3',
    #     'tqdm',
    #     'torch>=1.6.0',
    #     'torchvision',
    #     'numpy',
    #     'scikit-learn',
    #     'scipy',
    #     'nltk',
    #     'sentencepiece',
    #     'huggingface-hub==0.10.1',
    #     'protobuf',
    #     'prettytable',
    #     'pandas'
    # ],
    # py_modules=['sentence-transformers'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    keywords="Transformer Networks BERT XLNet sentence embedding PyTorch NLP deep learning"
)
