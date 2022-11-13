import re

import gradio as gr

import ml_pipeline.data.sqlite_source as repo

def convert_json_to_text(json_text):
    output_text = ""

    for section in json_text:
        output_text += section["section_title"] + " "
        output_text += section["text"]

    return output_text

def main():
    r = repo.SQLiteSource("./ml_pipeline/data/dataset.db")
    ids = r.get_ids()

    def update(doc_id):
        results = r.get_by_ids(doc_id)[0]
        document, lbl_string = results
        document = convert_json_to_text(document)
        labels = lbl_string.split("|")


        lbl_entities = []

        entities = []
        l_idx = 0
        for i, lbl in enumerate(labels, start=1):
            lbl_entities.append(dict(
                entity=f"Dataset {i}",
                start=l_idx,
                end=l_idx+len(lbl)
            ))
            l_idx += len(lbl)+1
            idxs = [m.start() for m in re.finditer(lbl, document)]
            for idx in filter(lambda idx: idx!=-1, idxs):
                entities.append(dict(
                    entity=f"Dataset {i}",
                    start=idx,
                    end=idx+len(lbl)
                ))

        document = dict(
            text=document,
            entities=entities,
        )
        labels = dict(
            text = lbl_string,
            entities=lbl_entities
        )
        return document, labels


    with gr.Blocks() as demo:
        gr.Markdown("Select a paper")
        dropdown = gr.Dropdown(ids)
        btn = gr.Button("Fetch Document")
        # with gr.Row():
            # with gr.Column(scale=1):
        labels = gr.HighlightedText()
        text_area = gr.HighlightedText(combine_adjacent=True)
            # with gr.Column(scale=1):
        # dropdown.change(fn=update, inputs=dropdown, outputs=[text_area, out])
        btn.click(fn=update, inputs=dropdown, outputs=[text_area, labels])

    demo.launch()


if __name__=="__main__":
    main()