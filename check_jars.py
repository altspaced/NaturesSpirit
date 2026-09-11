import zipfile, os, shutil
desktop = r'C:\Users\altsp\Desktop\NaturesSpirit-26.2\fabric\build\libs\natures_spirit-fabric-2.3.0+26.2.jar'
mods = r'C:\Users\altsp\AppData\Roaming\PrismLauncher\instances\26.2\minecraft\mods\natures_spirit-fabric-2.3.0+26.2.jar'
paths = [
    'data/natures_spirit/worldgen/configured_feature/aspen_tree.json',
    'data/natures_spirit/worldgen/configured_feature/compat_terralith_desert_sprinkle.json',
]
for label, path in [('desktop', desktop), ('mods', mods)]:
    print(label, 'exists', os.path.exists(path), 'size', os.path.getsize(path) if os.path.exists(path) else None, 'mtime', os.path.getmtime(path) if os.path.exists(path) else None)
    with zipfile.ZipFile(path) as z:
        for p in paths:
            t = z.read(p).decode()
            print(label, p.split('/')[-1], 'btp', 'below_trunk_provider' in t, 'random_patch', 'random_patch' in t, 'simple_block', 'simple_block' in t)
# install
shutil.copy2(desktop, mods)
print('copied desktop jar to mods')
# clear fabric processed cache for natures_spirit if present
cache = r'C:\Users\altsp\AppData\Roaming\PrismLauncher\instances\26.2\minecraft\.fabric\processedMods'
if os.path.isdir(cache):
    removed = 0
    for name in os.listdir(cache):
        if 'natures_spirit' in name.lower():
            os.remove(os.path.join(cache, name))
            removed += 1
            print('removed cache', name)
    print('cache removals', removed)
# verify mods after copy
with zipfile.ZipFile(mods) as z:
    t = z.read(paths[0]).decode()
    s = z.read(paths[1]).decode()
    print('after_copy btp', 'below_trunk_provider' in t, 'sprinkle_simple', 'simple_block' in s and 'random_patch' not in s)
