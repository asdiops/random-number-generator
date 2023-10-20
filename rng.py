from random import randint
from flask import Flask, render_template
import os

#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"
def get_rand_num():
    random_num = randint(1, 100)

    return render_template('verymain.html', random_num=random_num)

def main():
    get_rand_num()
    return render_template('verymain.html')

#def result():
#    print(session['total'], session['answers'])
#    total = session['total']
#    answers = session['answers']
#    end_quiz()
#    return render_template('result.html', total=total, answers=answers)
#def question_form(question):
#    answer_list = [question[2], question[3], question[4], question[5]]
#    shuffle(answer_list)
#    quest_id = question[0]
#    print(answer_list)
#    return render_template('test.html', question=question[1], answer_list=answer_list, quest_id=quest_id)

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)
app.add_url_rule('/', 'main', main)
app.add_url_rule('/rand', 'rdn', get_rand_num)

app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == "__main__":
    app.run()


#     <p>Ваше случайное чило:{{СЛУЧАЙНОЕ ЧИСЛО(которое генерируется сверху)}}</p>  
#     <br><input class="btn btn-success rounded-pill px-3" type="submit" value="Генерировать"></br>  
#        В таком варианте наверно должна обновляться страница и генерировать число снова  
#
#     
#<% if КНОПКА ГЕНЕРИРОВАТЬ НАЖАТА%>  
#<p>Ваше случайное чило:{{СЛУЧАЙНОЕ ЧИСЛО}}</p>  
#<% endif %>  
#но тут только после if должна создаваться  кнопка