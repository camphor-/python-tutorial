#!/bin/bash
cd `dirname $0`

cd ./source/
jupyter nbconvert --to=python ../notebooks/*
