def link_previous(qs):
    ids = qs.values_list("id", flat=True)
    out = {ids[0]: "-"}

    for i in range(len(ids)):
        if i == len(ids) - 1:
            break
        out[ids[i + 1]] = f"Res-{ids[i]}"

    return out
