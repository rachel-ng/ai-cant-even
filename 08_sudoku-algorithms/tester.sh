dotpyfile="x.py"
inputfile="master-boards.txt"
outputfile="outputfile.txt"
while read line; do
time(python $dotpyfile $inputfile $outputfile $line);
done<<<"name,Easy-NYTimes,unsolved
name,Medium-NYTimes,unsolved
name,Medium-NYTimes,solved
name,WebSudoku-Hard,unsolved
name,WebSudoku-Evil,unsolved
name,hardest-sudoku-telegraph,unsolved
name,sudokugarden.de/files/100sudoku2-en.pdf-Nr-100,unsolved
name,sudokugarden.de/files/100sudoku2-en.pdf-Nr-50,unsolved"
