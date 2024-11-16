import bpy

# Define the name of the widget collection
widget_collection_name = "Collection_Name"

# Ensure the active object is an armature in pose mode
if bpy.context.object and bpy.context.object.type == 'ARMATURE':
    armature = bpy.context.object
    custom_objects = set()  # Set to store unique custom object names

    # Loop through each pose bone in the armature
    for pose_bone in armature.pose.bones:
        # Check if the bone has a custom object
        if pose_bone.custom_shape:
            custom_objects.add(pose_bone.custom_shape.name)  # Add the custom object's name

    # Find the widget collection
    widget_collection = bpy.data.collections.get(widget_collection_name)

    if widget_collection:
        # Create a list of objects to delete
        unused_objects = [obj for obj in widget_collection.objects if obj.name not in custom_objects]

        # Unlink objects from the collection first
        for obj in unused_objects:
            widget_collection.objects.unlink(obj)

        # Delete unused objects safely
        for obj in unused_objects:
            if obj.name in bpy.data.objects:
                bpy.data.objects.remove(obj, do_unlink=True)
                print(f"Deleted unused widget: {obj.name}")

        print("Cleanup completed.")
    else:
        print(f"Collection '{widget_collection_name}' not found.")
else:
    print("Please select an armature in Pose Mode.")
