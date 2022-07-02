'kved parser'
import json


def form_dict(sec_i, div_i, gr_i, cl_i, data):
    """
    Forms a nested dictionary with a following structure
    {
  "name": "<class_name>",
  "type": "class"
  "parent": {
    "name": "<group_name>",
    "type": "group",
    "num_children": <0>,
    "parent": {
      "name": "<division_name>",
      "type": "division"
      "num_children": <0>,
      "parent": {
        "name": "<section_name>",
        "type": "section"
        "num_children": <0>
      }
    }
  }
}
    :param sec_i: int
    :param div_i: int
    :param gr_i: int
    :param cl_i: int
    :param data: deserialized data from json file
    :return: dict
    """
    class_name = data[sec_i]['divisions'][div_i]['groups'][gr_i]['classes'][cl_i]['className']
    group_name = data[sec_i]['divisions'][div_i]['groups'][gr_i]['groupName']
    group_childs = len(data[sec_i]['divisions'][div_i]['groups'][gr_i]['classes'])
    division_name = data[sec_i]['divisions'][div_i]['divisionName']
    division_childs = len(data[sec_i]['divisions'][div_i]['groups'])
    section_name = data[sec_i]['sectionName']
    section_childs = len(data[sec_i]['divisions'])
    output = {  "name": class_name,
                "type": "class",
                "parent": {
                            "name": group_name,
                            "type": "group",
                            "num_children": group_childs,
                            "parent": {
                                        "name": division_name,
                                        "type": "division",
                                        "num_children": division_childs,
                                        "parent": {
                                                    "name": section_name,
                                                    "type": "section",
                                                    "num_children": section_childs
                                                    }
                                        }
                          }
                }
    return output

def parse_kved(class_code):
    """
    Parses text kved and saves JSON file 'kved_results.json' in root project directory
    :param class_code: string, e.g '46.13'
    :return: None
    >>> parse_kved('46.13')

    """
    set_division_code  = class_code[:2]
    set_group_code = class_code[:4]
    result_dict = None
    with open('kved.json', 'r', encoding='utf-8') as file:
        data = (json.load(file))['sections'][0]
        for sec_i in range(len(data)):
            for div_i in range(len(data[sec_i]['divisions'])):
                if data[sec_i]['divisions'][div_i]['divisionCode'] == set_division_code:
                    for gr_i in range(len(data[sec_i]['divisions'][div_i]['groups'])):
                        if data[sec_i]['divisions'][div_i]['groups'][gr_i]['groupCode'] == set_group_code:
                            for cl_i in range(len(data[sec_i]['divisions'][div_i]['groups'][gr_i]['classes'])):
                                if data[sec_i]['divisions'][div_i]['groups'][gr_i]['classes'][cl_i]['classCode'] == class_code:
                                    result_dict = form_dict(sec_i, div_i, gr_i, cl_i, data)
    with open('kved_results.json', 'w', encoding='utf-8') as file:
        json.dump(result_dict, file, ensure_ascii=False, indent=4)
import doctest
doctest.testmod()
print(parse_kved('46.13'))