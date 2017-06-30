from binaryninja import *

def type_importer(bv):
    form_fields = [ 
        interaction.MultilineTextField("Paste Code Here")
    ]
    result = interaction.get_form_input(form_fields, "Enter Code") 
    try: 
        parsedtypes = bv.arch.parse_types_from_source(form_fields[0].result)
        for currenttype in parsedtypes.types:
            bv.define_type(Type.generate_auto_type_id("source", currenttype), currenttype, parsedtypes.types[currenttype])
    except:
        log_error(traceback.format_exc())

PluginCommand.register("Type Importer", "parse pasted code and import as types", type_importer)
