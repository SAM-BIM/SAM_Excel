"""Repository-specific classification decisions for SAM_Excel (the only non-shared tool file).

OVERRIDES     : component display name -> (object glyph, op, extra)   extra: None | "plural" | "library" | note
PARAM_OBJECTS : param type key (Goo<X>Param class or typeof(X) name) -> glyph | (glyph, container, plural)
OBJECTS/VERBS : extra noun/verb rules tried before the shared ones (same shapes as SAM's OBJECTS/VERBS)
"""
OVERRIDES = {
    "SAMExcel.ClearContents": ("table", "remove", None), "SAMExcel.ClearOption": ("table", "value", "clear option"),
    "SAMExcel.Read": ("value", "import", "plural"), "SAMExcel.WriteByValues": ("value", "export", "plural"),
}
PARAM_OBJECTS = {}
OBJECTS = []
VERBS = []
