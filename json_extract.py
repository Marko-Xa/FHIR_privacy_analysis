def json_extract(obj, key):
    """Extract values from nested JSON by key."""
    
    result = []

    def extract(obj, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, key)
                elif k == key:
                    result.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, key)

    extract(obj, key)
    return result