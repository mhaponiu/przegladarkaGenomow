#TODO class Meanings
from dbbase import DBBase
from zprapp.models import Meaning


class Meanings(DBBase):
    def glos(self):
        print 'Znaczenia! '

    def create(self):
        means = ["poczatek genu", "koniec genu", "znaczenie 3", "znaczenie 4", "znaczenie 5", "znaczenie 6", "znaczenie 7", "znaczenie 8"]
        for m in means:
            mean = Meaning(mean = m);
            mean.save();
        print "utworzono znaczenia markerow (meaning)"

    def delete(self):
        meanings = Meaning.objects.all();
        for m in meanings:
            m.delete()
        print "usunieto znaczenia markerow (meaning)"