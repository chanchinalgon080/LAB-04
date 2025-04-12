class TextEditor:
    def __init__(self):
        self.text_stack = []
        self.undo_stack = []

    def type(self, char):
        self.text_stack.append(char)
        self.undo_stack.append(('type', char))

    def delete(self):
        if self.text_stack:
            deleted_char = self.text_stack.pop()
            self.undo_stack.append(('delete', deleted_char))

    def undo(self):
        if not self.undo_stack:
            return
        action, char = self.undo_stack.pop()
        if action == 'type':
            self.text_stack.pop()
        elif action == 'delete':
            self.text_stack.append(char)

    def get_text(self):
        return ''.join(self.text_stack)

editor = TextEditor()

editor.type('a')
editor.type('b')
editor.type('c')
editor.undo()
print("Test 1:", editor.get_text())  

editor = TextEditor()

editor.type('x')
editor.type('y')
editor.delete()
editor.undo()
print("Test 2:", editor.get_text())  

editor = TextEditor()

editor.type('o')
editor.type('k')
editor.delete()
editor.delete()
editor.undo()
editor.undo()
print("Test 3:", editor.get_text()) 
