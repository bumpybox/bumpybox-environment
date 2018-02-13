import nuke

# Create menu
menubar = nuke.menu("Nuke")
menu = menubar.addMenu("Bumpybox")

cmd = "from bumpybox_environment.nuke import setup;"
cmd += "setup.import_full_resolution_movie()"
menu.addCommand("Import Movie (Full)", cmd)
