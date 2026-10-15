# Introduction

## What is Programming Language?

Programming Language is language used to give instructions to computer based on which, computer performs tasks.
But why do we need programming languages, can't we just give instructions to computer in English or any other natural languages and computer execute tasks based on that.

Because computers can only understand binary language(0s and 1s), the programming language allows you to write instructions which are then translated to binary language.

Then, why not just use Natural languages if it is going to be translated anyways?

Because, Natural Languages are ambigious (one instruction can have multiple meanings), 
whereas programming languages are specific or clear in terms of writing instructions.

Programming Languages borrows terms from natural languages like English making them human readable language and imposes strict rules so that there is no ambiguity or mistakes made.

Programming Languages are classified based on abstraction and the paradigms (way the language works.) and also the way they are executed.

## What is Abstraction?

Abstraction basically means how closely programming language can operate on hardware components like memory,register of computer.

Based on abstraction, there are three levels of programming languages.

1. Low Level Programming Languages - are programming languages that works on memory and registers directly.
Example -  Assembly Language

2. Middle Level Languages - are programming languages that allows you to work with programming concepts like functions and data structures while also allowing to work with memory.
Example - Language like C/C++ can also work with memory directly.

3. High Level Languages - are programming languages that do not work directly with memory and registers and works on high-level concepts like data structures.

Example - Python, Java, JavaScript

Programming Languages are also classified based on paradigm (the way programming langauge works).

There are 2 Programming Paradigms:

1. Imperative Programming - is programming paradigm where we describe the steps and the whole procedure of how program is going to work and what tasks we want to get done.

- Imperative Programming consists of 2 sub-types:
    1. Procedural Programming - In Procedural Programming, multiple instructions written by programmer are grouped into procedures or functions, which are executed one by one.
    Example - C
    2. Object-Oriented Programming - In Object-Oriented Programming, the programs consists of objects - a group of attributes and functions.
    Example - Java

2. Declarative Programming - is programming paradigm where programmer only described what tasks to be done and in what manner the task should be done, you do not write the whole procedure to perform a task.

- There are 2 subtypes of Declarative Programming-
    1. Functional Programming - is programming paradigm which deals with use of functions, where multiple functions are composed (output of one function is used as input for another.)
    Example - Haskell
    2. Logic Programming - is programming paradigm where program consists of facts and rules and based on that, the computer performs tasks.
    Example - Prolog

Modern Languages like Python, Java are considered as multi-paradigm languages, where more than one type of programming paradigms can be used.

# Compiler and Interpreter

Compiler is a program which translates the program into machine code creating an executable file, which is executed by computer.
- Whole program is read and if there is an error, the error is raised and the program cannot be executed.

Interpreter is a program which translates and run each line in the code.
- Each line is translated/checked for errors and executed, and if any line contains error, the error is raised and the interpreter stops executing lines below it.

The languages that use compiler are called Compiled Languages whereas languages using interpreter are called Interpreted languages.

Note- The terms compiled and interpreted are used broadly, not strictly. For ex- Python, even being called as interpreted language, it consists of compiling the code into bytecode and then executing line by line by Virtual Machine instead of translation and execution happening at one time.

## Compile Time and Runtime

Compile Time is phase where program is checked for syntax and semantic errors and translated into machine code.
Example - Missing Semicolons, Spelling Mistakes

Runtime is phase where compiled program is executed and logical error could be raised in this phase.
Example - Dividing a number by zero or trying to add to two variable with different data types.

## Programming Fundamentals

After discussing the types of programming languages, let's talk about programming fundamentals.
The Programming Fundamentals are the concepts that are used to learn how to work with programming languages.
The Programming Fundamentals remains same for all programming languages and have some additional concepts based on what programming language you're learning.

Here is the list of Programming Fundamentals:
1. Variables and data types: integers, floats, strings, booleans, type casting
2. Operators and expressions: arithmetic, comparison, logical, bitwise
3. Input and output: reading user input, printing, file I/O
4. Control flow: if/else, switch, loops (for, while), break/continue
5. Functions: parameters, return values, scope, recursion
6. Native Data Structures and their operations
7. String and String methods
8. Error handling
9. Object-Oriented Programming Concepts (if included). 