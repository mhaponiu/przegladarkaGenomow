from zprapp.models import Annotation, AnnotationType

class Layerer():
    '''
    ma za zadanie poukladac na siebie cale linie adnotacji uwzlgedniajac podany priorytet
    wypelnia luki miedzy adnotacjami wyzszego priorytetu, adnotacjami nizszego priorytetu
    '''
    #TODO na chwile obecna bierze tylko pierwszy typ i jedynie jego zwraca -> do implementacji kiedys

    def __init__(self, type_priority_list):
        self.type_priority = type_priority_list

    def compose(self):
        type_id = self.type_priority[0]
        annotations = Annotation.objects.filter(type=AnnotationType.objects.get(id=type_id)).order_by('start_chr')
        return annotations