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
        assert(isinstance(scene_or_mesh, trimesh.Trimesh))
        mesh = scene_or_mesh
    return mesh

# rest of code
mesh_cap1: trimesh.Trimesh = trimesh.load("lfd/examples/cup1.obj")
mesh_airplane: trimesh.Trimesh = as_mesh(trimesh.load("lfd/examples/airplane.obj"))
mesh_cap2: trimesh.Trimesh = as_mesh(trimesh.load("lfd/examples/cup2.obj"))
mesh_3dcafe: trimesh.Trimesh = as_mesh(trimesh.load("lfd/examples/3dcafe_a-10.obj"))

lfd_value: float = LightFieldDistance(verbose=True).get_distance(
    mesh_cap1, mesh_airplane
)
print(f'Between cup1 and airplane = {lfd_value}')

lfd_value: float = LightFieldDistance(verbose=True).get_distance(
    mesh_cap1, mesh_cap1
)
print(f'Between cup1 and cup1 = {lfd_value}')

lfd_value: float = LightFieldDistance(verbose=True).get_distance(
    mesh_airplane, mesh_airplane
)
print(f'Between airplane and airplane = {lfd_value}')

lfd_value: float = LightFieldDistance(verbose=True).get_distance(
    mesh_cap1, mesh_cap2
)
print(f'Between cup1 and cup2 = {lfd_value}')

lfd_value: float = LightFieldDistance(verbose=True).get_distance(
    mesh_airplane, mesh_3dcafe
)
print(f'Between airplane and 3dcafe = {lfd_value}')