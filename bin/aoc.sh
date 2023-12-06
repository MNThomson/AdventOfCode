#!/bin/bash
# aoc:   quickly run AdventOfCode problems
# setup: ln -s `pwd`/bin/aoc.sh /usr/local/bin/aoc

if [[ "$#" -eq 1 ]] && ! [[ "$1" == "-"* ]]; then
  python3.11 $1
fi

# Iterate through args
while [[ $# -gt 0 ]] && [[ "$1" == "-"* ]]; do
  opt="$1"
  shift #expose next argument

  case "$opt" in
  "-t") # run test input
    python3.11 1.py <../test.txt
    shift
    ;;
  "-l") # lint files
    black .
    isort .
    shift
    ;;
  *)
    echo >&2 "Invalid option: $opt"
    exit 1
    ;;
  esac
done
