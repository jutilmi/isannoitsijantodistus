"""This module includes common functions used in the project"""

import xml.etree.ElementTree as ET

def set_context_ref(root_element, context_ref=None):
    """Tämä funktio asettaa saman contextRef-arvon kaikille niille elementeille,
       joilla on kyseinen attribuutti.

       Keyword arguments:
       root_element                 -- etree.Elementree.Element, root element of the tree
       context_ref                  -- str, text string to be applied on the xml parameter

       Output:                      -- etree.ElementTree.Element
       """

    for i in root_element.iter():
        if i.get('contextRef', None) is not None:
            i.set('contextRef', context_ref)

    return root_element

def elements_to_element_tree(element_dict, parent_element, xml_definator):
    """This functions sets contextRef as an xml_definator to relevant elements in a tree.

       Keyword arguments:
       element_dict                 -- dict, dictionary of various keys
       root_element_tree            -- etree.ElementTree.ElementTree, specific element tree
       xml_definator                -- str, relevant definator to be applied

       Output:                       -- etree.ElementTree.ElementTree
       """


    if xml_definator[-1] != ':':
        xml_definator += ':'

    for key in element_dict:
        if element_dict[key] == 'stringItemType' or \
            element_dict[key] == 'booleanItemType' or \
            element_dict[key] == 'dateItemType' or \
            element_dict[key] == 'integerItemType':

            ET.SubElement(
                parent_element,
                xml_definator+key,
                attrib={
                    'contextRef' : ''
                    }
                )

        elif element_dict[key] == 'decimalItemType':
            ET.SubElement(
                parent_element,
                xml_definator+key,
                attrib={
                    'decimals' : '2',
                    'contextRef' : '',
                    'unitRef' : 'pure'
                    }
                )

        elif element_dict[key] == 'monetaryItemType':
            ET.SubElement(
                parent_element,
                xml_definator+key,
                attrib={
                    'decimals' : '2',
                    'contextRef' : '',
                    'unitRef' : 'EUR'
                    }
                )

        else:
            ET.SubElement(parent_element, xml_definator+key)

    return parent_element
