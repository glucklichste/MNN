# automatically generated by the FlatBuffers compiler, do not modify

# namespace: NamespaceA

import flatbuffers

class SecondTableInA(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSecondTableInA(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SecondTableInA()
        x.Init(buf, n + offset)
        return x

    # SecondTableInA
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SecondTableInA
    def ReferToC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .TableInC import TableInC
            obj = TableInC()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def SecondTableInAStart(builder): builder.StartObject(1)
def SecondTableInAAddReferToC(builder, referToC): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(referToC), 0)
def SecondTableInAEnd(builder): return builder.EndObject()
