#!/usr/bin/env python


from distutils.core import setup

classifiers_list = [
    "License :: OSI Approved :: MIT License",
    "Development Status :: 4 - Beta",
    "Framework :: Pytest"
]

setup(
    name="tavern_fastapi",
    version="0.0.2",
    author="Hamed Zaghaghi",
    author_email="hamed.zaghaghi@gmail.com",
    description="Tavern http backend for FastAPI TestClient",
    packages=[
        "tavern_fastapi",
    ],
    classifiers=classifiers_list,
    requires=["fastapi", "pytest", "tavern", "future"],
    include_package_data=True,
    package_data={"tavern_fastapi": ["schema.yaml"]},
)
