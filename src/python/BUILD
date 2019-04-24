python_library(
    name='library',
    dependencies=['3rdparty/python:cffi'],
    sources=['library.py'],
)

python_tests(
    name='test',
    dependencies=[
        ':library',
    ],
    sources=['test.py'],
)


python_binary(
    name='library-bin',
    dependencies=[':library'],
    entry_point='library:main',
    platforms=['linux-x86_64'],
)
