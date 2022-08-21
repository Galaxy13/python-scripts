from setuptools import setup

setup(
    name='Calendar Fimy',
    version='0.1.1',
    author='Retroider',
    description='An app for addind dates in MS Word document',
    long_description='Application uses Tkinter for front part. User can choose a column of dragged MS Word document,'
                     'and number of dates, which you can choose via TkCalendar module',
    url='https://github.com/Galaxy13',
    keywords='document, word, calendar',
    python_requires='>=3.10',
    install_requires=[
     'tkinterdnd2',
     'tkcalendar',
     'playsound==0.2.2',
     'python-docx'
    ],
    package_data={
        'mp3': ['mp3/*.mp3']
    }
)