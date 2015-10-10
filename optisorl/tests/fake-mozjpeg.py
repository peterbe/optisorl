#!/usr/bin/env python

import sys
import base64

"""
This is a very crude a dumb script that act as a fake mozjpeg executable.
Sample command

    fake-mozjpeg.py -outfile dest.jpg -optimise source.jpg

It will always produce the same image.
"""


JPEG = (
    '/9j/4AAQSkZJRgABAQEASABIAAD/2wCEAAUEBAQEAwUEBAQGBQUGCA0ICAcHCBALDAkNExAUE'
    'xIQEhIUFx0ZFBYcFhISGiMaHB4fISEhFBkkJyQgJh0gISABBQYGCAcIDwgIDyAVEhUgICAgIC'
    'AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIP/CABEIABQAFAM'
    'BEgACEQEDEQH/xAAYAAADAQEAAAAAAAAAAAAAAAAFBgcIBP/aAAgBAQAAAADTMzuGZep3HBFj'
    '/8QAGQEAAQUAAAAAAAAAAAAAAAAAAAIDBAUG/9oACAECEAAAAFPRdsVv/8QAFgEBAQEAAAAAA'
    'AAAAAAAAAAABAMF/9oACAEDEAAAABqFn1T/AP/EACgQAAEDAgUDBAMAAAAAAAAAAAECAwQFEQ'
    'AGByExEiJBExRxkRVCUf/aAAgBAQABPwDPlYqGX8jVKqUr0BObShDK5AJbbUtYQFqA5Ceq9tr'
    '2xpXqDmWq50ey5mCrx6+1JYMiPLjxRH9EpsSCL9yVBQKfIsdzfHRjT/Vas5lpknKGZIr9UQ+2'
    'o+9jEFyMOUlfg7gW8/ONG3o7OqMxdXKorntlCMXXexSyQFb8bgbD5xmHUyt0vMs+ntRmEMsOl'
    'DYLJcJSPJUDbfc7ccYpVLp9Hp/4ilxGokNodAbaSB1f0qP7E+SecViNHaSFIZQBDZKWkW7QL3'
    '4+vrEqz8t1bvUSFFIstQ2Bt4OP/8QAIBEAAgICAAcAAAAAAAAAAAAAAQIAAxEhBBIiQYGR8P/'
    'aAAgBAgEBPwBLSx5QN+4rO4OvvEbikU4MrVVUBRiW9NbldGLTXYis6gnHcT//xAAdEQACAQQD'
    'AAAAAAAAAAAAAAABAgADEiExBBET/9oACAEDAQE/AFRLhdqcihSAFu54dxiScyll1BjEqxAxP'
    '//Z'
)

if __name__ == '__main__':
    args = sys.argv[1:]
    destination = args[args.index('-outfile') + 1]
    with open(destination, 'wb') as f:
        f.write(base64.b64decode(JPEG))
