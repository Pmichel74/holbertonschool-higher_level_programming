#!/usr/bin/python3
"""XML serialization module"""
import xml.etree.ElementTree as ET
import xml.dom.minidom


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format.
    Args:
        dictionary: The dictionary to serialize
        filename: The output file name
    """
    # Create root element
    root = ET.Element("data")

    # Add each key-value pair as a child element
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create XML tree
    tree = ET.ElementTree(root)

    # Convert tree to string
    xml_str = ET.tostring(root, encoding='unicode')

    # Use minidom to format XML nicely
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml_str = dom.toprettyxml(indent="  ")

    # Write formatted XML to file
    with open(filename, 'w') as f:
        f.write(pretty_xml_str)


def deserialize_from_xml(filename):
    """
    Deserialize XML file to Python dictionary.
    Args:
        filename: The XML file to read
    Returns:
        The reconstructed dictionary
    """
    # Read and parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Create dictionary from XML elements
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary


# Test code if run directly
if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
