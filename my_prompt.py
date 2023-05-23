import re

def convert_to_markdown(titles_string):
    titles = titles_string.strip().split('\n')
    markdown_titles = []
    line_cnt = 0
    for title in titles:
        line_cnt = line_cnt + 1
        if line_cnt == 1:
            markdown_title = '# ' + title
        else:
            serial_number, text = title.split(' ', 1)
            num_of_hashes = serial_number.count('.')
            markdown_title = '#' * (num_of_hashes + 2) + ' ' + serial_number + ' ' + text
        markdown_titles.append(markdown_title)
    return '\n'.join(markdown_titles)


def  gpt_content_gen_prompt(text = ' ', info = ' ', format = 'Markdown'):
    markdown_text = convert_to_markdown(text)
    prompt = f"""
0. After reading the whole prompt, then output as \
required:
1. Only <read> given information <delimited by \
double backticks> and <make no output>: 
``{info}``.
2. Answer the questions in the text <delimited by \
triple backticks>.Put the answer below each question.
3. Output <[original serial numbered questions] and \
[generated answers]> in <hierarchical raw grammarly \
{format} format>.
```{markdown_text}```
"""
    return prompt

def gpt_content_gen_prompt_test(text = ' ', info = ' ', format = 'Markdown'):
    prompt = f"""
    [
    "requirements": [
        "input text":"```{text}```",
        "input info":"``{info}``",
        "output format":"{format}",
        "tasks":[
        "task-1":"Read given information in <input info> and <make no output>;",
        "task-2":"Answer the questions in the <input text>. Put the content below each question.",
        "task-3":"Output in <output format>."
        ]
    ]
    ]
    """
    return prompt

def  gpt_code_gen_prompt(text = ' ', info = ' '):
    prompt = f"""
0. After reading the whole prompt, then output as \
required:
1. Only <read> given information <delimited by\
double backticks> and <make no output>: 
``{info}``.
2. Write code as required in the text <delimited by\
triple backticks>.
```{text}```
"""
    return prompt
def gpt_paper_sum_prompt(format = 'Markdown'):
    text = f"""
    " 
    ## Summary,\
    ## Research Objective(s),\
    ## Background / Problem Statement,\
    ## Method(s),\
    ## Evaluation,\
    ## Conclusion,\
    ## Notes,\
    ## References 
    " """

    prompt = f"""
    Fulfill the content under the titles correspondingly, \
    which are descripted in the below text delimited by \
    triple backticks. 
    Output titles and contents in {format}.
    ```{text}```"""
    return prompt
