#!/usr/bin/env python
# -*- coding: utf-8 -*-


def square_root(number: int) -> float:
    # TODO completer la fonction
    square_root = number ** 0.5 
    return square_root 


def square(number: int) -> int:
    # TODO completer la fonction
    square = number ** 2 
    return square 


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
