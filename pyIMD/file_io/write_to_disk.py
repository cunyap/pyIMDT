from pyIMD.error.error_handler import ArgumentError

__author__ = 'Andreas P. Cuny'


def write_to_png(plot_object, file, **kwargs):
    """write_to_png  Writes figure in png format to current directory

    Args:
    :param plot_object:       ggplot object
    :param file:              File path + File name [String] for figure to save

    Kwargs:
    :keyword width:             Figure width (optional)
    :keyword height:            Figure height (optional)
    :keyword units:             Figure units (optional) 'in', 'mm' or 'cm'
    :keyword resolution:        Figure resolution in dots per inch [dpi] (optional)

    Returns:
    :return:                   Writes figure to disk
    """
    if 'width' and 'height' and 'units' and 'resolution' in kwargs:
        width = kwargs.get('width')
        height = kwargs.get('height')
        units = kwargs.get('units')
        resolution = kwargs.get('resolution')
        plot_object.save(filename='{}.png'.format(file), width=width, height=height, units=units, dpi=resolution)
    elif not kwargs:
        plot_object.save(filename='{}.png'.format(file))
    else:
        raise ArgumentError(write_to_png.__doc__)


def write_to_pdf(plot_object, file, **kwargs):
    """write_to_pdf Writes figure in pdf format to current directory

    Args:
    :param plot_object:         ggplot object
    :param file:                File path + File name [String] for figure to save

    Kwargs:
    :keyword width:             Figure width (optional)
    :keyword height:            Figure height (optional)
    :keyword units:             Figure units (optional) 'in', 'mm' or 'cm'
    :keyword resolution:        Figure resolution in dots per inch [dpi] (optional)

    Returns:
    :return:                    Writes figure to disk

    """
    if 'width' and 'height' and 'units' and 'resolution' in kwargs:
        width = kwargs.get('width')
        height = kwargs.get('height')
        units = kwargs.get('units')
        resolution = kwargs.get('resolution')
        plot_object.save(filename='{}.pdf'.format(file), width=width, height=height, units=units, dpi=resolution)
    elif not kwargs:
        plot_object.save(filename='{}.pdf'.format(file))
    else:
        raise ArgumentError(write_to_pdf.__doc__)


def write_to_disk_as(file_format, plot_object, file, **kwargs):
    if file_format == 'pdf':
        write_to_pdf(plot_object, file, **kwargs)
    elif file_format == 'png':
        write_to_png(plot_object, file, **kwargs)
    else:
        raise Exception("This figure format is currently not supported.")
