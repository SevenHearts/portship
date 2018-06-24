def unpack(f, spec):
    import struct
    size = struct.calcsize(spec)
    res = struct.unpack(spec, f.read(size))
    if len(res) == 1:
        return res[0]
    return res
