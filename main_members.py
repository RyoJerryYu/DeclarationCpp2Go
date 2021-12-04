'''The main func to convert Cpp members to Golang struct.'''
import fileinput

from members import Member


def main():
  member_pattern = Member()
  for line in fileinput.input():
    res = member_pattern.transform(line.removesuffix('\n'))
    print(res)


if __name__ == '__main__':
  main()
