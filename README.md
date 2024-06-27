# shell-sobriquet
*A tool that lets you alias your day to day shell commands.*

## Setup


1. Download the .whl file present in 

        
        dist/shell_sobriquet-1.0-py3-none-any.whl


2. Install the package with -


        pip install shell_sobriquet-1.0-py3-none-any.whl


3. Alias your shell commands with -


        alias-it <name-of-alias> "<shell-command>"
        
        
    Argument 1 - Any name given to alias

    Argument 2 - Any shell command in double quotes

4. Restart your terminal.

## Usage

Register an alias:

    alias-it <name-of-alias> "<shell-command>"

###### *Note: shell-command should be within double quotes.*

List aliases & their commands:

    alias-it ls

Clear all registered aliases:

    alias-it clear

Clear a single alias:

    alias-it clear <name-of-alias>

## Sample

    > alias-it say-hi "echo Hello World!" 
    > say-hi
    > Hello World!

## Support
This tool is presently supported on mac and linux based systems only.

*Feel free to raise a pull request if you'd like to contribute.*