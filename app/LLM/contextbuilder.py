

def build_context(results):
    context_parts = []

    for index, result in enumerate(results):
        source = result['file_name']
        text = result['text']

        context_parts.append(
            f'Source {index+1}: {source} \n '
            f'{text}'
        )

    return "\n\n".join(context_parts)