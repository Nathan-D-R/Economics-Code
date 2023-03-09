# Economics-Code
Various code that I make for economics classes.

PDF_Extractor
This is a script I wrote to extract key:value pairs from a pdf. The keys are easily configurable. This script probably saved me a bit of time. I used the data from this for my economics of sports analysis in SAS.

Example usage:
```sh
┌──(username㉿HOST)-[./PDF_Extractor]
└─$ python Data_Extractor.py
Enter the path to the PDF file: Examples/MLB.pdf

Done!
```


Reserves:
This is a simple script I made to automate calculations for fractional reserve banking.

Example usage:
```shell
python reserves.py
Input the initial currency in the economy.
Initial currency: 10000
Input the reserve ratio and household reserves, these should be between 0 and 1.
Reserve ratio: .15
Household reserves: 0

Bank 1:
  Reserves: $1500.00
  Deposits: $0.00
  Loans: $8500.00
  
...

The money supply now equals $66666.66
Depositors have $0.00 in demand deposits.
Borrowers hold $66666.66 in currency.
```
It will output reserves, deposits, and loans for every iteration.
It will also output total money supply.
