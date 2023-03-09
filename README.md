# Economics-Code
Various code that I make for economics classes.

PDF_Extractor
This is a script I wrote to extract key:value pairs from a pdf. The keys are easily configurable. This script probably saved me a bit of time. I used the data from this for my economics of sports analysis in SAS.

Example usage:
```sh
┌──(username@HOST)-[/PDF_Extractor]
└─$ python Data_Extractor.py
Enter the path to the PDF file: Examples/MLB.pdf

Done!
```


Reserves:
This is a simple script I made to automate calculations for fractional reserve banking.

Example usage:
```
┌──(user@HOST)-[/Reserves]
└─$ python reserves.py
Input the initial currency in the economy.
Initial currency: 20000
Input the reserve ratio and household reserves, these should be between 0 and 1.
Reserve ratio: .17
Household reserves: .10
Money supply: $77051.38

Bank 1:
  Reserves: $3400.00
  Deposits: $2000.00
  Loans: $14940.00

...

The money supply now equals $77051.38
Depositors have $7905.14 in demand deposits.
Borrowers hold $69146.24 in currency.
```
