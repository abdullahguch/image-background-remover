# Image Background Remover

This Python script uses the rembg library to remove the background from an image and saves the result with a transparent background in PNG format.

## Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Install the required Python packages:

```bash
pip install rembg Pillow
```

## Usage

1. Clone this repository or download the script `remove_background.py`.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script:

```bash
python remove_background.py
```

4. Enter the path of the input image when prompted.

```bash
Enter the path of the input image: path/to/your/image.jpg
```

5. The script will remove the background and save the result in the same directory with a ".png" extension.

6. After the script processes the image, it will provide feedback "Background removed successfully!" on the terminal.

## License

This script is licensed under the MIT License - see the LICENSE.md file for details.