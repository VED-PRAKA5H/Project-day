# Mile to Kilometer Converter (GUI)

A simple Python GUI project that converts **Miles** to **Kilometers** using the `Tkinter` library.  

***

### Features
- GUI-based converter using `Tkinter`.
- Converts input miles to kilometers with precision up to **2 decimal places**.
- User-friendly layout with labels, entry field, and calculate button.
- Automatic focus on input field when the app starts.

***

### Formula
$ 1 \text{ Mile} = 1.60934 \text{ Kilometers} $

***

### Requirements
- Python 3.x  
- Tkinter (comes pre-installed with Python)

***

### How to Run
1. Clone this repository or download the source code.  
2. Run the script in your terminal or Python IDE:

    ```bash
    python main.py
    ```

3. Enter a value in **miles** and click **calculate** to get the converted value in kilometers.

***

### Code Overview
- **Window**: Creates a Tkinter window with padding for clean layout.  
- **Labels**: Displays text like *Miles*, *is equal to*, *KM*, and shows the result dynamically.  
- **Entry**: Input field where the user types the miles value.  
- **Button**: Triggers calculation using the `calc()` function.  
- **calc()**: Reads user input, performs conversion, and updates label with result.

***


### References
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  
- [TCL/Tk Docs](https://www.tcl-lang.org/man/tcl8.6/TkCmd/pack.htm)
