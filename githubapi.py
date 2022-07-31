
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# data request
url = 'https://github.com/orgs/futurice/repositories'
r = requests.get(url)
text = r.json()
repo_dicts = text['items']

 # input
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

 # colour coordination 
my_style = LS('#333366', base_style=LCS)

 # 
my_config = pygal.Config()    
my_config.x_label_rotation = 45    
my_config.show_legend =  Ложь 
my_config.title_font_size = 24    
my_config.label_font_size = 14    
my_config.major_label_font_size = 18               
my_config.truncate_label = 15    
my_config.show_y_guides =  False 
my_config.width = 1000    

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Самая популярная программа GitHub Python"
chart.x_labels =  

chart.add('', plot_dicts)    
chart.render_to_file('python_repos.svg')


