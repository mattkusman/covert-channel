# File Access Covert Channel Demo

This small project demonstrates a very basic covert channel as described in the attached report.  

### Instructions:
You will need python3 installed to run the source code. To run it, within the project directory, run `python3 sender.py` in one terminal, and `python3 reader.py` in a second terminal.
Each terminal will wait for user input. The sender script will await either a `1` or a `0` as input, and the reciever will wait for `enter` to be pressed. 

### How it Works
The sender will control whether the reader can open the specified file using a mock file system that allows only one process access (via the [busy|free] tag at the top of the file). If the file is free when the reader attempts to read, it is recorded as a 1, otherwise it is recorded as a 0.

