import pymel.core as pm


# Quiet load alembic plugins
print "Loading Alembic plugins."
pm.loadPlugin('AbcExport.mll', quiet=True)
pm.loadPlugin('AbcImport.mll', quiet=True)
