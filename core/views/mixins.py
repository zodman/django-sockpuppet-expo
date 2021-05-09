from collections import defaultdict
from django.conf import settings
import os

BASE_PATH = settings.BASE_DIR


class MixinBase:
    template_name = "demo.html"
    demo_template = None
    subtitle = None

    def get_files(self):
        files = defaultdict(list)
        path_ = lambda x: open(os.path.join(BASE_PATH, x)).read()
        for filename, filetype, pygment_type in self.files:
            filesrc = path_(filename)
            files[filetype].append(
                {
                    "src": filesrc,
                    "pygment_type": pygment_type,
                    "filename": filename,
                    "loc": len(filesrc.split("\n")),
                }
            )
        return dict(files)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["files"] = self.get_files()
        context["demo_template"] = self.demo_template
        context["subtitle"] = self.subtitle
        return context


class BookSearchMixin(MixinBase):
    files = (
        ("core/reflexes/book_search_reflex.py", "python", "python3"),
        ("core/views/book_search.py", "python", "python3"),
        ("core/javascript/controllers/book_search_controller.js", "javascript",
         "javascript",),
        ("core/templates/_book_search_demo.html", "html", "htmldjango"),
    )


class ExampleMixin(MixinBase):
    files = (
        ('core/views/example.py', 'python', 'python3'),
        ('core/reflexes/example_reflex.py', 'python', 'python3'),
        ('core/javascript/controllers/example_controller.js', 'javascript', 'javascript'),
        ('core/templates/_example_demo.html', 'html', 'htmldjango'),
    )


class ChatMixin(MixinBase):
    files = (
        ('core/views/chat.py', 'python', 'python3'),
        ('core/reflexes/chat_reflex.py', 'python', 'python3'),
        ('core/javascript/controllers/chat_controller.js', 'javascript', 'javascript'),
        ('core/templates/_chat_demo.html', 'html', 'htmldjango'),
    )


class CalendarMixin(MixinBase):
    files = (
        ('core/views/calendar.py', 'python', 'python3'),
        ('core/templates/_calendar.html', 'html', 'htmldjango'),
        ('core/templates/_td_calendar.html', 'html', 'htmldjango'),
 
    )


class NewsletterSignupMixin(MixinBase):
    files = (
        ('core/views/newsletter_signup.py', 'python', 'python3'),
        ('core/reflexes/newsletter_signup_reflex.py', 'python', 'python3'),
        ('core/templates/_newsletter_signup.html', 'html', 'htmldjango')
    )
