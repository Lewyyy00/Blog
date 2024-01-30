from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm


@app.route("/")
def index():
   all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())

   return render_template("homepage.html", all_posts=all_posts)
'''
@app.route("/new-post/", methods=["GET", "POST"])
def edit_or_create_entry():
   form = EntryForm()
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           entry = Entry(
                title=form.title.data,
                body=form.body.data,
                is_published=form.is_published.data
            )
           db.session.add(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
   entry = Entry.query.filter_by(id=entry_id).first_or_404()
   form = EntryForm(obj=entry)
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           form.populate_obj(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)
'''

@app.route("/post_editor/", methods=["GET", "POST"])
@app.route("/post_editor/<int:entry_id>", methods=["GET", "POST"])
def edit_or_create_entry(entry_id=None):
    form = EntryForm()
    errors = None
    if entry_id:
        entry = Entry.query.get(entry_id)
    else:
        entry = None

    if entry and request.method == 'GET':
        form = EntryForm(obj=entry)

    if form.validate_on_submit():
        if not entry:
            entry = Entry(
                title=form.title.data,
                body=form.body.data,
                is_published=form.is_published.data
            )
            db.session.add(entry)
        else:
            form.populate_obj(entry)
        db.session.commit()
    else:
        errors = form.errors

    return render_template("entry_form.html", form=form, errors=errors, entry_id=entry_id)




