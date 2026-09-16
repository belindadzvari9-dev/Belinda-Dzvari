#4. Memory-efficient CSV/text-file reader using a generator
#A 50GB file should not be loaded all at once because it can exceed available RAM. A generator reads only a small part of the file at a time and gives one complete line when needed.

def chunked_file_reader(file_path, chunk_size_bytes):
    """Read a large text file lazily and yield complete lines."""

    with open(file_path, "rb") as file:
        remaining = b""

        while True:
            chunk = file.read(chunk_size_bytes)

            # Stop when there is no more data
            if not chunk:
                break

            # Add unfinished data from the previous chunk
            data = remaining + chunk

            # Split only at complete line endings
            lines = data.split(b"\n")
            remaining = lines.pop()  # Keep incomplete last line

            # Yield each complete line
            for line in lines:
                yield line.decode("utf-8")

        # Yield the final line if it has no newline at the end
        if remaining:
            yield remaining.decode("utf-8")
#Example
for line in chunked_file_reader("large_file.csv", 1024 * 1024):
    print(line)

    #Explanation:
#- The file is opened in binary mode ("rb") so the chunk size is measured in bytes.
#- file.read(chunk_size_bytes) reads only a small block, for example 1 MB.
#- remaining stores an unfinished line at the end of a chunk.
#- When the next chunk is read, the unfinished text is joined with it.
#- The generator uses yield, so it returns one line at a time instead of keeping the whole file in memory.
#- This prevents broken or “torn” lines across chunk boundaries.
