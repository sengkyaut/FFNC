from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import os
from tkinter import filedialog
from tkinter import Frame, Label
from tkinter.font import Font, nametofont
from tkinter.ttk import Treeview, Style


zawgyiRegex="\u103a[\u1000-\u102A]\u1039|\u1031[\u1078-\u1084]|[^\u1015\u103a\u100b\u1014\u1000\u1019\u100f\u100d]\u1039|[\u1060-\u1097][\u1000-\u102A]|[\u1000-\u102A][\u1060-\u1097]|\u1031\u103B|^\u1031|^\u103B|[\u1022-\u1030\u1032-\u1039\u103B-\u103D\u1040-\u104F]\u103B|\u1039$|\u103D\u103C|\u103B\u103C|[\u1000-\u1021]\u1039[\u101A\u101B\u101D\u101F\u1022-\u102A\u1031\u1037-\u1039\u103B\u1040-\u104F]|\u102E[\u102D\u103E\u1032]|\u1032[\u102D\u102E]|[\u1090-\u1099][\u102B-\u1030\u1032\u1037\u103C-\u103E]|[\u1000-\u102A]\u103A[\u102C-\u102E\u1032-\u1036]|[\u1023-\u1030\u1032-\u1039\u1040-\u104F]\u1031|[\u107E-\u1084][\u1001\u1003\u1005-\u100F\u1012-\u1014\u1016-\u1018\u101F]|\u1025\u1039|[\u1081\u1083]\u108F|\u108F[\u1060-\u108D]|[\u102D-\u1030\u1032\u1036\u1037]\u1039|\u102C\u1039|\u101B\u103C|[^\u1040-\u1049]\u1040\u102D|\u1031?\u1040[\u102B\u105A\u102E-\u1030\u1032\u1036-\u1038]|\u1031?\u1047[\u102C-\u1030\u1032\u1036-\u1038]|[\u102F\u1030\u1032]\u1094|\u1039[\u107E-\u1084]"
pattern = re.compile(zawgyiRegex)

# ===============================================================================#
# to convert (zawgyi-unicode)

import json,re,sys

def uni2zg(unicode):
    json_data = '[ { "from": "\\u1004\\u103a\\u1039", "to": "\\u1064" }, { "from": "\\u1039\\u1010\\u103d", "to": "\\u1096" }, { "from": "\\u102b\\u103a", "to": "\\u105a" }, { "from": "\\u100b\\u1039\\u100c", "to": "\\u1092" }, { "from": "\\u102d\\u1036", "to": "\\u108e" }, { "from": "\\u104e\\u1004\\u103a\\u1038", "to": "\\u104e" }, { "from": "[\\u1025\\u1009](?=[\\u1039\\u102f\\u1030])", "to": "\\u106a" }, { "from": "[\\u1025\\u1009](?=[\\u1037]?[\\u103a])", "to": "\\u1025" }, { "from": "\\u100a(?=[\\u1039\\u103d])", "to": "\\u106b" }, { "from": "(\\u1039[\\u1000-\\u1021])(\\u102D){0,1}\\u102f", "to": "\\\\1\\\\2\\u1033" }, { "from": "(\\u1039[\\u1000-\\u1021])\\u1030", "to": "\\\\1\\u1034" }, { "from": "\\u1014(?=[\\u102d\\u102e\\u102f\\u103A]?[\\u1030\\u103d\\u103e\\u102f\\u1039])", "to": "\\u108f" }, { "from": "\\u1014(?=\\u103A\\u102F )", "to": "\\u108f" }, { "from" : "\\u1014\\u103c", "to" : "\\u108f\\u103c" }, { "from": "\\u1039\\u1000", "to": "\\u1060" }, { "from": "\\u1039\\u1001", "to": "\\u1061" }, { "from": "\\u1039\\u1002", "to": "\\u1062" }, { "from": "\\u1039\\u1003", "to": "\\u1063" }, { "from": "\\u1039\\u1005", "to": "\\u1065" }, { "from": "\\u1039\\u1006", "to": "\\u1066" }, { "from": "\\u1039\\u1007", "to": "\\u1068" }, { "from": "\\u1039\\u1008", "to": "\\u1069" }, { "from": "\\u1039\\u100b", "to": "\\u106c" }, { "from": "\\u1039\\u100c", "to": "\\u106d" }, { "from": "\\u100d\\u1039\\u100d", "to": "\\u106e" }, { "from": "\\u100d\\u1039\\u100e", "to": "\\u106f" }, { "from": "\\u1039\\u100f", "to": "\\u1070" }, { "from": "\\u1039\\u1010", "to": "\\u1071" }, { "from": "\\u1039\\u1011", "to": "\\u1073" }, { "from": "\\u1039\\u1012", "to": "\\u1075" }, { "from": "\\u1039\\u1013", "to": "\\u1076" }, { "from": "\\u1039[\\u1014\\u108f]", "to": "\\u1077" }, { "from": "\\u1039\\u1015", "to": "\\u1078" }, { "from": "\\u1039\\u1016", "to": "\\u1079" }, { "from": "\\u1039\\u1017", "to": "\\u107a" }, { "from": "\\u1039\\u1018", "to": "\\u107b" }, { "from": "\\u1039\\u1019", "to": "\\u107c" }, { "from": "\\u1039\\u101c", "to": "\\u1085" }, { "from": "\\u103f", "to": "\\u1086" }, { "from": "\\u103d\\u103e", "to": "\\u108a" }, { "from": "(\\u1064)([\\u1000-\\u1021])([\\u103b\\u103c]?)\\u102d", "to": "\\\\2\\\\3\\u108b" }, { "from": "(\\u1064)([\\u1000-\\u1021])([\\u103b\\u103c]?)\\u102e", "to": "\\\\2\\\\3\\u108c" }, { "from": "(\\u1064)([\\u1000-\\u1021])([\\u103b\\u103c]?)\\u1036", "to": "\\\\2\\\\3\\u108d" }, { "from": "(\\u1064)([\\u1000-\\u1021])([\\u103b\\u103c]?)([\\u1031]?)", "to": "\\\\2\\\\3\\\\4\\\\1" }, { "from": "\\u101b(?=([\\u102d\\u102e]?)[\\u102f\\u1030\\u103d\\u108a])", "to": "\\u1090" }, { "from": "\\u100f\\u1039\\u100d", "to": "\\u1091" }, { "from": "\\u100b\\u1039\\u100b", "to": "\\u1097" }, { "from": "([\\u1000-\\u1021\\u108f\\u1029\\u106e\\u106f\\u1086\\u1090\\u1091\\u1092\\u1097])([\\u1060-\\u1069\\u106c\\u106d\\u1070-\\u107c\\u1085\\u108a])?([\\u103b-\\u103e]*)?\\u1031", "to": "\\u1031\\\\1\\\\2\\\\3" }, { "from": "\\u103c\\u103e", "to": "\\u103c\\u1087" }, { "from": "([\\u1000-\\u1021\\u108f\\u1029])([\\u1060-\\u1069\\u106c\\u106d\\u1070-\\u107c\\u1085])?(\\u103c)", "to": "\\\\3\\\\1\\\\2" }, { "from": "\\u103a", "to": "\\u1039" }, { "from": "\\u103b", "to": "\\u103a" }, { "from": "\\u103c", "to": "\\u103b" }, { "from": "\\u103d", "to": "\\u103c" }, { "from": "\\u103e", "to": "\\u103d" }, { "from": "([^\\u103a\\u100a])\\u103d([\\u102d\\u102e]?)\\u102f", "to": "\\\\1\\u1088\\\\2" }, { "from": "([\\u101b\\u103a\\u103c\\u108a\\u1088\\u1090])([\\u1030\\u103d])?([\\u1032\\u1036\\u1039\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e]?)(\\u102f)?\\u1037", "to": "\\\\1\\\\2\\\\3\\\\4\\u1095" }, { "from": "([\\u102f\\u1014\\u1030\\u103d])([\\u1032\\u1036\\u1039\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e]?)\\u1037", "to": "\\\\1\\\\2\\u1094" }, { "from": "([\\u103b])([\\u1000-\\u1021])([\\u1087]?)([\\u1036\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e]?)\\u102f", "to": "\\\\1\\\\2\\\\3\\\\4\\u1033" }, { "from": "([\\u103b])([\\u1000-\\u1021])([\\u1087]?)([\\u1036\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e]?)\\u1030", "to": "\\\\1\\\\2\\\\3\\\\4\\u1034" }, { "from": "([\\u103a\\u103c\\u100a\\u1020\\u1025])([\\u103d]?)([\\u1036\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e]?)\\u102f", "to": "\\\\1\\\\2\\\\3\\u1033" }, { "from": "([\\u103a\\u103c\\u100a\\u101b])(\\u103d?)([\\u1036\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e]?)\\u1030", "to": "\\\\1\\\\2\\\\3\\u1034" }, { "from": "\\u100a\\u103d", "to": "\\u100a\\u1087" }, { "from": "\\u103d\\u1030", "to": "\\u1089" }, { "from": "\\u103b([\\u1000\\u1003\\u1006\\u100f\\u1010\\u1011\\u1018\\u101a\\u101c\\u101a\\u101e\\u101f])", "to": "\\u107e\\\\1" }, { "from": "\\u107e([\\u1000\\u1003\\u1006\\u100f\\u1010\\u1011\\u1018\\u101a\\u101c\\u101a\\u101e\\u101f])([\\u103c\\u108a])([\\u1032\\u1036\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e])", "to": "\\u1084\\\\1\\\\2\\\\3" }, { "from": "\\u107e([\\u1000\\u1003\\u1006\\u100f\\u1010\\u1011\\u1018\\u101a\\u101c\\u101a\\u101e\\u101f])([\\u103c\\u108a])", "to": "\\u1082\\\\1\\\\2" }, { "from": "\\u107e([\\u1000\\u1003\\u1006\\u100f\\u1010\\u1011\\u1018\\u101a\\u101c\\u101a\\u101e\\u101f])([\\u1033\\u1034]?)([\\u1032\\u1036\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e])", "to": "\\u1080\\\\1\\\\2\\\\3" }, { "from": "\\u103b([\\u1000-\\u1021])([\\u103c\\u108a])([\\u1032\\u1036\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e])", "to": "\\u1083\\\\1\\\\2\\\\3" }, { "from": "\\u103b([\\u1000-\\u1021])([\\u103c\\u108a])", "to": "\\u1081\\\\1\\\\2" }, { "from": "\\u103b([\\u1000-\\u1021])([\\u1033\\u1034]?)([\\u1032\\u1036\\u102d\\u102e\\u108b\\u108c\\u108d\\u108e])", "to": "\\u107f\\\\1\\\\2\\\\3" }, { "from": "\\u103a\\u103d", "to": "\\u103d\\u103a" }, { "from": "\\u103a([\\u103c\\u108a])", "to": "\\\\1\\u107d" }, { "from": "([\\u1033\\u1034])\\u1094", "to": "\\\\1\\u1095" }, { "from": "\\u108F\\u1071", "to" : "\\u108F\\u1072" }, { "from": "([\\u1000-\\u1021])([\\u107B\\u1066])\\u102C", "to": "\\\\1\\u102C\\\\2" }, { "from": "\\u102C([\\u107B\\u1066])\\u1037", "to": "\\u102C\\\\1\\u1094" }]'
    rule = json.loads(json_data)
    return replace_with_rule(rule,unicode)

def zg2uni(zawgyi):
    json_data = '[ { "from" : "([\\u102D\\u102E\\u103D\\u102F\\u1037\\u1095])\\\\1+", "to" : "\\\\1" }, { "from": "\\u200B", "to": "" }, { "from" : "\\u103d\\u103c", "to" : "\\u108a" }, { "from": "(\\u103d|\\u1087)", "to": "\\u103e" }, { "from": "\\u103c", "to": "\\u103d" }, { "from": "(\\u103b|\\u107e|\\u107f|\\u1080|\\u1081|\\u1082|\\u1083|\\u1084)", "to": "\\u103c" }, { "from": "(\\u103a|\\u107d)", "to": "\\u103b" }, { "from": "\\u1039", "to": "\\u103a" }, { "from": "(\\u1066|\\u1067)", "to": "\\u1039\\u1006" }, { "from": "\\u106a", "to": "\\u1009" }, { "from": "\\u106b", "to": "\\u100a" }, { "from": "\\u106c", "to": "\\u1039\\u100b" }, { "from": "\\u106d", "to": "\\u1039\\u100c" }, { "from": "\\u106e", "to": "\\u100d\\u1039\\u100d" }, { "from": "\\u106f", "to": "\\u100d\\u1039\\u100e" }, { "from": "\\u1070", "to": "\\u1039\\u100f" }, { "from": "(\\u1071|\\u1072)", "to": "\\u1039\\u1010" }, { "from": "\\u1060", "to": "\\u1039\\u1000" }, { "from": "\\u1061", "to": "\\u1039\\u1001" }, { "from": "\\u1062", "to": "\\u1039\\u1002" }, { "from": "\\u1063", "to": "\\u1039\\u1003" }, { "from": "\\u1065", "to": "\\u1039\\u1005" }, { "from": "\\u1068", "to": "\\u1039\\u1007" }, { "from": "\\u1069", "to": "\\u1039\\u1008" }, { "from": "(\\u1073|\\u1074)", "to": "\\u1039\\u1011" }, { "from": "\\u1075", "to": "\\u1039\\u1012" }, { "from": "\\u1076", "to": "\\u1039\\u1013" }, { "from": "\\u1077", "to": "\\u1039\\u1014" }, { "from": "\\u1078", "to": "\\u1039\\u1015" }, { "from": "\\u1079", "to": "\\u1039\\u1016" }, { "from": "\\u107a", "to": "\\u1039\\u1017" }, { "from": "\\u107c", "to": "\\u1039\\u1019" }, { "from": "\\u1085", "to": "\\u1039\\u101c" }, { "from": "\\u1033", "to": "\\u102f" }, { "from": "\\u1034", "to": "\\u1030" }, { "from": "\\u103f", "to": "\\u1030" }, { "from": "\\u1086", "to": "\\u103f" }, { "from": "\\u1036\\u1088", "to": "\\u1088\\u1036" }, { "from": "\\u1088", "to": "\\u103e\\u102f" }, { "from": "\\u1089", "to": "\\u103e\\u1030" }, { "from": "\\u108a", "to": "\\u103d\\u103e" }, { "from": "\\u103B\\u1064", "to": "\\u1064\\u103B" }, { "from": "(\\u103c)?(\\u1031)?([\\u1000-\\u1021])\\u1064", "to": "\\u1004\\u103a\\u1039\\\\2\\\\3\\\\1" }, { "from": "(\\u1031)?([\\u1000-\\u1021])(\\u103b)?\\u108b", "to": "\\u1004\\u103a\\u1039\\\\1\\\\2\\\\3\\u102d" }, { "from": "(\\u1031)?([\\u1000-\\u1021])(\\u103b)?\\u108c", "to": "\\u1004\\u103a\\u1039\\\\1\\\\2\\\\3\\u102e" }, { "from": "(\\u1031)?([\\u1000-\\u1021])\\u108d", "to": "\\u1004\\u103a\\u1039\\\\1\\\\2\\u1036" }, { "from": "\\u108e", "to": "\\u102d\\u1036" }, { "from": "\\u108f", "to": "\\u1014" }, { "from": "\\u1090", "to": "\\u101b" }, { "from": "\\u1091", "to": "\\u100f\\u1039\\u100d" }, { "from": "\\u1092", "to": "\\u100b\\u1039\\u100c" }, { "from": "\\u1019\\u102c(\\u107b|\\u1093)", "to": "\\u1019\\u1039\\u1018\\u102c" }, { "from": "(\\u107b|\\u1093)", "to": "\\u1039\\u1018" }, { "from": "(\\u1094|\\u1095)", "to": "\\u1037" }, { "from": "([\\u1000-\\u1021])\\u1037\\u1032", "to": "\\\\1\\u1032\\u1037" }, { "from": "\\u1096", "to": "\\u1039\\u1010\\u103d" }, { "from": "\\u1097", "to": "\\u100b\\u1039\\u100b" }, { "from": "\\u103c([\\u1000-\\u1021])([\\u1000-\\u1021])?", "to": "\\\\1\\u103c\\\\2" }, { "from": "([\\u1000-\\u1021])\\u103c\\u103a", "to": "\\u103c\\\\1\\u103a" }, { "from": "\\u1047(?=[\\u102c-\\u1030\\u1032\\u1036-\\u1038\\u103d\\u1038])", "to": "\\u101b" }, { "from": "\\u1031\\u1047", "to": "\\u1031\\u101b" }, { "from": "\\u1040(\\u102e|\\u102f|\\u102d\\u102f|\\u1030|\\u1036|\\u103d|\\u103e)", "to": "\\u101d\\\\1" }, { "from": "([^\\u1040\\u1041\\u1042\\u1043\\u1044\\u1045\\u1046\\u1047\\u1048\\u1049])\\u1040\\u102b", "to": "\\\\1\\u101d\\u102b" }, { "from": "([\\u1040\\u1041\\u1042\\u1043\\u1044\\u1045\\u1046\\u1047\\u1048\\u1049])\\u1040\\u102b(?!\\u1038)", "to": "\\\\1\\u101d\\u102b" }, { "from": "^\\u1040(?=\\u102b)", "to": "\\u101d" }, { "from": "\\u1040\\u102d(?!\\u0020?/)", "to": "\\u101d\\u102d" }, { "from": "([^\\u1040-\\u1049])\\u1040([^\\u1040-\\u1049\\u0020]|[\\u104a\\u104b])", "to": "\\\\1\\u101d\\\\2" }, { "from": "([^\\u1040-\\u1049])\\u1040(?=[\\\\f\\\\n\\\\r])", "to": "\\\\1\\u101d" }, { "from": "([^\\u1040-\\u1049])\\u1040$", "to": "\\\\1\\u101d" }, { "from": "\\u1031([\\u1000-\\u1021\\u103f])(\\u103e)?(\\u103b)?", "to": "\\\\1\\\\2\\\\3\\u1031" }, { "from": "([\\u1000-\\u1021])\\u1031([\\u103b\\u103c\\u103d\\u103e]+)", "to": "\\\\1\\\\2\\u1031" }, { "from": "\\u1032\\u103d", "to": "\\u103d\\u1032" }, { "from": "([\\u102d\\u102e])\\u103b", "to": "\\u103b\\\\1" }, { "from": "\\u103d\\u103b", "to": "\\u103b\\u103d" }, { "from": "\\u103a\\u1037", "to": "\\u1037\\u103a" }, { "from": "\\u102f(\\u102d|\\u102e|\\u1036|\\u1037)\\u102f", "to": "\\u102f\\\\1" }, { "from": "(\\u102f|\\u1030)(\\u102d|\\u102e)", "to": "\\\\2\\\\1" }, { "from": "(\\u103e)(\\u103b|\\u103c)", "to": "\\\\2\\\\1" }, { "from": "\\u1025(?=[\\u1037]?[\\u103a\\u102c])", "to": "\\u1009" }, { "from": "\\u1025\\u102e", "to": "\\u1026" }, { "from": "\\u1005\\u103b", "to": "\\u1008" }, { "from": "\\u1036(\\u102f|\\u1030)", "to": "\\\\1\\u1036" }, { "from": "\\u1031\\u1037\\u103e", "to": "\\u103e\\u1031\\u1037" }, { "from": "\\u1031\\u103e\\u102c", "to": "\\u103e\\u1031\\u102c" }, { "from": "\\u105a", "to": "\\u102b\\u103a" }, { "from": "\\u1031\\u103b\\u103e", "to": "\\u103b\\u103e\\u1031" }, { "from": "(\\u102d|\\u102e)(\\u103d|\\u103e)", "to": "\\\\2\\\\1" }, { "from": "\\u102c\\u1039([\\u1000-\\u1021])", "to": "\\u1039\\\\1\\u102c" }, { "from": "\\u1039\\u103c\\u103a\\u1039([\\u1000-\\u1021])", "to": "\\u103a\\u1039\\\\1\\u103c" }, { "from": "\\u103c\\u1039([\\u1000-\\u1021])", "to": "\\u1039\\\\1\\u103c" }, { "from": "\\u1036\\u1039([\\u1000-\\u1021])", "to": "\\u1039\\\\1\\u1036" }, { "from": "\\u104e", "to": "\\u104e\\u1004\\u103a\\u1038" }, { "from": "\\u1040(\\u102b|\\u102c|\\u1036)", "to": "\\u101d\\\\1" }, { "from": "\\u1025\\u1039", "to": "\\u1009\\u1039" }, { "from": "([\\u1000-\\u1021])\\u103c\\u1031\\u103d", "to": "\\\\1\\u103c\\u103d\\u1031" }, { "from": "([\\u1000-\\u1021])\\u103b\\u1031\\u103d(\\u103e)?", "to": "\\\\1\\u103b\\u103d\\\\2\\u1031" }, { "from": "([\\u1000-\\u1021])\\u103d\\u1031\\u103b", "to": "\\\\1\\u103b\\u103d\\u1031" }, { "from": "([\\u1000-\\u1021])\\u1031(\\u1039[\\u1000-\\u1021])", "to": "\\\\1\\\\2\\u1031" }, { "from": "\\u1038\\u103a", "to": "\\u103a\\u1038" }, { "from": "\\u102d\\u103a|\\u103a\\u102d", "to": "\\u102d" }, { "from": "\\u102d\\u102f\\u103a", "to": "\\u102d\\u102f" }, { "from": "\\u0020\\u1037", "to": "\\u1037" }, { "from": "\\u1037\\u1036", "to": "\\u1036\\u1037" }, { "from": "[\\u102d]+", "to": "\\u102d" }, { "from": "[\\u103a]+", "to": "\\u103a" }, { "from": "[\\u103d]+", "to": "\\u103d" }, { "from": "[\\u1037]+", "to": "\\u1037" }, { "from": "[\\u102e]+", "to": "\\u102e" }, { "from": "\\u102d\\u102e|\\u102e\\u102d", "to": "\\u102e" }, { "from": "\\u102f\\u102d", "to": "\\u102d\\u102f" }, { "from": "\\u1037\\u1037", "to": "\\u1037" }, { "from": "\\u1032\\u1032", "to": "\\u1032" }, { "from": "\\u1044\\u1004\\u103a\\u1038", "to": "\\u104E\\u1004\\u103a\\u1038" }, { "from": "([\\u102d\\u102e])\\u1039([\\u1000-\\u1021])", "to": "\\u1039\\\\2\\\\1" }, { "from": "(\\u103c\\u1031)\\u1039([\\u1000-\\u1021])", "to": "\\u1039\\\\2\\\\1" }, { "from": "\\u1036\\u103d", "to": "\\u103d\\u1036" }]'
    rule = json.loads(json_data)
    return replace_with_rule(rule,zawgyi)

def replace_with_rule(rule,output):
    for data in rule:
        if sys.version_info >= (3,5):
            # no more return None for unmatched after 3.5
            output = re.sub(data["from"],data["to"].replace("\\\\","\\"),output)
        else:
            output = re_sub(data["from"],data["to"].replace("\\\\","\\"),output)
    return output

def re_sub(pattern, replacement, string):
    def _r(m):
    # Now this class is ugly.
    # Python has a "feature" where unmatched groups return None
    # then re.sub chokes on this.
    # see http://bugs.python.org/issue1519638

    # this works around and hooks into the internal of the re module...

    # the match object is replaced with a wrapper that
    # returns "" instead of None for unmatched groups
        class _m():
            def __init__(self, m):
                self.m=m
                self.string=m.string
            def group(self, n):
                return m.group(n) or ""

        return re._expand(pattern, _m(m), replacement)

    return re.sub(pattern, _r, string)

# ==============================================================================================

win = Tk()
win.title('Mdy_L33ts ==> File/Folder Name Converter (zawgyi-unicode)')
win.geometry('+350+100')
win.geometry('800x500')
win.config(bg='black')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
image_path = resource_path('android_logo.ico')
win.iconbitmap(image_path)



style = ttk.Style()
style.configure('.', font=('Helvetica', 8), foreground='black')
style.configure("Treeview", foreground='black', background='light pink')
style.configure("Treeview.Heading", foreground='black', background='red')

frame = Frame(win, background='black')
frame.pack(expand=True)

title = ttk.Label(frame, text='File/Folder Name Converter (zawgyi-unicode)', background='black', foreground='white', font=('bold','20'))
title.pack(fill='both', expand=True, pady=10)


header = ['Original Name']
header1 = ['Converted Name']

def cbrowse_file(*agrs):
    global checker
    global tempdir
    global blank
    tempdir = filedialog.askdirectory(parent=win, title="directory")
    if tempdir != '':
        tree.delete(*tree.get_children())
        tree1.heading(col, text=col.title())
        all_list = os.listdir(tempdir)
        for file in all_list:
            if os.path.isfile(os.path.join(tempdir, file)):
                tree.insert('', 'end', value=[file])     
        
        checker = 'cfile'
        z_button.set('Convert to Zawgyi')
        zg.config(state='normal')
        u_button.set('Convert to Unicode')
        uni.config(state='normal')
        blank = tempdir
    else:
        tempdir = blank
    
def cbrowse_folder(*agrs): 
    global checker
    global tempf
    global blank
    tempf = filedialog.askdirectory(parent=win, title="directory")
    if tempf != '':
        tree.delete(*tree.get_children())
        tree1.heading(col, text=col.title())
        all_list = os.listdir(tempf)
        for folder in all_list:
            if os.path.isdir(os.path.join(tempf, folder)):
                tree.insert('', 'end', value=[folder])
                
        checker = 'cfolder'
        z_button.set('Convert to Zawgyi')
        zg.config(state='normal')
        u_button.set('Convert to Unicode')
        uni.config(state='normal')
        blank = tempf
    else:
        tempf = blank

def browse_file(*agrs): 
    global checker
    global tempdir
    global blank
    tempdir = filedialog.askdirectory(parent=win, title="directory")
    if tempdir != '':
        tree.delete(*tree.get_children())
        tree1.heading(col, text=col.title())
        for root, directories, filenames in os.walk(tempdir):
            for filename in filenames:
                tree.insert('', 'end', value=[filename])
        checker = 'fileall'
        z_button.set('Convert to Zawgyi')
        zg.config(state='normal')
        u_button.set('Convert to Unicode')
        uni.config(state='normal')
        blank = tempdir
    else:
        tempdir = blank
        
def browse_folder(*agrs): 
    global checker
    global tempf
    global blank
    tempf = filedialog.askdirectory(parent=win, title="directory")
    if tempf != '':
        tree.delete(*tree.get_children())
        tree1.heading(col, text=col.title())
        for root, directories, filenames in os.walk(tempf):
            for directory in directories:
                tree.insert('', 'end', value=[directory])
                
        checker = 'folderall'
        z_button.set('Convert to Zawgyi')
        zg.config(state='normal')
        u_button.set('Convert to Unicode')
        uni.config(state='normal')
        blank = tempf
    else:
        tempf = blank

menuBar = Menu(win)
win.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff = 0)
fileHelp = Menu(menuBar, tearoff = 0)

menuBar.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label='Convert filenames (only current directory)', command=cbrowse_file)
fileMenu.add_command(label='Convert foldernames (only current directory)', command=cbrowse_folder)

fileMenu.add_command(label='Convert filenames (included all subdirectories)', command=browse_file)
fileMenu.add_command(label='Convert foldernames (included all subdirectories)', command=browse_folder)


ttk.Label(win, text='     ', background='black').pack(side='left')

#=================================================================#

frame1 = Frame(win, background='black')
frame1.pack(fill='both', expand=True)

d_label = LabelFrame(frame1, text= 'File or Folder list', padx=5, pady=5, background='black', foreground='white')
d_label.pack(padx=10, pady=5, fill='both', side='left', expand=True)

tree = ttk.Treeview(columns=header, show="headings")

vsb = ttk.Scrollbar(orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(orient="horizontal", command=tree.xview)
        
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, columnspan=2, row=0, sticky='nsew', in_=d_label)

vsb.grid(column=3, row=0, sticky='ns', in_=d_label)
hsb.grid(column=0, columnspan=2, row=1, sticky='ew', in_=d_label)

d_label.grid_columnconfigure(0, weight=1)
d_label.grid_rowconfigure(0, weight=1)

for col in header:
    tree.heading(col, text=col.title())
    # adjust the column's width to the header string
    tree.column(col, width=tkFont.Font().measure(col.title()))

#=================================================================#

e_label = LabelFrame(frame1, text= 'Convert List', padx=5, pady=5, background='black', foreground='white')
e_label.pack(padx=10, pady=5, fill='both', side='left', expand=True)

tree1 = ttk.Treeview(columns=header1, show="headings")

vsb1 = ttk.Scrollbar(orient="vertical", command=tree1.yview)
hsb1 = ttk.Scrollbar(orient="horizontal", command=tree1.xview)
        
tree1.configure(yscrollcommand=vsb1.set, xscrollcommand=hsb1.set)
tree1.grid(column=0, row=0, sticky='nsew', in_=e_label)
        
vsb1.grid(column=1, row=0, sticky='ns', in_=e_label)
hsb1.grid(column=0, row=1, sticky='ew', in_=e_label)

e_label.grid_columnconfigure(0, weight=1)
e_label.grid_rowconfigure(0, weight=1)

for col in header1:
    tree1.heading(col, text=col.title())
    # adjust the column's width to the header string
    tree1.column(col, width=tkFont.Font().measure(col.title()))


#=================================================================#

z_button = StringVar()
z_button.set('Convert to Zawgyi')
u_button = StringVar()
u_button.set('Convert to Unicode')

def u2z():
    item = tree.get_children()
    if len(item)==0:
        tree.insert('', 'end', value=["dosen't have any file or folder"])
    else:
        tree1.delete(*tree1.get_children())
        zg.config(state='disabled')
        if checker == 'fileall':
            for root, directories, filenames in os.walk(tempdir):
                for filename in filenames:
                    fn = filename.strip().split(" ")
                    #pattern = re.compile(zawgyiRegex)
                    for i in fn:
                        match = pattern.search(i)
                        if not match:
                            unicode = uni2zg(filename)
                            src = os.path.join(root,filename)
                            dst = src.replace(filename, unicode)
                            try:
                                os.rename(src,dst)
                                tree1.insert('', 'end', value=[unicode])
                            except:
                                pass
        elif checker == 'folderall':
            for root, directories, filenames in os.walk(tempf):
                for directory in directories:
                    fn = directory.strip().split(" ")
                    #pattern = re.compile(zawgyiRegex)
                    for i in fn:
                        match = pattern.search(i)
                        if not match:
                            unicode = uni2zg(directory)
                            src = os.path.join(root,directory)
                            dst = src.replace(directory, unicode)
                            try:
                                os.rename(src,dst)
                                tree1.insert('', 'end', value=[unicode])
                            except:
                                pass
        elif checker == 'cfile':
            all_list = os.listdir(tempdir)
            for filename in all_list:
                if os.path.isfile(os.path.join(tempdir, filename)):
                    fn = filename.strip().split(" ")
                    for i in fn:
                        match = pattern.search(i)
                        if not match:
                            unicode = uni2zg(filename)
                            src = os.path.join(tempdir,filename)
                            dst = src.replace(filename, unicode)
                            try:
                                os.rename(src,dst)
                                tree1.insert('', 'end', value=[unicode])
                            except:
                                pass
        elif checker == 'cfolder':
            all_list = os.listdir(tempf)
            for foldername in all_list:
                if os.path.isdir(os.path.join(tempf, foldername)):
                    fn = foldername.strip().split(" ")
                    #pattern = re.compile(zawgyiRegex)
                    for i in fn:
                        match = pattern.search(i)
                        if not match:
                            unicode = uni2zg(foldername)
                            src = os.path.join(tempf,foldername)
                            dst = src.replace(foldername, unicode)
                            try:
                                os.rename(src,dst)
                                tree1.insert('', 'end', value=[unicode])
                            except:
                                pass
        else:
            print('hello')
        
                
        z_button.set('Finish')
        zg.config(state='normal')
        zg.config(state='disabled')
        u_button.set('Convert to Unicode')
        uni.config(state='normal')
        

def z2u():
    item = tree.get_children()
    if len(item)==0:
        tree.insert('', 'end', value=["dosen't have any file or folder"])
    else:
        tree1.delete(*tree1.get_children())
        uni.config(state='disabled')
        if checker == 'fileall':
            for root, directories, filenames in os.walk(tempdir):
                for filename in filenames:
                    fn = filename.strip().split(" ")
                    #pattern = re.compile(zawgyiRegex)
                    for i in fn:
                        match = pattern.search(i)
                        if match:
                            zawgyi = zg2uni(filename)
                            src = os.path.join(root,filename)
                            dst = src.replace(filename, zawgyi)
                            try:
                                os.rename(src,dst)
                                tree1.insert('', 'end', value=[zawgyi])
                            except:
                                pass
        elif checker == 'folderall':
            for root, directories, filenames in os.walk(tempf):
                for directory in directories:
                    fn = directory.strip().split(" ")
                    for i in fn:
                        match = pattern.search(i)
                        if match:
                            zawgyi = zg2uni(directory)
                            src = os.path.join(root,directory)
                            dst = src.replace(directory, zawgyi)
                            try:
                                os.rename(src,dst)
                                tree1.insert('', 'end', value=[zawgyi])
                            except:
                                pass
        elif checker == 'cfile':
            all_list = os.listdir(tempdir)
            for filename in all_list:
                if os.path.isfile(os.path.join(tempdir, filename)):
                    fn = filename.strip().split(" ")
                    for i in fn:
                        match = pattern.search(i)
                        if match:
                            zawgyi = zg2uni(filename)
                            src = os.path.join(tempdir,filename)
                            dst = src.replace(filename, zawgyi)
                            try:
                                os.rename(src,dst)
                                tree1.insert('', 'end', value=[zawgyi])
                            except:
                                pass
        elif checker == 'cfolder':
            all_list = os.listdir(tempf)
            for foldername in all_list:
                if os.path.isdir(os.path.join(tempf, foldername)):
                    fn = foldername.strip().split(" ")
                    for i in fn:
                        match = pattern.search(i)
                        if match:
                            zawgyi = zg2uni(foldername)
                            src = os.path.join(tempf,foldername)
                            dst = src.replace(foldername, zawgyi)
                            try:
                                os.rename(src,dst)
                                tree1.insert('', 'end', value=[zawgyi])
                            except:
                                pass
        
        u_button.set('Finish')
        uni.config(state='normal')
        uni.config(state='disabled')
        z_button.set('Convert to Zawgyi')
        zg.config(state='normal')

frame2 = Frame(win, background='black')
frame2.pack(expand=True, pady=2)

zg = ttk.Button(frame2, textvariable=z_button, width=17, command=u2z)
zg.pack(expand=True, side='left', padx=10)

uni = ttk.Button(frame2, textvariable=u_button, width=17, command=z2u)
uni.pack(expand=True, padx=10)
      
frame3 = Frame(win, background='black')
frame3.pack()

dev = ttk.Label(frame3, text='Developed by Mdy_L33ts and credit to creator of rabbit-converter (saturngod)', background='black', foreground='white')
dev.pack(side='left', expand=True)

win.mainloop() 



