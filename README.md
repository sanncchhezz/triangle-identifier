# Triangle Identifier

Interactive tools for classifying triangles by their side lengths and angles. The project includes both a command-line questionnaire (`triangle.py`) and a p5.js-powered web visualizer (`Triangle_Identifier.html`). The python code was created with the assistance of gpt5 and the web page was created by Codex.

## Project Structure
- `triangle.py` — Console assistant that walks through a series of questions to identify the triangle type.
- `Triangle_Identifier.html` — Browser UI that lets you select side/angle characteristics and renders a matching triangle using p5.js.

## Requirements
- Python 3.8+
- Web browser with JavaScript enabled (for the HTML interface)

All Python dependencies are from the standard library. See `requirements.txt`.

## Usage
1. **Command-line version**
   ```bash
   python3 triangle.py
   ```
   Answer the prompts to classify your triangle. Enter `n` when you're done to exit.

2. **Web version**
   - Open `Triangle_Identifier.html` in your browser.
   - Pick the number of matching sides and answer the angle questions.
   - A representative triangle visualization updates automatically.

## Development Notes
- The HTML file references p5.js from a CDN. Internet access is required the first time it loads to fetch the library.
- Feel free to extend either interface with additional validations, visualizations, or persistence.
