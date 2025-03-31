import re


def split_markdown_by_spans(markdown_text):
    # Pattern to match span tags with their IDs
    span_pattern = r'<span id="([^"]+)"></span>'
    
    # Find all span positions and their IDs
    span_matches = list(re.finditer(span_pattern, markdown_text))
    
    # If no spans found, return empty dict
    if not span_matches:
        return {}
    
    # Create dictionary to store chunks
    chunks = {}
    
    # Process each span and extract the text until the next span (or end of text)
    for i, match in enumerate(span_matches):
        span_id = match.group(1)  # Extract the ID
        start_pos = match.end()   # Position right after the span tag
        
        # If this is not the last span, get text until next span
        if i < len(span_matches) - 1:
            end_pos = span_matches[i + 1].start()
        else:
            end_pos = len(markdown_text)
        
        # Extract text and store in dictionary with span ID as key
        chunk_text = markdown_text[start_pos:end_pos].strip()
        chunks[span_id] = chunk_text
    
    return chunks



