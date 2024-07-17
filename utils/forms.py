def style_input_form(field, css_class):
    field.widget.attrs.update({"class": css_class})


def add_placeholder(field, placeholder):
    field.widget.attrs["placeholder"] = placeholder


def update_label_suffix(field, suffix):
    field.label_suffix = suffix
