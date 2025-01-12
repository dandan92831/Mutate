import os
import random
import subprocess
import xml.etree.ElementTree as ET
from html import unescape

def java_to_srcml(input_file, output_file):
    """Convert Java files to srcML XML"""
    subprocess.run(["srcml", input_file, "-o", output_file], check=True)

def srcml_to_java(input_file, output_file):
    """Convert srcML XML back to Java file"""
    subprocess.run(["srcml", input_file, "-o", output_file], check=True)

    # Rename the generated file to Sample.java
    if os.path.exists(output_file):
        os.rename(output_file, output_file)

        # Change the package name to after_mutating
        with open(output_file, "r") as file:
            content = file.read()

        content = content.replace("package initial;", "package after_mutating;")

        with open(output_file, "w") as file:
            file.write(content)

def mutate_binary_operator(xml_file, output_file):
    """Randomly replace binary operators in XML files"""
    # 定义二元操作符替换规则
    binary_operators = {
        ">": ["<", "==", ">=", "<="],
        "<": [">", "==", ">=", "<="],
        "==": ["!=", ">", "<"],
        "!=": ["==", ">", "<"],
        ">=": ["<", ">"],
        "<=": [">", "<"]
    }

    # Parse XML file and declare namespace
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get the namespace of srcML
    namespace = {"ns0": "http://www.srcML.org/srcML/src"}

    # Debug: Output the XML file content to confirm whether it is generated correctly
    print("Original XML:\n", ET.tostring(root, encoding='unicode'))

    # Find all namespaced <operator> tags
    replaced = False
    for operator in root.findall(".//ns0:operator", namespaces=namespace):
        # Decoding operators, e.g. converting &gt; to >
        decoded_operator = unescape(operator.text)
        if decoded_operator in binary_operators:
            original_operator = decoded_operator
            new_operator = random.choice(binary_operators[original_operator])
            operator.text = new_operator
            print(f"Replaced operator '{original_operator}' with '{new_operator}'")
            replaced = True
            break

    if not replaced:
        print("No binary operator found to replace.")

    # 保存变异后的 XML
    tree.write(output_file)

if __name__ == "__main__":
    # Enter the Java file and its path
    prefix_path = "/Users/phoebe/IdeaProjects/mutated1/" # Change this to your local path
    original_java_file = os.path.join(prefix_path, "java1/src/initial/Sample.java")
    xml_file = "data/Sample.xml"  # srcML The path to the XML file to be transformed
    mutated_xml_file = "data/Sample_mutated.xml"  # The mutated XML file path
    mutated_java_file = os.path.join(prefix_path, "java1/src/after_mutating/Sample.java")  # The mutated Java file path

    java_to_srcml(original_java_file, xml_file)

    mutate_binary_operator(xml_file, mutated_xml_file)

    if not os.path.exists(mutated_xml_file):
        print("No mutated file was generated. Exiting...")
        exit(1)

    srcml_to_java(mutated_xml_file, mutated_java_file)

    if not os.path.exists("/Users/phoebe/IdeaProjects/mutated1/java1/src/after_mutating/Sample.java"):
        print("No mutated Java file found. Exiting...")
        exit(1)
