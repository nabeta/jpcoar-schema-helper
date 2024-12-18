#!/usr/bin/env python3
import sys
import yaml
from xml.dom import minidom
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

def resource_type_uri(string):
  match string:
    case "conference paper":
      return "http://purl.org/coar/resource_type/c_5794"
    case "data paper":
      return "http://purl.org/coar/resource_type/c_beb9"
    case "departmental bulletin paper":
      return "http://purl.org/coar/resource_type/c_6501"
    case "editorial":
      return "http://purl.org/coar/resource_type/c_b239"
    case "journal":
      return "http://purl.org/coar/resource_type/c_0640"
    case "journal article":
      return "http://purl.org/coar/resource_type/c_6501"
    case "newspaper":
      return "http://purl.org/coar/resource_type/c_2fe3"
    case "review article":
      return "http://purl.org/coar/resource_type/c_dcae04bc"
    case "other periodical":
      return "http://purl.org/coar/resource_type/QX5C-AR31"
    case "software paper":
      return "http://purl.org/coar/resource_type/c_7bab"
    case "article":
      return "http://purl.org/coar/resource_type/c_6501"
    case "book":
      return "http://purl.org/coar/resource_type/c_2f33"
    case "book part":
      return "http://purl.org/coar/resource_type/c_3248"
    case "cartographic material":
      return "http://purl.org/coar/resource_type/c_12cc"
    case "map":
      return "http://purl.org/coar/resource_type/c_12cd"
    case "conference output":
      return "http://purl.org/coar/resource_type/c_c94f"
    case "conference presentation":
      return "http://purl.org/coar/resource_type/R60J-J5BD"
    case "conference proceedings":
      return "http://purl.org/coar/resource_type/c_f744"
    case "conference poster":
      return "http://purl.org/coar/resource_type/c_6670"
    case "aggregated data":
      return "http://purl.org/coar/resource_type/ACF7-8YT9"
    case "clinical trial data":
      return "http://purl.org/coar/resource_type/c_cb28"
    case "compiled data":
      return "http://purl.org/coar/resource_type/FXF3-D3G7"
    case "dataset":
      return "http://purl.org/coar/resource_type/c_ddb1"
    case "encoded data":
      return "http://purl.org/coar/resource_type/AM6W-6QAW"
    case "experimental data":
      return "http://purl.org/coar/resource_type/63NG-B465"
    case "genomic data":
      return "http://purl.org/coar/resource_type/A8F1-NPV9"
    case "geospatial data":
      return "http://purl.org/coar/resource_type/2H0M-X761"
    case "laboratory notebook":
      return "http://purl.org/coar/resource_type/H41Y-FW7B"
    case "measurement and test data":
      return "http://purl.org/coar/resource_type/DD58-GFSX"
    case "observational data":
      return "http://purl.org/coar/resource_type/FF4C-28RK"
    case "recorded data":
      return "http://purl.org/coar/resource_type/CQMR-7K63"
    case "simulation data":
      return "http://purl.org/coar/resource_type/W2XT-7017"
    case "survey data":
      return "http://purl.org/coar/resource_type/NHD0-W6SY"
    case "image":
      return "http://purl.org/coar/resource_type/c_c513"
    case "still image":
      return "http://purl.org/coar/resource_type/c_ecc8"
    case "moving image":
      return "http://purl.org/coar/resource_type/c_8a7e"
    case "video":
      return "http://purl.org/coar/resource_type/c_12ce"
    case "lecture":
      return "http://purl.org/coar/resource_type/c_8544"
    case "design patent":
      return "http://purl.org/coar/resource_type/C53B-JCY5"
    case "patent":
      return "http://purl.org/coar/resource_type/c_15cd"
    case "PCT application":
      return "http://purl.org/coar/resource_type/SB3Y-W4EH"
    case "plant patent":
      return "http://purl.org/coar/resource_type/Z907-YMBB"
    case "plant variety protection":
      return "http://purl.org/coar/resource_type/GPQ7-G5VE"
    case "software patent":
      return "http://purl.org/coar/resource_type/MW8G-3CR8"
    case "trademark":
      return "http://purl.org/coar/resource_type/H6QP-SC1X"
    case "utility model":
      return "http://purl.org/coar/resource_type/9DKX-KSAF"
    case "report":
      return "http://purl.org/coar/resource_type/c_93fc"
    case "research report":
      return "http://purl.org/coar/resource_type/c_18ws"
    case "technical report":
      return "http://purl.org/coar/resource_type/c_18gh"
    case "policy report":
      return "http://purl.org/coar/resource_type/c_186u"
    case "working paper":
      return "ihttp://purl.org/coar/resource_type/c_8042"
    case "data management plan":
      return "http://purl.org/coar/resource_type/c_ab20"
    case "sound":
      return "http://purl.org/coar/resource_type/c_18cc"
    case "thesis":
      return "http://purl.org/coar/resource_type/c_46ec"
    case "bachelor thesis":
      return "http://purl.org/coar/resource_type/c_7a1f"
    case "master thesis":
      return "http://purl.org/coar/resource_type/c_bdcc"
    case "doctoral thesis":
      return "http://purl.org/coar/resource_type/c_db06"
    case "commentary":
      return "http://purl.org/coar/resource_type/D97F-VB57"
    case "design":
      return "http://purl.org/coar/resource_type/542X-3S04"
    case "industrial design":
      return "http://purl.org/coar/resource_type/JBNF-DYAD"
    case "interactive resource":
      return "http://purl.org/coar/resource_type/c_e9a0"
    case "layout design":
      return "http://purl.org/coar/resource_type/BW7T-YM2G"
    case "learning object":
      return "http://purl.org/coar/resource_type/c_e059"
    case "manuscript":
      return "http://purl.org/coar/resource_type/c_0040"
    case "musical notation":
      return "http://purl.org/coar/resource_type/c_18cw"
    case "peer review":
      return "http://purl.org/coar/resource_type/H9BQ-739P"
    case "research proposal":
      return "http://purl.org/coar/resource_type/c_baaf"
    case "research protocol":
      return "http://purl.org/coar/resource_type/YZ1N-ZFT9"
    case "software":
      return "http://purl.org/coar/resource_type/c_5ce6"
    case "source code":
      return "http://purl.org/coar/resource_type/QH80-2R4E"
    case "technical documentation":
      return "http://purl.org/coar/resource_type/c_71bd"
    case "transcription":
      return "http://purl.org/coar/resource_type/6NC7-GK9S"
    case "workflow":
      return "http://purl.org/coar/resource_type/c_393c"
    case "other":
      return "http://purl.org/coar/resource_type/c_1843"

def text_version_uri(string):
  match string:
    case "AO":
      return "http://purl.org/coar/version/c_b1a7d7d4d402bcce"
    case "SMUR":
      return "http://purl.org/coar/version/c_71e4c1898caa6e32"
    case "AM":
      return "http://purl.org/coar/version/c_ab4af688f83e57aa"
    case "P":
      return "http://purl.org/coar/version/c_fa2ee174bc00049f"
    case "VoR":
      return "http://purl.org/coar/version/c_970fb48d4fbd8a85"
    case "CVoR":
      return "http://purl.org/coar/version/c_e19f295774971610"
    case "EVoR":
      return "http://purl.org/coar/version/c_dc82b40f9837b551"
    case "NA":
      return "http://purl.org/coar/version/c_be7fb7dd8ff6fe43"

def jpcoar_identifier_type(string):
  url = urlparse(string)
  match url.hostname.lower():
    case "doi.org":
      return "DOI"
    case "dx.doi.org":
      return "DOI"
    case "hdl.handle.net":
      return "HDL"
    case _:
      return "URI"

with open(sys.argv[1]) as file:
  entry = yaml.load(file, Loader = yaml.Loader)

ns = {
  "jpcoar": "https://github.com/JPCOAR/schema/blob/master/2.0/",
  "dc": "http://purl.org/dc/elements/1.1/",
  "dcterms": "http://purl.org/dc/terms/",
  "datacite": "https://schema.datacite.org/meta/kernel-4/",
  "oaire": "http://namespace.openaire.eu/schema/oaire/",
  "dcndl": "http://ndl.go.jp/dcndl/terms/",
  "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
  "xsi": "http://www.w3.org/2001/XMLSchema-instance"
}

for key in ns.keys():
  ET.register_namespace(key, ns[key])

root = ET.Element(ET.QName(ns["jpcoar"], "jpcoar"))
root.set(ET.QName(ns["xsi"], "schemaLocation"), "https://github.com/JPCOAR/schema/blob/master/2.0/ jpcoar_scm.xsd")

for title in entry["title"]:
  elem_title = ET.SubElement(root, ET.QName(ns["dc"], "title"))
  elem_title.text = title["title"]
for creator in entry["creator"]:
  elem_creator = ET.SubElement(root, ET.QName(ns["jpcoar"], "creator"), {"creatorType": "著"})
  for name_identifier in creator["name_identifier"]:
    elem_name_identifier = ET.SubElement(elem_creator, ET.QName(ns["jpcoar"], "nameIdentifier"), {
      "nameIdentifierScheme": name_identifier["identifier_scheme"],
      "nameIdentifierURI": name_identifier["identifier"]
    })
    elem_name_identifier.text = name_identifier["identifier"]
  for creator_name in creator["creator_name"]:
    elem_creator_name = ET.SubElement(elem_creator, ET.QName(ns["jpcoar"], "creatorName"), {"xml:lang": creator_name["lang"]})
    elem_creator_name.text = creator_name["name"]
  for affiliation in creator["affiliation"]:
    elem_affiliation = ET.SubElement(elem_creator, ET.QName(ns["jpcoar"], "affiliation"))
    elem_affiliation_identifier = ET.SubElement(elem_affiliation, ET.QName(ns["jpcoar"], "nameIdentifier"), {
      "nameIdentifierScheme": affiliation["identifier_scheme"],
      "nameIdentifierURI": affiliation["identifier"]
    })
    elem_affiliation_identifier.text = affiliation["identifier"]
    for affiliation_name in affiliation["affiliation_name"]:
      elem_affiliation_name = ET.SubElement(elem_affiliation, ET.QName(ns["jpcoar"], "affiliationName"), {"xml:lang": affiliation_name["lang"]})
      elem_affiliation_name.text = affiliation_name["name"]

elem_access_rights = ET.SubElement(root, ET.QName(ns["dcterms"], "accessRights"))
elem_access_rights.text = entry["access_rights"]

if entry.get("rights"):
  for rights in entry["rights"]:
    elem_rights = ET.SubElement(root, ET.QName(ns["dc"], "rights"), {
      "xml:lang": rights["lang"],
      ET.QName(ns["rdf"], "resource"): rights["rights"]
    })
    elem_rights.text = rights["rights"]

for subject in entry["subject"]:
  elem_subject = ET.SubElement(root, ET.QName(ns["jpcoar"], "subject"), {
    "xml:lang": subject["lang"],
    "subjectScheme": subject["subject_scheme"]
  })
  elem_subject.text = subject["subject"]

for publisher in entry["publisher"]:
  elem_publisher = ET.SubElement(root, ET.QName(ns["dc"], "publisher"), {"xml:lang": publisher["lang"]})
  elem_publisher.text = publisher["publisher"]

for date in entry["date"]:
  elem_date = ET.SubElement(root, ET.QName(ns["datacite"], "date"), {"dateType": date["date_type"]})
  elem_date.text = str(date["date"])

for language in entry["language"]:
  elem_language = ET.SubElement(root, ET.QName(ns["dc"], "language"))
  elem_language.text = language

elem_resource_type = ET.SubElement(root, ET.QName(ns["dc"], "type"), {
  ET.QName(ns["rdf"], "resource"): resource_type_uri(entry["type"])
})
elem_resource_type.text = entry["type"]

if entry.get("text_version"):
  elem_text_version = ET.SubElement(root, ET.QName(ns["oaire"], "version"), {
    ET.QName(ns["rdf"], "resource"): text_version_uri(entry["text_version"])
  })
  elem_text_version.text = entry["text_version"]

for identifier in entry["identifier"]:
  elem_identifier = ET.SubElement(root, ET.QName(ns["jpcoar"], "identifier"), {"identifierType": jpcoar_identifier_type(identifier)})
  elem_identifier.text = identifier

if entry.get("identifier_registration"):
  elem_identifier_registration = ET.SubElement(root, ET.QName(ns["jpcoar"], "identifierRegistration"), {
    "identifierType": entry["identifier_registration"]["identifier_type"]
  })
  elem_identifier_registration.text = entry["identifier_registration"]["identifier"]

if entry.get("relation"):
  for relation in entry["relation"]:
    elem_relation = ET.SubElement(root, ET.QName(ns["jpcoar"], "relation"), {
      "relationType": relation["relation_type"]
    })
    for related_identifier in relation["related_identifier"]:
      elem_related_identifier = ET.SubElement(elem_relation, ET.QName(ns["jpcoar"], "relatedIdentifier"), {"identifierType": jpcoar_identifier_type(related_identifier)})
      elem_related_identifier.text = related_identifier

for funding_reference in entry["funding_reference"]:
  elem_funding_reference = ET.SubElement(root, ET.QName(ns["jpcoar"], "fundingReference"))
  elem_funder_identifier = ET.SubElement(elem_funding_reference, ET.QName(ns["jpcoar"], "funderIdentifier"), {
    "funderIdentifierType": funding_reference["funder_identifier_type"]
  })
  elem_funder_identifier.text = funding_reference["funder_identifier"]
  elem_funder_name = ET.SubElement(elem_funding_reference, ET.QName(ns["jpcoar"], "funderName"), {
    "xml:lang": funding_reference["funder_name"]["lang"]
  })
  elem_funder_name.text = funding_reference["funder_name"]["funder_name"]
  elem_funding_stream = ET.SubElement(elem_funding_reference, ET.QName(ns["jpcoar"], "fundingStream"), {
    "xml:lang": funding_reference["funding_stream"]["lang"]
  })
  elem_funding_stream.text = funding_reference["funding_stream"]["funding_stream"]

  elem_award_number = ET.SubElement(elem_funding_reference, ET.QName(ns["jpcoar"], "awardNumber"), {
    "awardURI": funding_reference["award_number"]["award_uri"],
    "awardNumberType": funding_reference["award_number"]["award_number_type"]
   })
  elem_award_number.text = funding_reference["award_number"]["award_number"]

  elem_award_title = ET.SubElement(elem_funding_reference, ET.QName(ns["jpcoar"], "awardTitle"), {
    "xml:lang": funding_reference["award_title"]["lang"]
  })
  elem_award_title.text = funding_reference["award_title"]["award_title"]

for source_identifier in entry["source_identifier"]:
  elem_source_identifier = ET.SubElement(root, ET.QName(ns["jpcoar"], "sourceIdentifier"), {"identifierType": source_identifier["identifier_type"]})
  elem_source_identifier.text = source_identifier["source_identifier"]

for source_title in entry["source_title"]:
  elem_source_title = ET.SubElement(root, ET.QName(ns["jpcoar"], "sourceTitle"), {"xml:lang": source_title["lang"]})
  elem_source_title.text = source_title["source_title"]

volume = ET.SubElement(root, ET.QName(ns["jpcoar"], "volume"))
volume.text = entry["volume"]

issue = ET.SubElement(root, ET.QName(ns["jpcoar"], "issue"))
issue.text = entry["issue"]

num_pages = ET.SubElement(root, ET.QName(ns["jpcoar"], "numPages"))
num_pages.text = str(entry["num_pages"])

page_start = ET.SubElement(root, ET.QName(ns["jpcoar"], "pageStart"))
page_start.text = entry["page_start"]

page_end = ET.SubElement(root, ET.QName(ns["jpcoar"], "pageEnd"))
page_end.text = entry["page_end"]

if entry.get("file"):
  for file in entry["file"]:
    elem_file = ET.SubElement(root, ET.QName(ns["jpcoar"], "file"))
    elem_file_uri = ET.SubElement(
      elem_file,
      ET.QName(ns["jpcoar"], "URI"),
      {
        "objectType": file["object_type"],
        "label": file["label"]
      }
    )
    elem_file_uri.text = file["uri"]

    for extent in file["extent"]:
      elem_file_extent = ET.SubElement(elem_file, ET.QName(ns["jpcoar"], "extent"))
      elem_file_extent.text = extent

    for date in file["date"]:
      elem_file_date = ET.SubElement(elem_file, ET.QName(ns["datacite"], "date"), {"dateType": date["date_type"]})
      elem_file_date.text = str(date["date"])

ET.indent(root, space = "  ", level = 0)
print(ET.tostring(root, encoding = "unicode", xml_declaration = True))