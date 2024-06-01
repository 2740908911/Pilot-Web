from flask import Blueprint, request
from lxml import etree
import responses

xxe = Blueprint('xxe', __name__)

# xxe
@xxe.route('/api/xxe/l1/xmldata', methods=['POST'])
@responses.check_post(['xml'])
def parse_xml():
    xml_data = request.form['xml']
    try:
        parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
        tree = etree.fromstring(xml_data, parser=parser)
        
        content = ''
        for elem in tree.iter():
            content += elem.tag + ': ' + (elem.text or '') + '\n'
        
        return responses.update_callback(responses.callback_public_getinfo, {"msg": content})
    except etree.XMLSyntaxError as e:
        return responses.update_callback(responses.callback_public_getinfo, {"msg": str(e)})

    
   
    