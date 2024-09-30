import unicodedata 
from brutils.data.enums import UF

def text_formatter(text: str) -> str:
    """
    Removes special characters and accentuation marks from a given text and turns it
    to lowercase
    """
    # Normalize and lowercase
    text_lower_normalized = unicodedata.normalize("NFD", text).lower()
    # Removes accentuation marks
    lower_norm_no_acc_marks = text_lower_normalized.encode("ascii", "ignore").decode("utf-8")

    return lower_norm_no_acc_marks


def convert_text_to_uf(state_name): # type: (str) -> str | None
    """
    Converts a given Brazilian state full name to its corresponding UF code.

    This function takes the full name of a Brazilian state and returns the corresponding 
    2-letter UF code. It handles all Brazilian states and the Federal District. 

    Args:
        state_name (str): The full name of the state to be converted.

    Returns:
        str or None: The UF code corresponding to the full state name, 
            or None if the full state name is invalid.

    Example:
        >>> convert_text_to_uf('São Paulo')
        "SP"
        >>> convert_text_to_uf('Rio de Janeiro')
        "RJ"
        >>> convert_text_to_uf('Minas Gerais')
        "MG"
        >>> convert_text_to_uf('Distrito Federal')
        "DF"
        >>> convert_text_to_uf('Estado Inexistente')
        None
    """
    # Remove special characters and accentuation marks from function parameter (state_name) and lowercase it
    formatted_state_name = text_formatter(state_name)
    print(formatted_state_name)

    # Create a list with all states abbreviations
    all_abbrv = [abbreviation.name for abbreviation in UF]
    # Create a list with all formatted state names
    all_state_names = [text_formatter(statename.value) for statename in UF]
    # Create a dict where abbreviations are keys and state names are values
    new_dict = dict(zip(all_abbrv, all_state_names))

    # Iterates dict items in order to seach for formatted state names.
    for k, v in new_dict.items():
        if v == formatted_state_name:
            return k
    return None

