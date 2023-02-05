def load_document(document):
    document_list = [content.split('\t') for content in document]
    return {int(id_): article for id_, article in document_list}