#!/usr/bin/env python

import sys
import base64

"""
This is a very crude a dumb script that act as a fake mozjpeg executable.
Sample command

    fake-mozjpeg.py -outfile dest.jpg -optimise -copy none source.jpg

It will always produce the same image.
"""


JPEG = (
    '/9j/4AAQSkZJRgABAQEASABIAAD/2wCEAAUEBAQEAwUEBAQGBQUGCA0ICAcHCBALDAkNExAUEx'
    'IQEhIUFx0ZFBYcFhISGiMaHB4fISEhFBkkJyQgJh0gISABBQYGCAcIDwgIDyAVEhUgICAgICAg'
    'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIP/CABEIABQAFAMBEg'
    'ACEQEDEQH/xAAYAAADAQEAAAAAAAAAAAAAAAAFBgcIBP/aAAgBAQAAAADTMzuGZep3HBFj/8QA'
    'GQEAAQUAAAAAAAAAAAAAAAAAAAIDBAUG/9oACAECEAAAAFPRdsVv/8QAFgEBAQEAAAAAAAAAAA'
    'AAAAAABAMF/9oACAEDEAAAABqFn1T/AP/EACgQAAEDAgUDBAMAAAAAAAAAAAECAwQFEQAGByEx'
    'EiJBExRxkRVCUf/aAAgBAQABPwDPlYqGX8jVKqUr0BObShDK5AJbbUtYQFqA5Ceq9tr2xpXqDm'
    'Wq50ey5mCrx6+1JYMiPLjxRH9EpsSCL9yVBQKfIsdzfHRjT/Vas5lpknKGZIr9UQ+2o+9jEFyM'
    'OUlfg7gW8/ONG3o7OqMxdXKorntlCMXXexSyQFb8bgbD5xmHUyt0vMs+ntRmEMsOlDYLJcJSPJ'
    'UDbfc7ccYpVLp9Hp/4ilxGokNodAbaSB1f0qP7E+SecViNHaSFIZQBDZKWkW7QL34+vrEqz8t1'
    'bvUSFFIstQ2Bt4OP/8QAIBEAAgICAAcAAAAAAAAAAAAAAQIAAxEhBBIiQYGR8P/aAAgBAgEBPw'
    'BLSx5QN+4rO4OvvEbikU4MrVVUBRiW9NbldGLTXYis6gnHcT//xAAdEQACAQQDAAAAAAAAAAAA'
    'AAABAgADEiExBBET/9oACAEDAQE/AFRLhdqcihSAFu54dxiScyll1BjEqxAxP//Z'
)


if __name__ == '__main__':
    args = sys.argv[1:]
    destination = args[args.index('-outfile') + 1]
    with open(destination, 'wb') as f:
        f.write(base64.b64decode(JPEG))
