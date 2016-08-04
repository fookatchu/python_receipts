
# Show maximized plot on second monitor (with qt backend)
mgr = plt.get_current_fig_manager()
mgr.window.move(2000,0)
mgr.window.showMaximized()