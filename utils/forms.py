def add_placeholder(field, placeholder):
    field.widget.attrs["placeholder"] = placeholder


def style_input_form(field, css_class):
    field.widget.attrs.update({"class": css_class})
