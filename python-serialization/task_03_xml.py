#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML format and save it to a file."""
    # Create the root element correctly
    root = ET.Element('data')
    
    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    # Create and write the tree
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML data from a file into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    
    result = {}
    for child in root:
git         # Get each child's tag as key and text as value
        result[child.tag] = child.text
    
    return result
