from tkinter import *
from tkinter import ttk
import os
import ctypes
import poke_api
import image_list

# Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Create image cache directory
image_cache_dir = os.path.join(script_dir, 'images')
if not os.path.isdir(image_cache_dir):
    os.makedir(image_cache_dir)
    return

# create the main winndow
root = Tk()
root.title("Pokemon Image Viewer")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(500, 600)


# Set the window icon
icon_path = os.path.join(script_dir, 'Poke-Ball.ico')
app_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
root.iconbitmap(icon_path)

# Put a frame on the GUI 
frame = ttk.Frame(root)
frame.grip(row=0, column=0, sticky=NSEW)
frame.columconfigure(0, weight=100)
frame.rowconfigure(0, weight=100)



# put image into frame
image_path = os.path.join(script_dir, 'logo.png')
img_logo = PhotoImage(file=image_path)
lbl_image = ttk.Label(frm_right, image=img_poke)
lbl_image.grid(padx=10, pady=10)

# put the pull-down list of pokemon names into the frame
pokemon_name_list = ('Windows', 'MacOS', 'Linux')
cbox_pokemon_names = ttk.Combobox(frame, values=pokemon_name_list, state='readonly')
cbox_pokemon_names.set("Select an Pokemon")
cbox_pokemon_names.grid(padx=10, pady=(10, 0))

def handle_pokemon_sel(event):
    sel_pokemon = cbox_pokemon_names.get()
    global image_path
    image_path = poke_api.download_pokemon_artwork(sel_pokemon, image_cache_dir)
    img_poke['file'] = image_path
    return

cbox_pokemon_names.bind('<<ComboboxSelected>>', handle_pokemon_sel)    

#put "set desktop" button into frame
def handle_set_desktop():
    image_lib.set_desktop_background_image(image_path)

btm_set_desktop = ttk.Button(frame, text='set as Desktop Image', command=handle_set_desktop)
btm_set_desktop.grip(padx=10, pady=(10,20))

# TODO: Put code here

root.mainloop()