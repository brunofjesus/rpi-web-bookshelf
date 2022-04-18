from flask import Flask, render_template, request

from bookshelf.parser import Parser

app = Flask(__name__)


def main():
    app.run(host="0.0.0.0", port=8080)


@app.route('/')
def root():
    sections = Parser().parse_sections()

    param_section = request.args.get('section')

    active_section = sections[0]
    if param_section:
        for section in sections:
            if section.id == param_section:
                active_section = section
                break

    return render_template('template.html', sections=sections, active_section=active_section)


if __name__ == '__main__':
    main()
