def _create_post_form(request, get_form, form_valid, form_invalid):
    form = get_form()
    _mutable = form.data._mutable
    form.data._mutable = True
    form.data['author'] = str(request.user.id)
    form.data._mutable = _mutable

    if form.is_valid():
        return form_valid(form)
    else:
        return form_invalid(form)