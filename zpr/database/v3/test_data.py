import sys, os
sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from zprapp.models import Organism, Chromosome, AnnotationType, Annotation

class TestDataInserter():
    def insert(self):
        print "insert test data"
        self.db_objects = []

        organisms = self._organisms()
        self._save_elements(organisms)
        self.db_objects += organisms

        chromosomes = self._chromosomes(organisms[0])
        self._save_elements(chromosomes)
        self.db_objects += chromosomes

        annotation_types = self._annotation_types()
        self._save_elements(annotation_types)
        self.db_objects += annotation_types

        annotations = self._annotations(chromosomes)
        self._save_elements(annotations)
        self.db_objects += annotations

    def _save_elements(self, elements):
        ''':param elements -- list'''
        for e in elements:
            e.save()

    def delete(self):
        print "delete test data"
        for i in reversed(self.db_objects):
            i.delete()

    def _organisms(self):
        return [Organism(name="demo_organism")]

    def _chromosomes(self, org):
        return [Chromosome(organism=org, number=1, ordered=True, length=100),
                Chromosome(organism=org, number=2 , ordered=True, length=100)]

    def _annotation_types(self):
        return [
            AnnotationType(name='demo_marker1', short_name='demo1'),
            AnnotationType(name='demo_marker2', short_name='demo2'),
            AnnotationType(name='demo_marker3', short_name='demo3'),
            AnnotationType(name='demo_marker4', short_name='demo4'),
            AnnotationType(name='alfabet', short_name='abcd'),
            AnnotationType(name='demo_nadmiarowy', short_name='nadmiar')
        ]

    def _annotations(self, chromosomes):
        chromosome1 = chromosomes[0]
        chromosome2 = chromosomes[1]
        demo1 = AnnotationType.objects.get(short_name='demo1')
        annotations_demo1 = [
            Annotation(start_chr=0, length=10, name='ann1', sequence='1_DEMO1_A1',
                       type=demo1, chromosome=chromosome1),
            Annotation(start_chr=20, length=10, name='ann2', sequence='1_DEMO1_A2',
                       type=demo1, chromosome=chromosome1),
            Annotation(start_chr=35, length=60, name='ann1', sequence='2_DE'+"E"*50+'MO1_A1',
                       type=demo1, chromosome=chromosome2)
        ]
        demo2 = AnnotationType.objects.get(short_name='demo2')
        annotations_demo2 = [
            Annotation(start_chr=40, length=10, name='ann1', sequence='1_DEMO2_A1',
                       type=demo2, chromosome=chromosome1),
            Annotation(start_chr=60, length=10, name='ann2', sequence='1_DEMO2_A2',
                       type=demo2, chromosome=chromosome1)
        ]
        demo3 = AnnotationType.objects.get(short_name='demo3')
        annotations_demo3 = [
            Annotation(start_chr=5, length=17, name='ann1', sequence='1_DE'+"E"*7+'MO3_A1',
                       type=demo3, chromosome=chromosome1),
            Annotation(start_chr=24, length=40, name='ann2', sequence='1_DE'+"E"*30+'MO3_A2',
                       type=demo3, chromosome=chromosome1)
        ]
        demo4 = AnnotationType.objects.get(short_name='demo4')
        annotations_demo4 = [
            Annotation(start_chr=80, length=10, name='ann1', sequence='1_DEMO4_A1',
                       type=demo4, chromosome=chromosome1),
            Annotation(start_chr=85, length=10, name='ann2', sequence='1_DEMO4_A2',
                       type=demo4, chromosome=chromosome1)
        ]
        abcd = AnnotationType.objects.get(short_name='abcd')
        annotations_abcd = [
            Annotation(start_chr=20, name='a_z', length=22, sequence="abcdefghijklmoprstwxyz",
                       type=abcd, chromosome=chromosome1)
        ]
        return annotations_demo1 + annotations_demo2 + annotations_demo3 + annotations_demo4 \
               + annotations_abcd

if __name__ == '__main__':
    t = TestDataInserter()
    t.insert()
