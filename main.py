class SmartCut:
    def __init__(self):
        pass

    def cut(self, incoming_text):
        new_text = ''
        # Check length of incoming string
        if len(incoming_text) > 25:
            # Cut incoming string until it become 25 characters length
            for symbol in incoming_text:
                new_text += symbol
                if len(new_text) == 25:
                    break
            # check the new string for special characters and spaces at the end of it
            while True:
                if new_text[-1] == '!' or new_text[-1] == '?':
                    new_text = new_text + '...'
                    break
                elif new_text[-1] == ' ' or new_text[-1] == ',' or new_text[-1] == '.' or new_text[-1] == ':':
                    new_text = new_text[:-1] + '...'
                    break
                else:
                    new_text = new_text[:-1]
            return new_text
        else:
            return incoming_text
