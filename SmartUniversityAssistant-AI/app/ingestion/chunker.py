def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 150
) -> list[str]:

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid overlap")

    if not text or not text.strip():
        return []

    # Split text into non-empty lines
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    # Split exceptionally long lines into word groups
    normalized_lines = []

    for line in lines:
        if len(line) <= chunk_size:
            normalized_lines.append(line)
            continue

        words = line.split()
        current = ""

        for word in words:
            candidate = f"{current} {word}".strip()

            if len(candidate) > chunk_size and current:
                normalized_lines.append(current)
                current = word
            else:
                current = candidate

        if current:
            normalized_lines.append(current)

    chunks = []
    current_lines = []
    current_length = 0

    for line in normalized_lines:

        line_length = len(line) + 1

        if current_lines and current_length + line_length > chunk_size:

            chunks.append("\n".join(current_lines))

            # Preserve previous lines within the overlap budget
            overlap_lines = []
            overlap_length = 0

            for previous_line in reversed(current_lines):
                previous_length = len(previous_line) + 1

                if overlap_length + previous_length > overlap:
                    break

                overlap_lines.insert(0, previous_line)
                overlap_length += previous_length

            current_lines = overlap_lines
            current_length = overlap_length

        current_lines.append(line)
        current_length += line_length

    if current_lines:
        chunks.append("\n".join(current_lines))

    return chunks
