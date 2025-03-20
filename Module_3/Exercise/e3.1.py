# %%
class Node(object):
    """ A node in a linked list"""
    def _init_(self, data, next=None):
        self.data = data
        self.next = next
