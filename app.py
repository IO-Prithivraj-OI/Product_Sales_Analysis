from flask import Flask, render_template
import pandas as pd
import plotly.express as px
from io import StringIO

app = Flask(__name__)

# Load the data
dim_customer = pd.read_csv("Dim_Customer.csv")
dim_products = pd.read_csv("Dim_Products.csv")
dim_date = pd.read_csv("Dim_Date_Excel.csv")
fact_internet_sale = pd.read_csv("FactInternetSale.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sales')
def sales():
    # Join fact_internet_sale with dim_products for sales visualization
    sales_data = pd.merge(fact_internet_sale, dim_products, on='ProductKey', how='inner')
    sales_fig_bar = px.bar(sales_data, x='Product Name', y='SalesAmount', title='Product Sales (Bar Chart)')
    sales_fig_bar.update_layout(
        height=600,
        xaxis_title="Product Name",
        yaxis_title="Sales Amount",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title_font=dict(size=22),
        xaxis=dict(tickfont=dict(size=14)),
        yaxis=dict(tickfont=dict(size=14)),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    sales_graph_bar = sales_fig_bar.to_html(full_html=False)

    return render_template('sales.html', sales_graph_bar=sales_graph_bar)

@app.route('/customers')
def customers():
    # Customer's city distribution visualization
    customer_fig_pie = px.pie(dim_customer, names='Customer City', title='Customer City Distribution (Pie Chart)')
    customer_fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    customer_fig_pie.update_layout(
        height=600,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title_font=dict(size=22),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    customer_graph_pie = customer_fig_pie.to_html(full_html=False)

    return render_template('customers.html', customer_graph_pie=customer_graph_pie)

@app.route('/products/categories')
def product_categories():
    products_fig_bar = px.bar(dim_products, x='Product Category', title='Product Categories Distribution (Bar Chart)')
    products_fig_bar.update_layout(
        height=600,
        xaxis_title="Product Category",
        yaxis_title="Count",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title_font=dict(size=22),
        xaxis=dict(tickfont=dict(size=14)),
        yaxis=dict(tickfont=dict(size=14)),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    product_graph_bar = products_fig_bar.to_html(full_html=False)

    return render_template('product_categories.html', product_graph_bar=product_graph_bar)

@app.route('/products/colors')
def product_colors():
    products_fig_pie = px.pie(dim_products, names='Product Color', title='Product Colors Distribution (Pie Chart)')
    products_fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    products_fig_pie.update_layout(
        height=600,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title_font=dict(size=22),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    product_graph_pie = products_fig_pie.to_html(full_html=False)

    return render_template('product_colors.html', product_graph_pie=product_graph_pie)

@app.route('/sales/trends')
def sales_trends():
    # Merge fact_internet_sale with dim_date for date details
    sales_trend_data = pd.merge(fact_internet_sale, dim_date, left_on='OrderDateKey', right_on='DateKey', how='inner')
    sales_trends_fig = px.line(sales_trend_data, x='Date', y='SalesAmount', title='Sales Trends Over Time (Line Chart)')
    sales_trends_fig.update_layout(
        height=600,
        xaxis_title="Order Date",
        yaxis_title="Sales Amount",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title_font=dict(size=22),
        xaxis=dict(tickfont=dict(size=14)),
        yaxis=dict(tickfont=dict(size=14)),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    sales_trends_graph = sales_trends_fig.to_html(full_html=False)

    return render_template('sales_trends.html', sales_trends_graph=sales_trends_graph)

@app.route('/customers/gender')
def customer_gender():
    customer_gender_fig_pie = px.pie(dim_customer, names='Gender', title='Customer Gender Distribution (Pie Chart)')
    customer_gender_fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    customer_gender_fig_pie.update_layout(
        height=600,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title_font=dict(size=22),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    customer_gender_graph_pie = customer_gender_fig_pie.to_html(full_html=False)

    return render_template('customer_gender.html', customer_gender_graph_pie=customer_gender_graph_pie)

@app.route('/products/line')
def product_line():
    products_line_fig_bar = px.bar(dim_products, x='Product Line', title='Product Line Distribution (Bar Chart)')
    products_line_fig_bar.update_layout(
        height=600,
        xaxis_title="Product Line",
        yaxis_title="Count",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title_font=dict(size=22),
        xaxis=dict(tickfont=dict(size=14)),
        yaxis=dict(tickfont=dict(size=14)),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    product_line_graph_bar = products_line_fig_bar.to_html(full_html=False)

    return render_template('product_line.html', product_line_graph_bar=product_line_graph_bar)

@app.route('/products/model')
def product_model():
    products_model_fig_bar = px.bar(dim_products, x='Product Model Name', title='Product Model Distribution (Bar Chart)')
    products_model_fig_bar.update_layout(
        height=600,
        xaxis_title="Product Model",
        yaxis_title="Count",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        title_font=dict(size=22),
        xaxis=dict(tickfont=dict(size=14)),
        yaxis=dict(tickfont=dict(size=14)),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    product_model_graph_bar = products_model_fig_bar.to_html(full_html=False)

    return render_template('product_model.html', product_model_graph_bar=product_model_graph_bar)

@app.route('/products')
def products():
    # Create a DataFrame for the product list
    products_list = dim_products[['ProductKey', 'Product Name', 'Product Category', 'Product Color']]
    # Convert the DataFrame to HTML
    table_html = products_list.to_html(classes='data', header="true", index=False)
    return render_template('products.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
