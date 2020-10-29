# This is one of the variations of the three design patterns in document processing
from __future__ import annotations
from collections.abc import Iterable, Iterator
from abc import ABC, abstractmethod
from random import randrange, sample
from typing import Any, List
from datetime import datetime
from string import ascii_letters, digits
import hashlib

class Message:
    def __init__(self, name, text, recipient):
        self.name = name
        self.text = text
        self.recipient = recipient       

    def __repr__(self):
        return f"Send by {self.name} to {self.recipient}\nText: {self.text}"

    def update(self, status: MessageObserver):
        if not status.get_state(): return f"Send by {self.name} to {self.recipient}\nText: {self.text}"
        else: return f"Error"

    def text_list(self):
        return list(self.text.split(" "))

    def save(self):
        return Memento(self)

    def restore(self, memento) -> None:
        message = memento.get_message()
        self.name = message.name
        self.text = message.text
        self.recipient = message.recipient

# Iterator implementation
class TextCryptor(Iterator):
    _position: int = None

    def __init__(self, collection: Words) -> None:
        self._collection = collection
        self._position = 0

    def __str__(self):
        return list(self.value)

    def __next__(self):
        try:
            value = self._collection[self._position]
            value = hashlib.sha1(value.encode('utf-8')).hexdigest()
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value

class Words(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> TextCryptor:
        return TextCryptor(self._collection)

    def add_item(self, item: Any):
        self._collection.append(item)

# Observer implementation
class MessageObserver:
    _state: bool = None
    _observers = []

    def attach(self, observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            print("Message sent")
            observer.update(self)

    def send(self, message_state: bool) -> None:
        self._state = message_state

        print("Message on the way") if message_state else print("WTF, error")
        self.notify()

    def get_state(self):
        return self._state

# Memento implementation
class Memento:
    def __init__(self, message):
        self.message = Message(name = message.name, text = message.text, recipient = message.recipient)

    def get_message(self):
        return self.message

class Caretaker:
    def __init__(self, message) -> None:
        self.mementos = []
        self.message = message

    def backup(self) -> None:
        self.mementos.append(self.message.save())

    def undo(self) -> None:
        if not len(self.mementos):
            return

        memento = self.mementos.pop()
        try:
            self.message.restore(memento)
        except Exception:
            self.undo()

if __name__ == "__main__":
    notify = MessageObserver()

    letter = Message("Egor", "How do you?", "Ilya")
    print(letter)

    notify.attach(letter)

    caretaker = Caretaker(letter)
    caretaker.backup()

    notify.send(True)

    collection = Words()
    collection.add_item(letter.name)
    collection.add_item(letter.text)   
    collection.add_item(letter.recipient) 

    name = "\n".join(collection)[0:40]
    text = "\n".join(collection)[41:81]
    recipient = "\n".join(collection)[82:122]

    letter.name = name
    letter.text = text
    letter.recipient = recipient
    print(letter)

    caretaker.undo()
    print(letter)

