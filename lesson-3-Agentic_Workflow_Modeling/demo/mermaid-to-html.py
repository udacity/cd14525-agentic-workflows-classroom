import os

def save_mermaid_to_html(mermaid_code, filename="mermaid_diagram.html"):
    """
    Saves a Mermaid diagram to an HTML file, which can then be opened in a browser.

    Args:
        mermaid_code (str): The Mermaid diagram code (e.g., 'graph TD; A-->B;').
        filename (str): The name of the HTML file to save.
    """
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mermaid Diagram</title>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.js';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        <style>
            body {{ font-family: sans-serif; }}
            .mermaid {{ display: flex; justify-content: center; align-items: center; min-height: 90vh; }}
        </style>
    </head>
    <body>
        <div class="mermaid">
            {mermaid_code}
        </div>
    </body>
    </html>
    """
    with open(filename, "w") as f:
        f.write(html_template)
    print(f"Mermaid diagram saved to {os.path.abspath(filename)}. Open this file in your web browser.")

if __name__ == "__main__":

    sequence_code = """
    sequenceDiagram
        participant User
        participant Server
        participant Database

        User->>Server: Request data
        Server->>Database: Query data
        Database-->>Server: Data results
        Server-->>User: Display data
    """
    save_mermaid_to_html(sequence_code, "my_sequence_diagram.html")