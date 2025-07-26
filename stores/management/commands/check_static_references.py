from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import re
from pathlib import Path

class Command(BaseCommand):
    help = "Scan templates and CSS for static file references and verify files exist"

    template_pattern = re.compile(r"{%%\s*static ['\"](?P<path>[^'\"]+)['\"]\s*%%}")
    css_pattern = re.compile(r"url\((?:'|\")?(?P<path>static/[^)'\"]+)")

    def handle(self, *args, **options):
        base_dirs = [
            Path(settings.BASE_DIR) / 'static',
            Path(settings.BASE_DIR) / 'frontend' / 'dist' / 'assets',
        ]
        missing = []

        def exists(rel_path):
            rel_path = rel_path.split('?', 1)[0].split('#', 1)[0]
            for base in base_dirs:
                if (base / rel_path).exists():
                    return True
            return False

        # Scan templates
        templates_dir = Path(settings.BASE_DIR) / 'templates'
        for root, _, files in os.walk(templates_dir):
            for fname in files:
                if not fname.endswith(('.html', '.htm', '.txt')):
                    continue
                fpath = Path(root) / fname
                with open(fpath, encoding='utf-8') as fh:
                    for lineno, line in enumerate(fh, start=1):
                        for match in self.template_pattern.finditer(line):
                            rel = match.group('path')
                            if not exists(rel):
                                missing.append(f"{fpath}:{lineno} -> {rel}")

        # Scan CSS files
        css_files = []
        for base in base_dirs:
            if base.exists():
                for root, _, files in os.walk(base):
                    for fname in files:
                        if fname.endswith('.css'):
                            css_files.append(Path(root) / fname)
        for css_file in css_files:
            with open(css_file, encoding='utf-8') as fh:
                for lineno, line in enumerate(fh, start=1):
                    for match in self.css_pattern.finditer(line):
                        rel = match.group('path')[len('static/'):]  # remove leading static/
                        if not exists(rel):
                            missing.append(f"{css_file}:{lineno} -> {rel}")

        if missing:
            missing_report = '\n'.join(missing)
            self.stderr.write(self.style.ERROR('Missing static file references found:'))
            self.stderr.write(missing_report)
            raise CommandError('Static reference check failed')
        self.stdout.write(self.style.SUCCESS('All static references are valid'))
