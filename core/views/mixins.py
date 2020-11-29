from collections import defaultdict
from django.conf import settings
import os

BASE_PATH = settings.BASE_DIR


class MixinBase:
    template_name="demo.html"
    demo_template = None
    subtitle = None

    def get_files(self):
        files = defaultdict(list)
        path_ = lambda x: open(os.path.join(BASE_PATH, x)).read()
        for filename, filetype, pygment_type  in self.files:
            filesrc = path_(filename)
            files[filetype].append({
                'src': filesrc,
                'pygment_type': pygment_type,
                'filename': filename,
                'loc': len(filesrc.split('\n'))
            })
        return dict(files)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = self.get_files()
        context['demo_template'] = self.demo_template
        context['subtitle'] = self.subtitle
        return context

