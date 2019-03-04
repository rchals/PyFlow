from PyFlow.Packages.BasePackage import PACKAGE_NAME
from PyFlow.Core import PinBase
from PyFlow.Core.AGraphCommon import *
from PyFlow.UI.Settings import Colors
from PyFlow import getAllPinClasses


class AnyPin(PinBase):
    """doc string for SgPin"""
    def __init__(self, name, parent, dataType, direction, **kwargs):
        super(AnyPin, self).__init__(name, parent, dataType, direction, **kwargs)

        self.setDefaultValue(None)
        self.supportedDataTypesList = tuple([pin.__name__ for pin in getAllPinClasses() if pin.IsValuePin()])
        self.origDataType = "AnyPin"
        self._free = True
        self.isAny = True
        self.origSetData = self.setData
        self.super = None

    def supportedDataTypes(self):
        return self.supportedDataTypesList

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def defcolor():
        return (255, 255, 255, 255)

    @staticmethod
    def color():
        return (255, 255, 255, 255)

    @staticmethod
    def pinDataTypeHint():
        return 'AnyPin', ""

    @staticmethod
    def packageName():
        return PACKAGE_NAME

    @staticmethod
    def processData(data):
        return data

    def setData(self, data):
        if self.dataType != "AnyPin":
            if self.super is not None:
                data = self.super.processData(data)
        self._data = data
        PinBase.setData(self, self._data)

    def serialize(self):
        from PyFlow import CreateRawPin
        dt = super(PinBase, self).serialize()
        if self.dataType != DataTypes.Any:
            a = CreateRawPin("", None, self.dataType, 0)
            a.setData(self._data)
            data = a.serialize()
            dt['value'] = data["value"]
            del a
        return dt

    def pinConnected(self, other):
        self.updateOnConnection(other)
        PinBase.pinConnected(self, other)
        # self.OnPinConnected.emit(other)

    def pinDisconnected(self, other):
        PinBase.pinDisconnected(self, other)
        # self.OnPinConnected.emit(other)
        self.updateOnDisconnection()

    def updateOnConnection(self, other):
        if self.constraint is None:
            self.setType(other)
            self._free = False
        else:
            if other.dataType != DataTypes.Any:
                self._free = False
                self.setType(other)
                for port in self.parent()._Constraints[self.constraint]:
                    if port != self:
                        port.setType(other)
                        port._free = False
                        for e in port.edge_list:
                            for p in [e.source(), e.destination()]:
                                if p != port:
                                    if p.dataType == DataTypes.Any and p.dataType != self.dataType:
                                        p.updateOnConnection(port)

    def updateOnDisconnection(self):
        if self.constraint is None:
            self.setDefault()
            self._free = True
        elif not self._free:
            self._free = self.checkFree([])
            if self._free:
                self.setDefault()
                for port in self.parent()._Constraints[self.constraint]:
                    if port != self:
                        port.setDefault()
                        port._free = True
                        for e in port.edge_list:
                            for p in [e.source(), e.destination()]:
                                if p != port:
                                    p.updateOnDisconnection()

    def checkFree(self, checked=[], selfChek=True):
        if self.constraint is None or self.dataType == DataTypes.Any:
            return True
        else:
            con = []
            if selfChek:
                free = not self.hasConnections()
                if not free:
                    for edge in self.edge_list:
                        for c in [edge.source(), edge.destination()]:
                            if c != self:
                                if c not in checked:
                                    con.append(c)
            else:
                free = True
                checked.append(self)
            free = True
            for port in self.parent()._Constraints[self.constraint] + con:
                if port not in checked:
                    checked.append(port)
                    if not isinstance(port, AnyPin):
                        free = False
                    elif free:
                        free = port.checkFree(checked)

            return free

    def call(self):
        super(AnyPin, self).call()
        # pass execution flow forward
        for p in [pin for pin in self.affects if pin.dataType == DataTypes.Exec]:
            p.call()
        # highlight wire
        for e in self.edge_list:
            e.highlight()

    def setDefault(self):
        self.super = None
        self.dataType = "AnyPin"
        self.color = self.defcolor
        self.setDefaultValue(None)
        for e in self.edge_list:
            e.setColor(self.color())
        # self.OnPinChanged.emit(self)
        # self.update()

    def setType(self, other):
        self.super = other.__class__
        self.dataType = other.dataType
        self.color = other.color
        if str(type(self._data)) == "<type 'unicode'>":
            self._data = str(self._data)
        if type(self._data) != type(other._data):
            self.setData(other.defaultValue())
        self.setDefaultValue(other.defaultValue())
        for e in self.edge_list:
            e.setColor(self.color())
        # self.OnPinChanged.emit(self)
        # self.update()