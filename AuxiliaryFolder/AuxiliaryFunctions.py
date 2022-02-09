class AuxiliaryFunctions:
    def is_exists(self, check_item, items):

        for i in range(len(items) - 1):
            if items[i].id == check_item.id:
                return True

            return False

    def get_location(self, id, items):
        for counter in range(len(items)):
            if items[counter].id == id:
                return counter
        else:
            return -1

    def get_id(self, item):
        return item.id
