import base64

import matplotlib.pyplot as plt
import seaborn as sns
import io


def get_image():
    # Create bytes buffer for the image to save
    buffer = io.BytesIO()
    # Create the plot with the use of BytesIO object as its 'file'
    plt.savefig(buffer, format='png')
    # set the cursor the beginning of the stream
    buffer.seek(0)
    # retrieve the entire content of the 'file'
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the memory of buffer
    buffer.close()

    return graph


def get_simple_plot(chart_type, *args, **kwargs):
    # https://matplotlib.org/faq/usage_faq.html?highlight=backend#what-is-a-backend
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))

    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')

    if chart_type == 'bar':
        title = 'total price by day (bar)'
        plt.title(title)
        plt.bar(x, y)
    elif chart_type == 'line':
        title = 'title'
        plt.title(title)
        plt.plot(x, y)
    else:
        title = 'Product count'
        plt.title(title)
        sns.countplot('name', data=data)

    plt.tight_layout()

    graph = get_image()
    return graph
