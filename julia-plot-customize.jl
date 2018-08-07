# Customizing matplotlib plots in julia. Add this to the beginning of the plot file and customize according to your needs.



using PyPlot

# Customize plot
PyPlot.matplotlib[:rc]("text", usetex = true)
PyPlot.matplotlib[:rc]("text.latex", preamble = "\\usepackage{amsmath}")
#PyPlot.matplotlib[:rc]("font", size = 18)
#PyPlot.matplotlib[:rc]("axes", labelsize = 15)
#PyPlot.matplotlib[:rc]("axes", titlesize = 18)
#PyPlot.matplotlib[:rc]("xtick", labelsize = 12)
#PyPlot.matplotlib[:rc]("ytick", labelsize = 12)
#PyPlot.matplotlib[:rc]("legend", fontsize = 15)
#PyPlot.matplotlib[:rc]("figure", titlesize = 18)
#PyPlot.matplotlib[:rc]("figure", dpi = 100)
PyPlot.matplotlib[:rc]("figure", figsize = (7,5), dpi = 120)

