from tkinter import Tk, Button, Label, filedialog, OptionMenu, StringVar, Scale
from PIL import Image
import os

def resize_image(image_path, output_path, resolution, quality=100):
    img = Image.open(image_path)
    img.thumbnail(resolution)
    img.save(output_path, quality=quality)

def convert_to_webp(input_dir, output_dir, resolution, quality):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_dir, output_filename)
            resize_image(input_path, output_path, resolution, quality)

def select_input_directory():
    global input_directory
    input_directory = filedialog.askdirectory()
    input_label.config(text=input_directory)

def select_output_directory():
    global output_directory
    output_directory = filedialog.askdirectory()
    output_label.config(text=output_directory)

def convert_images():
    global input_directory, output_directory

    if not input_directory or not output_directory:
        status_label.config(text="Error: Select input/output directories!")
        return
    
    resolution = resolutions[resolution_var.get()]
    quality = quality_scale.get()
    
    try:
        convert_to_webp(input_directory, output_directory, resolution, quality)
        status_label.config(text="Conversion complete!")

    except Exception as text:
        status_label.config(text=f"Error during conversion: {str(text)}")



# GUI setup
root = Tk()
root.title("Image Converter by Mario Pfaff")

input_directory = ""
output_directory = ""

input_button = Button(root, text="Select Input Directory", command=select_input_directory)
input_button.pack(pady=5)

input_label = Label(root, text="")
input_label.pack()

output_button = Button(root, text="Select Output Directory", command=select_output_directory)
output_button.pack(pady=5)

output_label = Label(root, text="")
output_label.pack()

# Resolution options
resolutions = {
    "Ultra Low (80x60)": (80, 60),
    "Very Low (160x120)": (160, 120),
    "Low (320x240)": (320, 240),
    "Moderate (480x360)": (480, 360),
    "Standard Definition (640x480)": (640, 480),
    "Enhanced Definition (960x720)": (960, 720),
    "High Definition (1280x960)": (1280, 960),
    "Full High Definition (1920x1080)": (1920, 1080),
    "Ultra HD (3840x2160)": (3840, 2160),
}

resolution_var = StringVar(root)
resolution_var.set("Original")

resolution_label = Label(root, text="Select Resolution:")
resolution_label.pack()

resolution_menu = OptionMenu(root, resolution_var, *resolutions.keys())
resolution_menu.pack()

# Add spacing
spacing_label = Label(root, text="")
spacing_label.pack()

# Quality Scale
quality_label = Label(root, text="Select Quality:")
quality_label.pack()

quality_scale = Scale(root, from_=1, to=100, orient="horizontal")
quality_scale.set(100)  # Default quality set to 100
quality_scale.pack()

convert_button = Button(root, text="Convert Images", command=convert_images)
convert_button.pack(pady=10)

status_label = Label(root, text="")
status_label.pack()

root.mainloop()
