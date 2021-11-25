# `extrude`

Extrude faces on a given object in the board. Output is mesh object/s depending on the input object/s.

## Inputs

### `in_object`

Connect one or array of objects that will be used to perform an extrude function on their faces.


### `Transform Properties`

These settings apply to the base mesh and never to the extruded faces.

### `scale_object`

Scale of the base bif object generated in the board.

### `scale_faces`

Scale of the individual faces on the base bif object.

### `rotate_faces`

Rotation of the individual faces on the base bif object.


### `Extrude Properties`

These settings apply to the extruded faces.

### `enable`

Turn off to disable extrusion.

### `offset_ext_faces`

Extrusion amount. distance between the extruded faces to the base object.

### `scale_ext_faces`

Scale of the extruded faces.

### `scale_ext_faces`

Rotation of the extruded faces.


### `Influencer Properties`

Influencer settings apply the extrude function to a portion of the geometry if enabled, based on the dropoff distance.
influencer does not evaluate collisions or geometry shapes. It works based on a single position in space and a dropoff radius from that point.

### `enable`

Turn on to use the influencer options.

### `influencer_location`

Location in space used as an influencer. 

### `dropoff`

Distance used for the amound of extrude applied to the object. 









