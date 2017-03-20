# coding: utf-8
from __future__ import unicode_literals

from enum import Enum

from yargy.normalization import get_normalized_text
from yargy.interpretation import (
    InterpretationObject,
    damerau_levenshtein_distance,
)


class OrganisationObject(InterpretationObject):

    class Attributes(Enum):

        Name = 0 # кировский
        Descriptor = 1 # завод

    @property
    def normalized_name(self):
        if self.name:
            return get_normalized_text(
                self.name
            ).lower()
        else:
            return None

    @property
    def normalized_descriptor(self):
        if self.descriptor:
            return get_normalized_text(
                self.descriptor,
            ).lower()
        else:
            return None
