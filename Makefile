# File              : Makefile
# Author            : cppygod
# Date              : 23.01.2022
# Last Modified Date: 10.02.2022
# Last Modified By  : cppygod
# +--------------------+
# |                    |
# |   GENERAL CONFIG   |
# |                    |
# +--------------------+

pname := concert_tickets
DEBUG := true
LANG := cpp

CXX := g++
CXXFLAGS := -std=c++17 -O2 -Wall -Wextra -pedantic -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -Wno-unused-result -Wno-sign-conversion
DEBUG_CXXFLAGS := -fsanitize=address -fsanitize=undefined -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-sanitize-recover=all -fstack-protector-all -D_FORTIFY_SOURCE=2
DEBUG_CXXFLAGS += -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC
PRECOMPILE_HEADERS := bits/stdc++.h


# +-------------------+
# |                   |
# |   GENERAL RULES   |
# |                   |
# +-------------------+


.PHONY: default
default: build

.PHONY: build
build:
	@ mkdir -p "output"
	${CXX} ${CXXFLAGS}  ${pname}.cpp -o output/${pname}

.PHONY: run
run: build
	timeout 1.0s ./output/${pname} && cat data.out

.PHONY: clean
clean:
	rm -rf output/
