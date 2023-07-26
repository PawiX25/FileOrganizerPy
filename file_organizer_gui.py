import os
import shutil
import wx

def get_category(file_extension):
    categories = {
        "Documents": ["txt", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"],
        "Images": ["jpg", "jpeg", "png", "gif", "bmp"],
        "Videos": ["mp4", "avi", "mkv", "mov", "wmv"],
        "Music": ["mp3", "ogg", "wav", "flac"],
    }

    for category, extensions in categories.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_files(source_folder, destination_folder, move_files=True, sort_by_category=True):
    total_files_moved = 0
    total_errors = 0

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, _, files in os.walk(source_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1][1:]  # Get the file extension without the dot

                if sort_by_category:
                    category = get_category(file_extension)
                    destination_path = os.path.join(destination_folder, category)
                else:
                    destination_path = os.path.join(destination_folder, file_extension)

                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                try:
                    if move_files:
                        shutil.move(file_path, os.path.join(destination_path, filename))
                        total_files_moved += 1
                    else:
                        shutil.copy2(file_path, os.path.join(destination_path, filename))
                        total_files_moved += 1
                except shutil.Error:
                    total_errors += 1

    summary = f"Total {total_files_moved} files organized with {total_errors} errors."
    return summary

class FileOrganizerPy(wx.Frame):
    def __init__(self, parent, title):
        super(FileOrganizerPy, self).__init__(parent, title=title, size=(400, 250))
        self.panel = wx.Panel(self)

        self.source_label = wx.StaticText(self.panel, label="Source Folder:")
        self.source_edit = wx.TextCtrl(self.panel)
        self.source_browse_button = wx.Button(self.panel, label="Browse")

        self.destination_label = wx.StaticText(self.panel, label="Destination Folder:")
        self.destination_edit = wx.TextCtrl(self.panel)
        self.destination_browse_button = wx.Button(self.panel, label="Browse")

        self.copy_checkbox = wx.CheckBox(self.panel, label="Copy files instead of moving")
        self.sort_checkbox = wx.CheckBox(self.panel, label="Sort by file categories")

        self.organize_button = wx.Button(self.panel, label="Organize Files")
        self.cancel_button = wx.Button(self.panel, label="Cancel")

        self.__set_properties()
        self.__do_layout()
        self.__bind_events()

    def __set_properties(self):
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

    def __do_layout(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer1.Add(self.source_label, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer1.Add(self.source_edit, 1, wx.ALL | wx.EXPAND, 5)
        sizer1.Add(self.source_browse_button, 0, wx.ALL, 5)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2.Add(self.destination_label, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer2.Add(self.destination_edit, 1, wx.ALL | wx.EXPAND, 5)
        sizer2.Add(self.destination_browse_button, 0, wx.ALL, 5)

        main_sizer.Add(sizer1, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(sizer2, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.copy_checkbox, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.sort_checkbox, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.organize_button, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.cancel_button, 0, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizer(main_sizer)
        self.Layout()

    def __bind_events(self):
        self.source_browse_button.Bind(wx.EVT_BUTTON, self.on_browse_source)
        self.destination_browse_button.Bind(wx.EVT_BUTTON, self.on_browse_destination)
        self.organize_button.Bind(wx.EVT_BUTTON, self.on_organize_files)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

    def on_browse_source(self, event):
        dlg = wx.DirDialog(self, "Select Source Folder")
        if dlg.ShowModal() == wx.ID_OK:
            self.source_edit.SetValue(dlg.GetPath())
        dlg.Destroy()

    def on_browse_destination(self, event):
        dlg = wx.DirDialog(self, "Select Destination Folder")
        if dlg.ShowModal() == wx.ID_OK:
            self.destination_edit.SetValue(dlg.GetPath())
        dlg.Destroy()

    def on_organize_files(self, event):
        source_folder = self.source_edit.GetValue()
        destination_folder = self.destination_edit.GetValue()
        copy_files = self.copy_checkbox.GetValue()
        sort_by_category = self.sort_checkbox.GetValue()

        if not source_folder or not destination_folder:
            wx.MessageBox("Please select both source and destination folders.", "Error", wx.OK | wx.ICON_ERROR)
            return

        move_files = not copy_files

        try:
            summary = organize_files(source_folder, destination_folder, move_files, sort_by_category)
            wx.MessageBox(summary, "Success", wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox(f"An error occurred: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)

    def on_cancel(self, event):
        self.Close()

if __name__ == "__main__":
    app = wx.App(False)
    frame = FileOrganizerPy(None, "FileOrganizerPy")
    frame.Show()
    app.MainLoop()
