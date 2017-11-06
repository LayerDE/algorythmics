#!/usr/bin/python3
import os


def run_c(str):
    os.system(str)


if __name__ == "__main__":
    run_c("gcc -fPIC -Os -std=c99 -o launcher launcher.c -ldl")
    run_c("chmod +x launcher")
    run_c("./launcher")
