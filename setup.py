from distutils.core import setup

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.3",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="黑k江湖",
    author_email="m-6290499@moe-dl.edu.my",
    url="https://github.com/leecongwei/main-termux",
    keywords=["dos", "http", "slowloris"],
    license="MIT",
)
