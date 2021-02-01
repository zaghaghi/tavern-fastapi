#!/usr/bin/env python


from distutils.core import setup

classifiers_list = [
    "License :: OSI Approved :: MIT License",
    "Development Status :: 4 - Beta",
    "Framework :: Pytest"
]

setup(
    name="tavern_fastapi",
    version="0.0.1",
    author="Hamed Zaghaghi",
    author_email="hamed.zaghaghi@gmail.com",
    description="tavern http backend for fastapi",
    packages=[
        "tavern_fastapi",
    ],
    classifiers=classifiers_list,
    requires=["fastapi", "pytest", "tavern", "future"],
    data_files=[("schemas", ["tavern_fastapi/schema.yaml"])]
)
