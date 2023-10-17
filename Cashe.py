class Cashe:
    def __init__(self, size, cashe_lines, line_size):
        self.size = size
        self.cashe_lines = cashe_lines
        self.line_size = line_size
        self.enabled = False
        self.cashe_data = [None] * cashe_lines

    def enable_cashe(self):
        self.enable = True

    def disable_cashe(self):
        self.enable = False

    def flush_cashe(self):
        self.cashe_data = [None] * self.cashe_lines
            # Implement methods for cache read and write operations as needed


    def read_from_cashe(self, address):
        if not self.enabled:
            return None
        # Calculate the cache line index and offset within the cache line
        line_index = (address // self.line_size) % self.cache_lines
        offset = address % self.line_size

        # Check if the requested data is in the cache
        cache_line = self.cache_data[line_index]
        if cache_line is not None and cache_line['valid']:
            cached_data = cache_line['data'][offset]
            return cached_data

        # If the data is not in the cache, return None (cache miss)
        return None
        
    def write_to_cashe(self, address, data):
        if not self.enabled:
            return None
        # Implement cache write logic
        # Calculate the cache line index and offset within the cache line
        line_index = (address // self.line_size) % self.cache_lines
        offset = address % self.line_size

        # Update the cache data with the new data
        if self.cache_data[line_index] is None:
            self.cache_data[line_index] = {'valid': True, 'data': [None] * self.line_size}
        self.cache_data[line_index]['data'][offset] = data
