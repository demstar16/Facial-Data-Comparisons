# cits1401-project2

Due date: 5PM Friday 27th May (end of week 12)
Weight: 20%

Resources:
  + [Project Spec](https://lms.uwa.edu.au/bbcswebdav/pid-2598858-dt-content-rid-36576430_1/xid-36576430_1)
 
## Todo
+ [x] Read Specs
+ [x] Process CSV file
  + [x] Filter so we only have the wanted adultID's
+ [x] Implement OP1
+ [x] Implement OP2
+ [x] Implement OP3
  + [x] Figure out ordering when sorting
+ [x] Implement OP4
+ [ ] Additional Requirements
    + [x] Rounding in correct areas
    + [x] Clarify terminating gracefully & what to return
    + [x] Order of csv data
    + [x] Variable Names
    + [x] comments
    + [ ] do we need to account for spaces in CSV file?
    + [ ] Your program needs to validate the inputs to the main() function and gracefully terminate if invalid inputs are provided.
    + [ ] You program needs to terminate gracefully if the file cannot be found or opened. For graceful terminations, you need to print the message related to the problem and return None for each unavailable output.
    + [ ] Your program needs to validate the input data from the file. The X,Y or Z coordinate (or all coordinates) of a landmark could be corrupted or missing. In that case the value in the cell would be empty or out of bounds. If data is not correct, then entire row needs to be discarded.
    + [ ] If a particular landmark of a face is missing or corrupted, then consider the entire adult’s record corrupt.
    + [ ] It is possible that the Research Assistant marking these landmarks on the faces could have forgotten to mark/ record a landmark. In this case, that particular landmark will be missing from the CSV file. You should follow the protocol given above in such cases.
    + [x] Your program needs to consider that record of the landmarks for a particular Adult may not have any specific order or can be in any order (excluding header row).
    + [x] The columns in the CSV file can be in any order and the headings are case insensitive i.e. AdultID, Landmark, X, Y and Z.
    + [x] Your program needs to convert all text data in the csv to be upper order alphabets to ensure that program is case insensitive.