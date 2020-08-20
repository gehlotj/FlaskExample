from flask import render_template, url_for, request, flash, session, make_response, Blueprint
from bs4 import BeautifulSoup
from download_images.image_url import GetImageURL

di  = Blueprint("download_images",__name__)

@di.route('/')
def home():
    session.permanent = True
    if 'history' not in session:
        session['history'] = []
    return render_template("index.html",history=session.get('history'))


@di.route('/url_submission', methods=['GET','POST'])
def url_submission():
    if request.method == "POST":
        url_to_get_img = request.form['url_name']

        if 'history' not in session:
            session['history'] = []

        if url_to_get_img not in session['history']:
            session['history'].append(url_to_get_img)

        images = GetImageURL(url_to_get_img).get_images_from_url()
        return render_template("url_submission.html",images=images)
    else:
        flash("The page is not accessible. Resubmit the form")
        return render_template("error.html")
