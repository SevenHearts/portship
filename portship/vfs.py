from .util import unpack

def _short_string(f):
    length = unpack(f, '<H')
    return f.read(length)[:-1].decode('utf-8', 'ignore') # length includes the null byte, which we don't want


class VFSEntry(object):
    def __init__(self, archive_path, path, offset, length, block_size, deleted, compressed, encrypted, version, crc):
        self.archive_path = archive_path
        self.path = path
        self.offset = offset
        self.length = length
        self.block_size = block_size
        self.deleted = deleted
        self.compressed = compressed
        self.encrypted = encrypted
        self.version = version
        self.crc = crc


class VFSFile(object):
    def __init__(self, idx):
        import os

        self.path = idx.name
        self.dirpath = os.path.dirname(self.path)
        self.entries = {}

        self.std_version, self.cur_version, entry_total = unpack(idx, '<iii')

        print('detected ROSE Online std={} cur={}'.format(self.std_version, self.cur_version))
        print('found {} VFS entries:'.format(entry_total))

        for i in range(entry_total):
            name = _short_string(idx)
            offset = unpack(idx, '<i')
            print('- entry: {} (at offset {})'.format(name, offset))

            pos = idx.tell()
            idx.seek(offset)

            entry_count, _, archive_offset = unpack(idx, '<iii') # second int is unused

            # note that in the official VFS implementation, their encrypt/decrypt
            # functions are blind buffer copies (they took out encryption altogether)
            # so it's largely uninteresting data.
            total_encrypted = 0
            total_compressed = 0
            total_deleted = 0

            for j in range(entry_count):
                f_path = _short_string(idx)
                f_offset, f_length, f_block_size, f_deleted, f_compressed, f_encrypted, f_version, f_crc = unpack(idx, '<iii???ii')

                entry = VFSEntry(name, f_path, f_offset, f_length, f_block_size, f_deleted, f_compressed, f_encrypted, f_version, f_crc)

                if f_path in self.entries:
                    print('  WARNING: skipping duplicate entry (may be from another archive): {}'.format(f_path))
                else:
                    self.entries[f_path] = entry

                if f_deleted:
                    total_deleted += 1
                if f_compressed:
                    total_compressed += 1
                if f_encrypted:
                    total_encrypted += 1


            print('  loaded {} entities'.format(entry_count))
            print('  deleted={} compressed={} encrypted={}'.format(total_deleted, total_compressed, total_encrypted))

            idx.seek(pos)

        print('finished processing IDX - {} entries discovered'.format(len(self.entries)))
