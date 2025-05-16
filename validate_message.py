import json
import sys
from jsonschema import validate, ValidationError, SchemaError
from jsonschema.exceptions import best_match

# Ruta del esquema
SCHEMA_FILE = "schema/vap-message-schema.json"

def main(json_file_path):
    try:
        with open(SCHEMA_FILE, 'r') as schema_file:
            schema = json.load(schema_file)
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        validate(instance=data, schema=schema)
        print(f"✅ {json_file_path} is valid ✅")

    except FileNotFoundError:
        print("❌ File not found. Check the path.")
    except ValidationError as ve:
        print(f"❌ Validation error: {ve.message}")
        print(f"   ↳ Path: {' → '.join(map(str, ve.absolute_path))}")
        if ve.cause:
            print(f"   Cause: {ve.cause}")
    except SchemaError as se:
        print(f"❌ Schema error: {se.message}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_message.py <json_file_to_validate>")
    else:
        main(sys.argv[1])
