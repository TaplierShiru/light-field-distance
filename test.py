from lfd import LightFieldDistance
import trimesh

def as_mesh(scene_or_mesh):
    """
    Convert a possible scene to a mesh.

    If conversion occurs, the returned mesh has only vertex and face data.
    """
    if isinstance(scene_or_mesh, trimesh.Scene):
        if len(scene_or_mesh.geometry) == 0:
            mesh = None  # empty scene
        else:
            # we lose texture information here
            mesh = trimesh.util.concatenate(
                tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                    for g in scene_or_mesh.geometry.values()))
    else:
        assert(isinstance(mesh, trimesh.Trimesh))
        mesh = scene_or_mesh
    return mesh

# rest of code
mesh_1: trimesh.Trimesh = trimesh.load("lfd/examples/cup1.obj")
mesh_2: trimesh.Trimesh = as_mesh(trimesh.load("lfd/examples/airplane.obj"))

lfd_value: float = LightFieldDistance(verbose=True).get_distance(
    mesh_1.vertices, mesh_1.faces,
    mesh_2.vertices, mesh_2.faces
)
print(f'Between cup1 and airplane = {lfd_value}')

mesh_1: trimesh.Trimesh = trimesh.load("lfd/examples/cup1.obj")
mesh_2: trimesh.Trimesh = trimesh.load("lfd/examples/cup1.obj")

lfd_value: float = LightFieldDistance(verbose=True).get_distance(
    mesh_1.vertices, mesh_1.faces,
    mesh_2.vertices, mesh_2.faces
)
print(f'Between cup1 and cup1 = {lfd_value}')

mesh_1: trimesh.Trimesh = as_mesh(trimesh.load("lfd/examples/airplane.obj"))
mesh_2: trimesh.Trimesh = as_mesh(trimesh.load("lfd/examples/airplane.obj"))

lfd_value: float = LightFieldDistance(verbose=True).get_distance(
    mesh_1.vertices, mesh_1.faces,
    mesh_2.vertices, mesh_2.faces
)
print(f'Between airplane and airplane = {lfd_value}')