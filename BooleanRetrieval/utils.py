def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by converting it to lowercase and stripping extra spaces.
    :param text: The input document as a string.
    :return: The preprocessed text as a string.
    """
    return text.lower().strip()
