class NewList(object):

    def __init__(self, items):
        self.items = items
        self.counter = 0

    def index_error(self, idx):
        if idx == 0:
            raise IndexError('List index out of range.')

    def index_conversion(self, idx):
        start, stop, step = idx.start, idx.stop, idx.step
        self.index_error(start)
        self.index_error(stop)
        if (start != None):
            start -= 1
        if (stop != None):
            stop -= 1
        return slice(start,stop,step)

    def __getitem__(self, idx):
       if isinstance(idx, slice):
            new_slice = self.index_conversion(idx)
            return self.items[new_slice]
       else:
            self.index_error(idx)
            if idx > 0:
                return self.items[idx-1]
            else:
                return self.items[idx]
            
    def __setitem__(self, idx, value):
        self.index_error(idx)
        self.items[idx-1] = value

    def __delitem__(self, idx):
        self.index_error(idx)
        del self.items[idx-1]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.items)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self.items) > self.counter:
            value, self.counter = self.items[self.counter], self.counter+1
            return value
        else:
            raise StopIteration()
