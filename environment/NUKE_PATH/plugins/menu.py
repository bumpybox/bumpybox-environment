import nuke
import nukescripts
import sys

# set default node values
try:
    nuke.knobDefault("Multiply.label", "[value value]")
    nuke.knobDefault("Read.localizationPolicy", 'on')
except Exception:
    import traceback
    traceback.print_exc()


def createShotRef():
    def addCSRPanel():
        global csrPanel
        csrPanel = create_shot_ref.CreateShotRefPanel()
        return csrPanel.addToPane()

    paneMenu = nuke.menu('Pane')
    paneMenu.addCommand('CreateShotRef', addCSRPanel)
    nukescripts.registerPanel('com.ohufx.CreateShotRef', addCSRPanel)
    print('SUCCESS: Added CreateShotRef panel.')


try:
    createShotRef()
except Exception:
    import traceback
    traceback.print_exc()


# shared_toolsets
# Setup your SharedToolSets folder here
if nuke.GUI:

    import shared_toolsets
    import autolife
    import oz_backdrop
    import animatedSnap3D
    import kensuke_scripts
    import build_kensuke_character_shadows
    import create_shot_ref
    from toggleLocalAll import toggleLocalAll

    import sb_convertCornerPin
    import sb_convertTracker
    import reduceKeyframes
    from autocrop_to_ramp import createAutocropRamp
    from autocrop_to_tracker import autocropToTracker
    from hold_frame_analyzer import holdFrameAnalyzer
    import W_scaleTree

    # global toolbar
    toolbar = nuke.menu("Nodes")

    def toolSetsFilenameFilter(filename):
        if nuke.env['WIN32']:
            # lowercase
            filename = filename.replace('D:', 'C:')
            filename = filename.replace('/Volumes/Project', 'P:')
        return filename

    def sharedToolSet(path, menu):
        # create global shared toolset
        shared_toolsets.setSharedToolSetsPath(path)
        shared_toolsets.addFileFilter(toolSetsFilenameFilter)
        shared_toolsets.createToolsetsMenu(menu)

    def sharedToolSetKK(path, menu):
        # create global shared toolset
        shared_toolsets_kk.setSharedToolSetsPath(path)
        shared_toolsets_kk.addFileFilter(toolSetsFilenameFilter)
        shared_toolsets_kk.createToolsetsMenu(menu)

    def autoLife():
        # autoLive on Rotoshapes. takes first and last keyframe for lifetime (roto node and rotoshpe have to be selected)
        toolbar.addCommand('autolife roto shape',
                           'autolife.autoLife()', 'alt+l', icon='Roto.png')

    def ozBackdrop():
        # oz backdrop
        nukescripts.autoBackdrop = oz_backdrop.autoBackdrop
        nuke.menu('Nodes').addCommand('Other/Backdrop',
                                      'oz_backdrop.autoBackdrop([],None,None)', 'alt+b', 'Backdrop.png')

        item_list = [item.name()
                     for item in nuke.menu('Nuke').menu('Edit').items()]
        index_number = item_list.index('Node')
        nuke.menu('Nuke').addCommand('Edit/Replace all old backdrops',
                                     'oz_backdrop.replaceOldBackdrops()', icon='Backdrop.png', index=index_number+1)

    def animatedSnap3DPlugin():
        animatedSnap3D.run()

    def bjorkScripts():
        # Add toolbar.
        sb_tools = toolbar.addMenu(
            "sb_Tools", icon="sb_tools.png")
        # Python scripts.
        sb_tools.addCommand("sb ConvertCornerPin",
                            "sb_convertCornerPin.sb_convertCornerPin()", "")
        sb_tools.addCommand("sb ConvertTracker",
                            "sb_convertTracker.sb_convertTracker()", "")

    def kensukeScripts():
        # Add toolbar.
        kk_tools = toolbar.addMenu(
            "kk_tools", icon="kensukes_kingdom_wave.png")

        kk_tools.addCommand("Build Kensuke",
                            "kensuke_scripts.build_kensuke(None)", "")
        # kk_tools.addCommand("Build Kensuke Shadows",
        #                     "build_kensuke_character_shadows.build_shadows(None, None, 110, 48)", "")
        kk_tools.addCommand("Autocrop Limit Write",
                            "kensuke_scripts.autocrop_framelimit_write()", "")
        kk_tools.addCommand("Hold Frame Analyzer",
                            "holdFrameAnalyzer()", "")
        kk_tools.addCommand("Create Autocrop Ramp",
                            "createAutocropRamp(None)", "")
        kk_tools.addCommand("Autocrop To Tracker",
                            "autocropToTracker(None)", "")
        kk_tools.addCommand("Toggle Localization All",
                            "toggleLocalAll()", "")
        kk_tools.addCommand("Create Shot Ref",
                            "createShotRef()", "")

    def richardFrazerScripts():
        m = nuke.menu('Animation')
        m.addCommand('Reduce Keyframes', "reduceKeyframes.doReduceKeyframes()")
        # scaletree nodes
        nuke.menu('Nuke').addCommand('Edit/Node/W_scaleTree',
                                     'W_scaleTree.scaleTreeFloatingPanel()', 'alt+`')

    # try adding all scripts
    try:
        autoLife()
        sharedToolSet(
            "G:/My Drive/library/Nuke/plugins/SharedToolSets", toolbar)
        ozBackdrop()
        animatedSnap3DPlugin()
        bjorkScripts()
        kensukeScripts()
        richardFrazerScripts()
    except Exception:
        import traceback
        traceback.print_exc()

    # nuke.pluginAddPath("Y:/my_petsaurus/work/comp/plugins/projectionist-master")
