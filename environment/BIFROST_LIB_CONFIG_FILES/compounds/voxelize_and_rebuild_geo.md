# `voxelize_and_rebuild_geo`

Voxelizes the input geometry and reconstructs it using the contour_dual_marching_cube algorithm.  Use this to quickly rebuild
invalid geometry (such as those with n-gons, holes, lamina faces, and nonmanifold geometry) into valid geometry.

## Inputs

### `geometry`

The object to be voxelized and rebuilt.

### `detail_size`

The resolution of the voxelization.  Lower values result in higher detail.

### `resolution_mode`

Determines the units of detail_size.

## Output

### `mesh`

A rebuilt version of the input mesh.








