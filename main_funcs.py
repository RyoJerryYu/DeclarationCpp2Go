'''The main func to convert Cpp methods to Golang interface methods.'''
import fileinput

from methods import Method


def main():
  method_pattern = Method()
  for line in fileinput.input():
    if line.strip() == '':
      continue
    res = method_pattern.transform(line.removesuffix('\n'))
    print(res)


if __name__ == '__main__':
  main()
