from IPython.core.display import display, HTML

def get_github_nbviewer_link(github_url):
    git_url = github_url.split('https://github.com/')[1]
    nb_viewer_url = 'http://nbviewer.jupyter.org/github/' + git_url
    
    notebook_name = git_url.split('/')[-1].split('.ipynb')[0]
    
    link = "<a style='text-decoration:none' href='{}' target='_blank'>Open {} in nbviewer</a>".format(nb_viewer_url, notebook_name)
    display(HTML(link))
