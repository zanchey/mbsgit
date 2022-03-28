#! python3

# mbsgit - transforms the Australian Medicare Benefits Schedule from XML to a git tree
#
# Copyright 2022 David Adam
# Licensed under the MIT license; see LICENSE for details
#
# SPDX-License-Identifier: MIT

import os
import xml.etree.ElementTree as ET


def node_to_dict(node: ET.Element):
    return {item.tag: (item.text.strip() if item.text else None) for item in node}


def write_item(output_path, item):
    filename = os.path.join(output_path, item["Group"], item["ItemNum"] + ".txt")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode="w") as f:
        f.write(repr(item))


def mbsgit(output_path="mbs_items"):
    tree = ET.parse("mbs.xml")
    root = tree.getroot()
    items = (node_to_dict(item) for item in root)
    # print([(item["ItemNum"], item["Description"]) for item in items])
    for item in items:
        write_item(output_path, item)


if __name__ == "__main__":
    mbsgit()
