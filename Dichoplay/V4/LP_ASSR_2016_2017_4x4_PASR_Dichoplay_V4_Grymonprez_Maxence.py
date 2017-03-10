# -*- coding: UTF-8 -*-

#! /usr/bin/env python3.5

# ---------------------------------------------------------------------
# Title: Dichoplay V4
# A Dichoplay game using Tkinter library
#
# Author: Grymonprez Maxence
# Email: maxgrymonprez@live.fr
# ---------------------------------------------------------------------
# All libs are part of standard distribution for python 3.5

from tkinter import Tk, Menu, Label, Button, Entry, Radiobutton, LabelFrame, messagebox
from tkinter import SUNKEN, GROOVE, CENTER, LEFT, RIGHT
from tkinter import IntVar, StringVar, BooleanVar, Toplevel, mainloop
from threading import Timer
from random import randint

class Dichoplay():

        def __init__(self):

	# Set up variables

                self.levels = {
                        1: {
                                "title": "Easy",
                                "min": 0,
                                "max": 100
                        },
                        2: {
                                "title": "Normal",
                                "min": 0,
                                "max": 500
                        },
                        3: {
                                "title": "Hard",
                                "min": 0,
                                "max": 1000
                        },
                        4: {
                                "title": "\"It's over 9000\"", 
                                "min": 0, 
                                "max": 9000
                        },
                        5: {
                                "title": "Welcome to Hell",
                                "min": 666,
                                "max": 666666
                        }
                }

                self._set_up_main_frame()

        def _set_up_main_frame(self):

                """
                        Set up main frame.

                        :param self:            (self)
                """

                # Set main window

                self.root = Tk()
                self.root.title('Dichoplay game')

                # Set variables

                self.level = IntVar()
                self.level.set(next (iter (self.levels))) # Select default level (first level in dict)

                self.cheat_mode = BooleanVar()
                self.cheat_mode.set(False) # Default

                self.game_try_count = IntVar()
                self.game_timer = IntVar()
                self.game_range_min = IntVar()
                self.game_range_max = IntVar()

                self.entry_number = StringVar()
                self.show_result = StringVar()

                self.settings_try_count = IntVar()
                self.settings_try_count.set(0)
                self.settings_timer = IntVar()
                self.settings_timer.set(0)

                self.game_started = BooleanVar()
                self.game_started.set(False)
                self.game_try_count_status = BooleanVar()
                self.game_try_count_status.set(False)
                self.game_timer_status = BooleanVar()
                self.game_timer_status.set(False)

                # Set dialog

                # Set menubar

                self.menubar = Menu(self.root)

                gamemenu = Menu(self.menubar, tearoff=0)
                gamemenu.add_command(label="Start game", command=lambda: self.start_game(lblTryCount, lblTimer))
                gamemenu.add_separator()
                gamemenu.add_command(label="Quit", command=self.root.destroy)
                
                optionsmenu = Menu(self.root, tearoff=0)
                levelmenu = Menu(optionsmenu, tearoff=0)
                # Filling from dict "levels"
                for k in self.levels.keys():
                        levelmenu.add_radiobutton(label=self.levels.get(k)["title"], variable=self.level, value=k)
                optionsmenu.add_cascade(label="Level", menu=levelmenu)
                cheatmenu = Menu(optionsmenu, tearoff=0)
                cheatmenu.add_radiobutton(label="Actived", variable=self.cheat_mode, value=True)
                cheatmenu.add_radiobutton(label="Desactived", variable=self.cheat_mode, value=False)
                optionsmenu.add_cascade(label="Cheat mode", menu=cheatmenu)
                optionsmenu.add_command(label="Settings", command=self._set_up_settings_frame)
                self.menubar.add_cascade(label="Game", menu=gamemenu)
                self.menubar.add_cascade(label="Options", menu=optionsmenu)
                self.root.config(menu=self.menubar)

                # Set main frame
                
                lbl = Label(self.root, text="Try count")
                lbl.grid(row=0, column=0, padx=10, pady=(2,1))
                lblResult = Label(self.root, relief=GROOVE, width=25, height=2, justify=CENTER, textvariable=self.show_result)
                lblResult.grid(row=1, column=1)
                lbl = Label(self.root, text="Timer")
                lbl.grid(row=0, column=2, padx=10, pady=(2,1))
                lblTryCount = Label(self.root, relief=SUNKEN, width=8, textvariable=self.game_try_count)
                lblTryCount.grid(row=1, column=0, padx=10, pady=(0,10))
                lblTimer = Label(self.root, relief=SUNKEN, width=8, textvariable=self.game_timer)
                lblTimer.grid(row=1, column=2, padx=10, pady=(0,10))
                
                lblFrame = LabelFrame(self.root, text="Range")
                lbl = Label(lblFrame, text="Minimum")
                lbl.grid(row=3, column=0, pady=(0,1))
                lbl = Label(lblFrame, text="Maximum")
                lbl.grid(row=3, column=1, pady=(0,1))
                lblRangeMin = Label(lblFrame, width=20, textvariable=self.game_range_min)
                lblRangeMin.grid(row=4, column=0)
                lblRangeMax = Label(lblFrame, width=20, textvariable=self.game_range_max)
                lblRangeMax.grid(row=4, column=1)
                lblFrame.grid(columnspan=3, padx=10, pady=(0,10))

                lbl = Label(self.root, text="Enter a number")
                lbl.grid(row=5, column=0, columnspan=3, padx=10, pady=(0,1))
                entryGame = Entry(self.root, justify=CENTER, width=30, textvariable=self.entry_number)
                entryGame.grid(row=6, column=0, columnspan=3, padx=10)
                btnGame = Button(self.root, text="Test it !", command=self.submit_number)
                btnGame.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
                
        def _set_up_settings_frame(self):

                """
                        Set up settings frame.
		
                        :param self:            (self)
                """

                # Set toplevel frame

                settingsFrame = Toplevel(self.root)
                
                # Set dialog

                # Try count setup
                lblFrameTryCount = LabelFrame(settingsFrame, text="Try count")
                lblFrameTryCount.pack(fill="both", expand="yes", padx=15, pady=5)
                lblFrameTryCount.columnconfigure(0, weight=1)
                lbl = Label(lblFrameTryCount, text="Set count")
                lbl.grid(row=0, column=0, padx=10, pady=(2,0))
                entryTryCount = Entry(lblFrameTryCount, justify=CENTER)
                entryTryCount.insert (0, self.settings_try_count.get())
                entryTryCount.grid(row=1, column=0, padx=10, pady=10)

                # Timer setup
                lblFrameTimer = LabelFrame(settingsFrame, text="Timer")
                lblFrameTimer.pack(fill="both", expand="yes", padx=15, pady=5)
                lblFrameTimer.columnconfigure(0, weight=1)
                lbl = Label(lblFrameTimer, text="Set timer (in second)")
                lbl.grid(row=0, column=0, padx=10, pady=(2,0))
                entryTimer = Entry(lblFrameTimer, justify=CENTER)
                entryTimer.insert (0, self.settings_timer.get())
                entryTimer.grid(row=1, column=0, padx=10, pady=10)

                # Apply settings
                lbl = Label(settingsFrame, text="NB: 0 <=> Unlimited")
                lbl.pack(pady=3)
                applyBtn = Button(settingsFrame, text="Apply", command=lambda: self.set_settings(entryTryCount.get(), entryTimer.get(), settingsFrame))
                applyBtn.pack(side = LEFT, expand=True, pady=(0,5))
                cancelBtn = Button(settingsFrame, text="Cancel", command=settingsFrame.destroy)
                cancelBtn.pack(side = RIGHT, expand=True, pady=(0,5))
                
                # Show dialog

                settingsFrame.transient(self.root)
                settingsFrame.parent = self.root
                settingsFrame.protocol("WM_DELETE_WINDOW", settingsFrame.destroy)
                settingsFrame.geometry("+{0}+{1}".format(self.root.winfo_rootx(), self.root.winfo_rooty()))
                settingsFrame.title("Settings")
                settingsFrame.focus_set()
                settingsFrame.grab_set()
                settingsFrame.mainloop()

        def set_settings(self, tryCount, timer, frame):

                """
                        Set new settings.
		
                        :param self:            (self)
                        :param tryCount:        Number of try
                        :param timer:           Number of Second
                        :param frame:           Dialog to close

		        :type tryCount:		int
		        :type timer:		int
		        :type frame:		tkinter dialog
		
                        :return:                (null)
                """
                
                try:
                        # Check entries format
                        # Only numeric format is accepted
                        tryCount = int(tryCount)
                        timer = int(timer)
                        if tryCount >= 0 and timer >= 0:
                                self.settings_try_count.set(tryCount)
                                self.settings_timer.set(timer)
                                messagebox.showinfo("Settings message", "Changes have been applied")
                                frame.destroy()
                        else:
                                messagebox.showerror("Value error", "Cannot use negative numbers")
                except ValueError:
                        messagebox.showerror("Value error", "Entries are only in numeric format")
                except Exception as e:
                        msgError = "An error occured\n" + str(e)
                        messagebox.showerror("Global error", msgError)
                        
        def start_game(self, lblTryCount, lblTimer):
                
                """
                        Start game.
		
                        :param self:            (self)
                        :param lblTryCount:     Try count label
                        :param lblTimer:        Timer label

		        :type tryCount:		tkinter label
		        :type timer:		tkinter label
		
                        :return:                (null)
                """

                # Set variables
                self.game_started.set(True)
                
                self.game_range_min.set(self.levels[self.level.get()]["min"])
                self.game_range_max.set(self.levels[self.level.get()]["max"])
                self.game_try_count.set(self.settings_try_count.get())
                self.game_timer.set(self.settings_timer.get())
                
                self.secret_number = IntVar()
                #  Generate random secret number
                self.secret_number.set(randint(self.levels[self.level.get()]["min"], self.levels[self.level.get()]["max"]))

                # Try count status
                self.game_try_count_status = StringVar()
                if self.game_try_count.get() > 0:
                        self.game_try_count_status.set(True)
                        lblTryCount.configure(bg="yellow", fg="blue")
                else:
                        self.game_try_count_status.set(False)
                        lblTryCount.configure(bg="black", fg="black")

                # Timer status
                self.game_timer_status = StringVar()
                if self.game_timer.get() > 0:
                        self.game_timer_status.set(True)
                        lblTimer.configure(bg="yellow", fg="blue")
                        timer = Timer(1.0, self.timer_mode).start()
                else:
                        self.game_timer_status.set(False)
                        lblTimer.configure(bg="black", fg="black")

                # Level name
                self.show_result.set("Game started\n"  + self.levels[self.level.get()]["title"])

                # Cheat mod
                if self.cheat_mode.get() :
                        self.entry_number.set(self.secret_number.get())
                        messagebox.showwarning("Cheat mod actived", "Entry is already the secret number")
                else:
                        self.entry_number.set("")              

        def submit_number(self):
                
                """
                        Submit a number to test.
		
                        :param self:            (self)
		
                        :return:                (null)
                """

                if self.game_started.get():
                        entry_verified = bool(False)
                        try:
                                entry = int(self.entry_number.get())
                                entry_verified = True
                        except ValueError:
                                self.show_result.set("Please, enter number")
                                
                        if entry_verified:
                                if entry in range(self.game_range_min.get(), self.game_range_max.get() + 1):
                                        if entry < self.secret_number.get():
                                                self.show_result.set("More than " + str(entry))
                                                if entry > self.game_range_min.get():
                                                    self.game_range_min.set(entry)
                                        elif entry > self.secret_number.get():
                                                self.show_result.set("Less than " + str(entry))
                                                if entry < self.game_range_max.get():
                                                    self.game_range_max.set(entry)
                                        else:
                                                self.game_range_min.set(entry)
                                                self.game_range_max.set(entry)
                                                self.game_started.set(False)
                                                messagebox.showinfo("You win :D", "Congratulation, you found the secret number :\n" + str(self.secret_number.get()))
                                else:
                                        self.show_result.set("Number out of range...")
                                        
                                # Try count limited
                                if self.game_try_count_status:
                                        self.game_try_count.set(self.game_try_count.get() - 1)
                                        if self.game_try_count.get() == 0 and self.game_started.get():
                                                self.game_started.set(False)
                                                messagebox.showinfo("You loose :'(", "It was your last try...\nSecret number was " + str(self.secret_number.get()))
                                if not self.game_started.get():
                                        self.show_result.set("Game ended")
                                        
                        # Clear entry
                        self.entry_number.set("")
                else:
                        messagebox.showwarning("Warning", "Game is not running")

        def timer_mode(self):
                
                """
                        Start timer.
		
                        :param self:            (self)
		
                        :return:                (null)
                """

                self.game_timer.set(self.game_timer.get() - 1)
                if self.game_timer.get() == 0:
                        self.game_started.set(False)
                        messagebox.showwarning("You loose :'(", "You're out of time\nSecret number was " + str(self.secret_number.get()))
                        self.show_result.set("Game ended")
                elif self.game_started.get():
                        timer = Timer(1.0, self.timer_mode)
                        timer.start()
                    
if __name__ == '__main__':
        game = Dichoplay()
        mainloop()
