import json
from pymol import cmd
from pymol.cgo import * 
from pymol.cgo import COLOR, SPHERE
resn_1letter = {
    'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D',
    'CYS': 'C', 'GLU': 'E', 'GLN': 'Q', 'GLY': 'G',
    'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
    'MET': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S',
    'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'
}

"""
af2color json_file

Set colors for atoms in the loaded PDB file based on the atom_plddts values from the JSON file.
Parameters:
- `json_file`: Path to the JSON file containing the atom_plddts values

The JSON file is located in PyMOL's current working directory; otherwise, the full path is required.

--------------------------------------

show_residue_sphere residue_number,sph_radius,sph_color

show_residue_sphere, which adds a colored sphere at the position of a specified residue in the loaded structure. 

Input Parameters:
	residue_number: The residue number to mark with a sphere. Defaults to 1.
	sph_radius: The radius of the sphere. Defaults to 2.
	sph_color: The color of the sphere, provided as a space-separated RGB string (e.g., '1.0 0.0 0.0' for red).

"""


def af2color(json_file):

	with open(json_file, 'r') as f:
		data = json.load(f)
	plddts = data["atom_plddts"]
	atoms = cmd.get_model("all").atom
	if len(atoms) != len(plddts):
		print("Warning: The number of atoms does not match the number of plddts data!")
		return
	for i, atom in enumerate(atoms):
		plddt = plddts[i]
		if plddt >= 90:
			color_name = "neptunium"
		elif 70 <= plddt < 90:
			color_name = "cyan"
		elif 50 <= plddt < 70:
			color_name = "gold"
		else:
			color_name = "phosphorus"
		atom_selection = f"id {atom.index}"
		cmd.color(color_name, atom_selection)




def show_residue_sphere0(residue_number=1,sph_radius=2,sph_color='1.0 0.0 0.0'):
	print(sph_color)
	residue_number=int(residue_number)
	sph_radius=int(sph_radius)
	residue_number = max(residue_number,1)

	sph_colors = [float(color) for color in re.split(r'\s+',sph_color)]
	if max(sph_colors)>1:
		sph_colors=[1,0,0]	
	print(f'residue_number: {residue_number}\nsph_colors:{sph_colors}')	
	objects = cmd.get_object_list()
	if objects:
		chains = cmd.get_chains(objects[0])
		selection = f'chain {chains[0]} and resi {residue_number}'
		if cmd.count_atoms(selection) == 0:
			print(f"Error: The selected residue '{selection}' does not exist!")
		else:
			residue_xyzs = cmd.get_coords(selection, 1)
			x, y, z = residue_xyzs[0]
			sphere_name=f'residue_{chains[0]}_{residue_number}'
			if sphere_name in cmd.get_names():
				cmd.delete(sphere_name) 
				print(f"Existing object '{sphere_name}' has been deleted.")
			cmd.load_cgo([COLOR, sph_colors[0], sph_colors[1], sph_colors[2], SPHERE, x, y, z, sph_radius], sphere_name)
	else: 
		print("Error: No available structure objects found. Please load a structure first.")

def show_residue_sphere(residue_number=1, sph_radius=2, sph_color='1.0 0.0 0.0'):
    """
    Display a sphere at the position of a specific residue and label it with a 1-letter residue name.

    Parameters:
        residue_number (int): Residue number to highlight.
        sph_radius (float): Radius of the sphere.
        sph_color (str): RGB color string, e.g. '1.0 0.0 0.0' for red.
    """
    print(sph_color)
    residue_number = int(residue_number)
    sph_radius = float(sph_radius)
    residue_number = max(residue_number, 1)

    # Parse color string
    sph_colors = [float(color) for color in re.split(r'\s+', sph_color)]
    if max(sph_colors) > 1:
        sph_colors = [1.0, 0.0, 0.0]

    print(f'residue_number: {residue_number}\nsph_colors: {sph_colors}')
    objects = cmd.get_object_list()
    if objects:
        chains = cmd.get_chains(objects[0])
        selection = f'chain {chains[0]} and resi {residue_number}'
        if cmd.count_atoms(selection) == 0:
            print(f"Error: The selected residue '{selection}' does not exist!")
        else:
            # Get coordinates of the residue (center)
            residue_xyzs = cmd.get_coords(selection, 1)
            x, y, z = residue_xyzs[0]
            sphere_name = f'residue_{chains[0]}_{residue_number}'

            # Remove old sphere if it exists
            if sphere_name in cmd.get_names():
                cmd.delete(sphere_name)
                print(f"Existing object '{sphere_name}' has been deleted.")

            # Draw a CGO sphere
            cmd.load_cgo([
                COLOR, sph_colors[0], sph_colors[1], sph_colors[2],
                SPHERE, x, y, z, sph_radius
            ], sphere_name)

            # Get residue name and convert to 1-letter code
            stored.resn = 'UNK'
            cmd.iterate(selection + " and name CA", "stored.resn = resn")
            resn3 = stored.resn.upper()
            resn1 = resn_1letter.get(resn3, 'X')
            label_text = f"{resn1}{residue_number}"

            # Create a label (pseudoatom) slightly above the sphere
            label_name = f"label_{chains[0]}_{residue_number}"
            cmd.pseudoatom(label_name, pos=[x, y, z + sph_radius + 0.5], label=label_text)
            cmd.set("label_size", 14, label_name)
            cmd.set("label_color", "black", label_name)
    else:
        print("Error: No available structure objects found. Please load a structure first.")


def show_residue_stick(residue_number=1, stick_radius=0.25, stick_color='1.0 0.0 0.0'):
    """
    Display a specific residue using sticks and add a 1-letter residue label (e.g., D368).
    Parameters:
        residue_number: the residue number to highlight
        stick_radius: thickness of the stick
        stick_color: RGB string, e.g., '1.0 0.0 0.0' for red
    """
    residue_number = int(residue_number)
    stick_radius = float(stick_radius)
    residue_number = max(residue_number, 1)

    rgb = [float(c) for c in re.split(r'\s+', stick_color.strip())]
    if len(rgb) != 3 or max(rgb) > 1:
        rgb = [1.0, 0.0, 0.0]  # default to red

    objects = cmd.get_object_list()
    if not objects:
        print("❗ No structure loaded.")
        return

    chains = cmd.get_chains(objects[0])
    if not chains:
        print("❗ No chains found.")
        return

    chain = chains[0]
    selection = f"chain {chain} and resi {residue_number}"
    if cmd.count_atoms(selection) == 0:
        print(f"❌ Residue {residue_number} not found in chain {chain}.")
        return

    # Show sticks and apply color
    cmd.show("sticks", selection)
    color_name = f"custom_color_{residue_number}"
    cmd.set_color(color_name, rgb)
    cmd.color(color_name, selection)
    cmd.set("stick_radius", stick_radius, selection)

    # Get residue name and convert to 1-letter code
    stored.resn = 'UNK'
    cmd.iterate(selection + " and name CA", "stored.resn = resn")
    resn3 = stored.resn.upper()
    resn1 = resn_1letter.get(resn3, 'X')
    label_text = f"{resn1}{residue_number}"

    # Label the CA atom of the residue
    cmd.label(selection + " and name CA", f'"{label_text}"')
    cmd.set("label_size", 14, selection)
    cmd.set("label_color", "black", selection)  # ← updated to black font

    print(f"✅ Highlighted stick-style residue {label_text}.")

cmd.extend("show_residue_stick", show_residue_stick)
cmd.extend("show_residue_sphere", show_residue_sphere)
cmd.extend("show_residue_sphere0", show_residue_sphere0)
 
cmd.extend("af2color", af2color)




