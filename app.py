from shiny import App, Inputs, Outputs, Session, render, ui

app_ui = ui.page_fluid(
    ui.h2("Mortgage Calculator"),
    ui.input_slider("price", "Home Price", 200000, 400000, 500),
    ui.input_slider("downpayment", "Down Payment %", 10, 20, 1),
    ui.input_slider("term", "Term in Years", 15, 30, 15),
    ui.input_slider("hoa", "HOA", 200, 400, 50),
    ui.output_text_verbatim("monthly"),
    ui.h3("What could this likely rent for?"),
    ui.input_slider("rent", "Monthly Rent", 1100, 1800, 100),
)


def server(input, output, session):
    @output
    @render.text
    def monthly():
        downpay_total = input.price() * (input.downpayment()/100)
        annual_mortgage = (input.price() - downpay_total)/input.term()
        monthly_mortgage = (annual_mortgage/12) + input.hoa()
        return f"Monthly Mortgage is $ {monthly_mortgage}"


app = App(app_ui, server)
