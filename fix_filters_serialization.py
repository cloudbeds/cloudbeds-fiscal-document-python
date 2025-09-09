"""
Post-generation script to fix filters serialization in the OpenAPI-generated Python client.
This script automatically patches the getFiscalDocuments method to properly serialize
the filters parameter as form data instead of URL-encoded query parameter.
"""

import re
import sys
from pathlib import Path

def fix_filters_serialization():
    """Fix the filters serialization in the generated API client."""
    
    api_file = Path("cloudbeds_fiscal_document/api/fiscal_documents_api.py")
    
    if not api_file.exists():
        print(f"Error: {api_file} not found")
        return False
    
    print(f"Patching filters serialization in {api_file}...")
    
    # Read the current content
    content = api_file.read_text()
    
    # Pattern to find the problematic filters serialization
    old_pattern = r'(\s+if filters is not None:\s+\n\s+)(_query_params\.append\(\(\'filters\', filters\)\))'
    
    # New serialization logic
    new_serialization = r'''\1# Custom form serialization for filters
            if hasattr(filters, 'to_dict'):
                filters_dict = filters.to_dict()
                for key, value in filters_dict.items():
                    if value is not None:
                        if isinstance(value, list):
                            for item in value:
                                if hasattr(item, 'value'):  # Handle enums
                                    _query_params.append((key, item.value))
                                else:
                                    _query_params.append((key, item))
                        else:
                            if hasattr(value, 'value'):  # Handle enums
                                _query_params.append((key, value.value))
                            else:
                                _query_params.append((key, value))
            else:
                _query_params.append(('filters', filters))'''
    
    # Apply the fix
    new_content = re.sub(old_pattern, new_serialization, content, flags=re.MULTILINE)
    
    # Check if the replacement was successful
    if new_content == content:
        print("No filters serialization pattern found to replace")
        return True
    
    # Write the updated content back
    api_file.write_text(new_content)
    print("Successfully patched filters serialization!")
    return True

def main():
    """Main function."""
    success = fix_filters_serialization()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
