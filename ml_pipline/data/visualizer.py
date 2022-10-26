from html import entities
import json
import gradio as gr

import ml_pipline.data.sqlite_source as repo

def convert_json_to_text(json_text):
    output_text = ""

    for section in json_text:
        output_text += section["section_title"] + "\n"
        output_text += section["text"] + "\n"

    return output_text

def main():
    r = repo.SQLiteSource("./ml_pipline/data/dataset.db")
    ids = r.get_ids()

    def update(doc_id):
        results = r.get_by_ids(doc_id)[0]
        document, lbl_string = results
        document = convert_json_to_text(document)
        labels = lbl_string.split("|")
        entities = []

        for lbl in labels:
            idx = document.find(lbl)
            if idx != -1:
                entities.append(dict(
                    entity="Dataset",
                    start=idx,
                    end=idx+len(lbl)
                ))

        document = dict(
            text=document,
            entities=entities,
        )
        return document, lbl_string


    with gr.Blocks() as demo:
        gr.Markdown("Select a paper")
        dropdown = gr.Dropdown(ids[:10])
        btn = gr.Button("Fetch Document")
        # with gr.Row():
            # with gr.Column(scale=1):
        labels = gr.Textbox()
        text_area = gr.HighlightedText(combine_adjacent=True)
            # with gr.Column(scale=1):
        # dropdown.change(fn=update, inputs=dropdown, outputs=[text_area, out])
        btn.click(fn=update, inputs=dropdown, outputs=[text_area, labels])

    demo.launch()


if __name__=="__main__":
    main()