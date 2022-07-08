# download-expensify-files
Short python script to download all receipts for recordkeeping when leaving Expensify.

I wrote the python script since I am more comfortable with python than command line.

Note that I would go into the CSV and manually update the "Downloaded" parameter if it errored out in the middle of the execution.

This is not a robust solution but provided a quick and dirty way to solve a business problem.

Credit to tullywork on Expensify forum for the idea and instructions below (https://community.expensify.com/discussion/3531/how-do-i-export-download-actual-images-of-receipts-for-document-support-storage):

"Figured this out; hopefully this is helpful to someone else. (note: I'm not a developer or in any way associated w/ expensify); note I did this on a Windows machine.

1) From the Expenses Section in the App; select a receipt (doesnt matter which at this point)

2) In the top right of the UI select Export To and select 'create new CSV layout'

3) In the new layout, customize as desired, I removed all columns and just created a new column with the Formula: {expense:receipt:url:direct} then Save Export Format

4) back in the Expenses section of the UI, select the receipts you want to download from the in my case I selected the 'Date' header checkbox and chose 'Select All'; then select 'Export to' button and select the previously saved export format.

5) In excel I created two columns; the first column A had the URL from above, the second column B I used Find/Replace feature in excel to remove 'https://s3.amazonaws.com/receipts.expensify.com/' so I was just left with the File Name in the B column (like shown below - just an example, all files should be different names)

6) I save this CSV file into a new empty directory

7) Open a cmd window and navigate to the new directory where you saved the above file; run the following command:

for /f "tokens=1,2 delims=," %a in (Bulk_Expense_Export2.csv) do curl %a --output %b

This command essentially loops through the CSV file (mine was named Bulk_Expense_Export2.csv) and using the 'curl' command line command for each column A (the URL to the file) created a file in the directory with the FileName from s3 - column B.

Obviously was fairly quick for a small number of receipts (in my case ~700); could take a long time for a larger fileset.

Hope this helps someone accomplish something similar to what I needed to do...backup all my data!"

