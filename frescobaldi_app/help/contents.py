# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2008 - 2011 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
The help contents.
"""

from __future__ import unicode_literals

from .helpimpl import page, shortcut
from colorize import colorize

import info


class nohelp(page):
    """Shown when no help is found."""
    def title():
        return _("No Help")
    
    def body():
        return _("No help has been found on this topic.")


class contents(page):
    """Main help contents."""
    def title():
        return _("Frescobaldi Manual")
    
    def body():
        # L10N: Translate this sentence and fill in your own name to have it appear in the About Dialog.
        text = _(
r"""<p>Frescobaldi is a light-weight and powerful editor for LilyPond
sheet music documents.
This manual is written by {author} and documents {appname} version {version}.</p>"""
            ).format(author=info.maintainer, appname=info.appname, version=info.version)
        translator = _("Translated by Your Name.")
        if translator != "Translated by Your Name.":
            text += "<p>" + translator + "</p>"
        return text
    
    def children():
        import scorewiz.dialog
        return (
            introduction,
            starting,
            scorewiz.dialog.scorewiz_help,
            
            about,            
        )


class introduction(page):
    def title():
        return _("Introduction")
    
    def body():
        return _("""\
<p>
<a href="http://lilypond.org/">LilyPond</a>
is an open-source music engraving program, producing very high-quality sheet
music printouts from fairly simple text input files.
Those text files can be created with any text editor, and LilyPond then loads
the text file and outputs a beautiful engraving, by default in PDF format.
</p>

<p>
Frescobaldi is an application designed to make editing LilyPond music scores
faster and easier. You still will need to learn the LilyPond input language.
If you read the {getting_started} section of this User Guide, you'll also pickup
some LilyPond basics.
</p>

<p>
Then you can continue to learn using the Learning Manual from 
<a href="http://lilypond.org/doc/">LilyPond's excellent online documentation</a>.
</p>""").format(getting_started=starting.link())



class starting(page):
    def title():
        return _("Getting Started")
    
    def body(cls):
        import engrave, panels
        example=colorize(r"""\relative c'' {
  \time 7/4
  c2 bes4 a2 g a bes4 a( g) f2
}
\addlyrics {
  Join us now and share the soft -- ware!
}""")
        action = engrave.Engraver.instances()[0].actionCollection.engrave_preview
        key_engrave = shortcut(action)
        action = panels.PanelManager.instances()[0].musicview.actionCollection.music_jump_to_cursor
        key_jump = shortcut(action)
        return _("""\
<p>
The default screen of Frescobaldi shows a text document on the left and an
empty music preview on the right.
</p>

<p>
Now, in the text view, enter some LilyPond code, like this:
</p>

{example}

<p>
Then click the Lily toolbar button or press {key_engrave}.
If all is well, LilyPond starts now and processes your file.
At the bottom of the screen you can follow LilyPond's progress.
If LilyPond does not encounter any mistakes on your part, it will produce a PDF
file that will be displayed in the music preview:
</p>

<p><img src="getting_started1.png"></p>

<p>
The musicview has many possibilities:
<p>

<ul>
<li>
Hovering notes and other objects will highlight them in the text;
click objects to move the text cursor to them
</li>

<li>
Ctrl-wheel to change the zoom. Zooming will center at the mouse pointer
</li>

<li>
Ctrl-click on an empty place to show a magnifier glass
</li>

<li>
Moving the text cursor highlights the notes in the preview; press {key_jump}
to explicitly center and highlight a note or other object in the preview.
</li>
</ul>

<p>
If your music score is finished, it is recommended to run LilyPond with clickable
notes turned off: menu LilyPond->Engrave (publish). This will result in much
smaller PDF documents.
</p>

<p>
If LilyPond does not start at all, check if you have installed LilyPond
correctly and that the lilypond command is in your system's PATH environment
variable. If needed, provide the exact path to your LilyPond executable under
Edit->Preferences->LilyPond preferences.
</p>
""").format(example=example, key_engrave=key_engrave, key_jump=key_jump)


class about(page):
    def title():
        return _("About Frescobaldi")
    
    def body():
        return _("""\
<p>
Frescobaldi is named after
<a href="http://en.wikipedia.org/wiki/Girolamo_Frescobaldi">Girolamo
Frescobaldi (1583 &#8211; 1643)</a>, an Italian organist and composer.
</p>

<p>
Frescobaldi's homepage is at
<a href="http://www.frescobaldi.org/">www.frescobaldi.org</a>
and there is a mailinglist at
<a href="mailto:frescobaldi@googlegroups.com">frescobaldi@googlegroups.com</a>
(<a href="http://groups.google.com/group/frescobaldi">more info</a>).
</p>
""")
    def children():
        return (
            credits,
            contributing,
            history,
        )


class credits(page):
    def title():
        return _("Credits")

    def body():
        text = []
        text.append(
            _("Frescobaldi's main author is {author}.").format(author=info.maintainer))
        import about
        text.extend(about.credits())
        return '\n'.join(map('<p>{0}</p>'.format, text))


class contributing(page):
    def title():
        return _("Contributing")
    
    def body():
        return _("""\
<p>
Frescobaldi is a <a href="http://www.gnu.org/philosophy/free-sw.html">Free
Software</a> project to create a user friendly LilyPond music score editor.
The goal is to make Frescobaldi available on all major platforms.
</p>

<p>
Frescobaldi is developed in a public GitHub repository at {url}.
There you can browse or checkout the source code and report bugs and wishes.
</p>

<p>
You can contribute by simply using Frescobaldi and reporting bugs and suggestions.
Translations are also very welcome. How to create new translations is described
in the file README-translations in the source distribution of Frescobaldi.
If you want to add functionality you can find information about the source code
structure in the file README-development.
</p>
""").format(url='<a href="http://github.com/wbsoft/frescobaldi">'
                'github.com/wbsoft/frescobaldi</a>')


class history(page):
    def title():
        return _("History of Frescobaldi")

    def body():
        return _("""\
<p>
Frescobaldi has its roots in LilyKDE, which was a plugin for KDE3's editor Kate.
LilyKDE was written in Python and released in 2007 on Christmas.
</p>

<p>
When KDE developed version 4, it was not immediately possible to make Kate
plugins in Python. So LilyKDE became a standalone application, wrapping the
Kate texteditor part, and was renamed to Frescobaldi. It still used the Okular
KDE part to display PDF documents.
Frescobaldi 0.7 was the first public release, on Christmas 2008.
On Christmas 2009 version 1.0.0 was released and on Christmas 2010 version 1.2.0.
</p>

<p>
At that time it was decided to move away from the KDE4 libraries and just use
Python and Qt4 which are easily available on all major computing platforms.
Frescobaldi 2.0 is a complete rewrite from scratch. Its release date is
targeted at Christmas 2011.
</p>
""")


