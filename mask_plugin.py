from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import os

MASK_PATTERN = r'!mask\[(.*?)\]'

class MaskedTextProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('span')
        el.set('class', 'masked-text')
        el.text = m.group(1)
        return el, m.start(0), m.end(0)

class MaskedTextExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(MaskedTextProcessor(MASK_PATTERN, md), 'masked-text', 175)

class MaskPlugin(BasePlugin):
    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
    )

    def on_config(self, config):
        # 注册 Markdown 扩展
        config['markdown_extensions'].append(MaskedTextExtension())
        return config

    def on_post_build(self, config):
        # 注入 CSS 文件
        dest_dir = os.path.join(config['site_dir'], 'assets')
        os.makedirs(dest_dir, exist_ok=True)
        css_path = os.path.join(dest_dir, 'masked.css')
        with open(css_path, 'w') as f:
            f.write('''
.masked-text {
    color: black;
    background-color: black;
    border-radius: 3px;
    padding: 0 4px;
    transition: all 0.2s !important;
    cursor: pointer;
}
.masked-text:hover {
    color: var(--md-typeset-color, #000);
    background-color: transparent;
    transition: all 0.2s !important;
}
            ''')

    def on_post_page(self, output, page, config):
        # 注入 CSS 链接
        if '<head>' in output:
            output = output.replace(
                '<head>',
                '<head>\n<link rel="stylesheet" href="/assets/masked.css">'
            )
        return output
