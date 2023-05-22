
def  gpt_content_gen_prompt(text = ' ', info = ' ', format = 'Markdown'):
    prompt = f"""
0. After reading the whole prompt, then output as \
required:
1. Only <read> given information <delimited by \
double backticks> and <make no output>: 
``{info}``.
2. Answer the questions in the text <delimited by \
triple backticks>.Put the answer below each question.
3. Output <[original serial numbered questions] and \
[generated answers]> in <hierarchical raw {format} \
grammar format>.
```{text}```
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
