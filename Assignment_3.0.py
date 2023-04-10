from tkinter import *
import tkinter as tkinter
from playsound import playsound
import csv
from collections import defaultdict
from time import *
import os
import winsound
from random import randint
import turtle
global player1_name, player2_name, current_player


class War_Game:
    def __init__(self):
        self.graph = defaultdict(list)

    def Interface(self):
        global player1, player2, turns,player1_name, player2_name, current_player
        self.GuiWindow = tkinter.Tk()
        self.GuiWindow.title("War Game v1.0")
        self.GuiWindow.geometry("1920x1080")
        self.GuiWindow.state('zoomed')
        photoImages = tkinter.PhotoImage(file="images\D.png", master=self.GuiWindow)
        BgImages = tkinter.Label(self.GuiWindow, image=photoImages)
        self.klara_logo = tkinter.PhotoImage(file="images\klara.png", master=self.GuiWindow)
        self.user_logo = tkinter.PhotoImage(file="images/user.png", master=self.GuiWindow)
        #LABEL_A
        self.klara_A = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                      font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")

        self.user_A = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                    font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
        # LABEL_B
        self.klara_B = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                     font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
        self.user_B = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                    font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
        # LABEL_C
        self.klara_C = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                     font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
        #self.klara_C.place(relx="0.625", rely="0.290")

        self.user_C = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                   font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")

        # LABEL_E
        self.klara_E = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                     font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
        #self.klara_E.place(relx="0.225", rely="0.490")

        self.user_E = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                    font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
        #self.user_E.place(relx="0.225", rely="0.490")
        # LABEL_F
        self.klara_F = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                     font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
        #self.klara_F.place(relx="0.425", rely="0.490")

        self.user_F = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                    font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
        #self.user_F.place(relx="0.425", rely="0.490")
        # LABEL_G
        self.klara_G = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                     font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
        #self.klara_G.place(relx="0.625", rely="0.490")

        self.user_G = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                    font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
        #self.user_G.place(relx="0.625", rely="0.490")
        # LABEL_I
        self.klara_I = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                     font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")

        self.user_I = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                    font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
        # LABEL_J
        self.klara_J = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                     font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")

        self.user_J = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                    font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
        # LABEL_K
        self.klara_K = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                     font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")

        self.user_K = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                    font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
        #if turns % 2 != 0:
            #current_player=player1_name
        #else:
            #current_player = player2_name turn
        self.current_player_v = StringVar()
        self.current_player_v.set(player1_name+"'s move")
        self.turnsNo = tkinter.Label(self.GuiWindow, textvariable=self.current_player_v, text=current_player+"'s turn",
                                     bg="black", fg="#227EB9",font=("Agency FB bold", 20), width="16", borderwidth="0")
        self.interface_text = tkinter.Label(self.GuiWindow, text="", bg="black", fg="#227EB9",
                                   font=("Agency FB bold", 19), width="20", borderwidth="0")
        self.interface_text.place(relx="0.675", rely="0.920")
        self.turnsNo.place(relx="0.260", rely="0.150")

        self.score_p1 = StringVar()
        self.score_p2 = StringVar()
        self.score_p1.set(player1_name+": "+str(player1))
        self.score_p2.set(player2_name+": "+str(player2))
        #Score Player1
        self.score_p1_label = tkinter.Label(self.GuiWindow, textvariable=self.score_p1,
                                     text="" ,
                                     bg="black", fg="#227EB9", font=("Agency FB bold", 20), width="16", borderwidth="0")
        self.score_p1_label.place(relx="0.650", rely="0.110")
        #Score AI/Player 2
        self.score_p2_label = tkinter.Label(self.GuiWindow, textvariable=self.score_p2,
                                     text="",
                                     bg="black", fg="#227EB9", font=("Agency FB bold", 20), width="16", borderwidth="0")
        self.score_p2_label.place(relx="0.650", rely="0.150")

        # Vertex A
        vertexA = tkinter.Label(self.GuiWindow, text="A", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexA.place(relx="0.145", rely="0.220")
        vertexA.bind("<Enter>", lambda event: self.hover_text_on(event, "A"))
        vertexA.bind("<Leave>", self.hover_text_off)
        # Vertex B
        vertexB = tkinter.Label(self.GuiWindow, text="B", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexB.place(relx="0.345", rely="0.220")
        vertexB.bind("<Enter>", lambda event: self.hover_text_on(event, "B"))
        vertexB.bind("<Leave>", self.hover_text_off)
        # Vertex C
        vertexC = tkinter.Label(self.GuiWindow, text="C", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexC.place(relx="0.545", rely="0.220")
        vertexC.bind("<Enter>", lambda event: self.hover_text_on(event, "C"))
        vertexC.bind("<Leave>", self.hover_text_off)
        # Vertex D
        vertexD = tkinter.Label(self.GuiWindow, text="D", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexD.place(relx="0.745", rely="0.220")
        vertexD.bind("<Enter>", lambda event: self.hover_text_on(event, "D"))
        vertexD.bind("<Leave>", self.hover_text_off)
        # Vertex E
        vertexE = tkinter.Label(self.GuiWindow, text="E", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexE.place(relx="0.145", rely="0.420")
        vertexE.bind("<Enter>", lambda event: self.hover_text_on(event, "E"))
        vertexE.bind("<Leave>", self.hover_text_off)
        # Vertex F
        vertexF = tkinter.Label(self.GuiWindow, text="F", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexF.place(relx="0.345", rely="0.420")
        vertexF.bind("<Enter>", lambda event: self.hover_text_on(event, "F"))
        vertexF.bind("<Leave>", self.hover_text_off)
        # Vertex G
        vertexG = tkinter.Label(self.GuiWindow, text="G", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexG.place(relx="0.545", rely="0.420")
        vertexG.bind("<Enter>", lambda event: self.hover_text_on(event, "G"))
        vertexG.bind("<Leave>", self.hover_text_off)
        # Vertex H
        vertexH = tkinter.Label(self.GuiWindow, text="H", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexH.place(relx="0.745", rely="0.420")
        vertexH.bind("<Enter>", lambda event: self.hover_text_on(event, "H"))
        vertexH.bind("<Leave>", self.hover_text_off)
        # Vertex I
        vertexI = tkinter.Label(self.GuiWindow, text="I", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexI.place(relx="0.145", rely="0.620")
        vertexI.bind("<Enter>", lambda event: self.hover_text_on(event, "I"))
        vertexI.bind("<Leave>", self.hover_text_off)
        # Vertex J
        vertexJ = tkinter.Label(self.GuiWindow, text="J", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexJ.place(relx="0.345", rely="0.620")
        vertexJ.bind("<Enter>", lambda event: self.hover_text_on(event, "J"))
        vertexJ.bind("<Leave>", self.hover_text_off)
        # Vertex K
        vertexK = tkinter.Label(self.GuiWindow, text="K", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexK.place(relx="0.545", rely="0.620")
        vertexK.bind("<Enter>", lambda event: self.hover_text_on(event, "K"))
        vertexK.bind("<Leave>", self.hover_text_off)
        # Vertex L
        vertexL = tkinter.Label(self.GuiWindow, text="L", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexL.place(relx="0.745", rely="0.620")
        vertexL.bind("<Enter>", lambda event: self.hover_text_on(event, "L"))
        vertexL.bind("<Leave>", self.hover_text_off)
        # Vertex M
        vertexM = tkinter.Label(self.GuiWindow, text="M", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexM.place(relx="0.145", rely="0.820")
        vertexM.bind("<Enter>", lambda event: self.hover_text_on(event, "M"))
        vertexM.bind("<Leave>", self.hover_text_off)
        # Vertex N
        vertexN = tkinter.Label(self.GuiWindow, text="N", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexN.place(relx="0.345", rely="0.820")
        vertexN.bind("<Enter>", lambda event: self.hover_text_on(event, "N"))
        vertexN.bind("<Leave>", self.hover_text_off)
        # Vertex O
        vertexO = tkinter.Label(self.GuiWindow, text="O", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexO.place(relx="0.545", rely="0.820")
        vertexO.bind("<Enter>", lambda event: self.hover_text_on(event, "O"))
        vertexO.bind("<Leave>", self.hover_text_off)
        # Vertex P
        vertexP = tkinter.Label(self.GuiWindow, text="P", bg="#B33838", fg="white",
                                font=("Agency FB bold", 20), width="13", borderwidth="0")
        vertexP.place(relx="0.745", rely="0.820")
        vertexP.bind("<Enter>", lambda event: self.hover_text_on(event, "P"))
        vertexP.bind("<Leave>", self.hover_text_off)

        # Button_AB
        self.Button_AB = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("A", "B", "array1", 0))
        self.Button_AB.place(relx="0.213", rely="0.230")
        self.Button_AB.bind("<Enter>", lambda event: self.hover_prompt_on(event, "A", "B"))
        self.Button_AB.bind("<Leave>", self.hover_text_off)
        #Displaying A-B edge
        self.Connection_AB = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_AE
        self.Button_AE = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("A", "E", "array1", 1))
        self.Button_AE.place(relx="0.175", rely="0.258")
        self.Button_AE.bind("<Enter>", lambda event: self.hover_prompt_on(event, "A", "E"))
        self.Button_AE.bind("<Leave>", self.hover_text_off)
        # Displaying A-E edge
        self.Connection_AE = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_EF
        self.Button_EF = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("E", "F", "array1", 2))
        self.Button_EF.place(relx="0.213", rely="0.430")
        self.Button_EF.bind("<Enter>", lambda event: self.hover_prompt_on(event, "E", "F"))
        self.Button_EF.bind("<Leave>", self.hover_text_off)
        # Displaying E-F edge
        self.Connection_EF = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_BF
        self.Button_BF = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("B", "F", "array1", 3))
        self.Button_BF.place(relx="0.375", rely="0.258")
        self.Button_BF.bind("<Enter>", lambda event: self.hover_prompt_on(event, "B", "F"))
        self.Button_BF.bind("<Leave>", self.hover_text_off)
        # Displaying B-F edge
        self.Connection_BF = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                          font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_BC
        self.Button_BC = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("B", "C", "array1", 4))
        self.Button_BC.place(relx="0.413", rely="0.230")
        self.Button_BC.bind("<Enter>", lambda event: self.hover_prompt_on(event, "B", "C"))
        self.Button_BC.bind("<Leave>", self.hover_text_off)
        # Displaying B-C edge
        self.Connection_BC = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_FG
        self.Button_FG = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("F", "G", "array1", 5))
        self.Button_FG.place(relx="0.413", rely="0.430")
        self.Button_FG.bind("<Enter>", lambda event: self.hover_prompt_on(event, "F", "G"))
        self.Button_FG.bind("<Leave>", self.hover_text_off)
        # Displaying F-G edge
        self.Connection_FG = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_CG
        self.Button_CG = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("C", "G", "array1", 6))
        self.Button_CG.place(relx="0.575", rely="0.258")
        self.Button_CG.bind("<Enter>", lambda event: self.hover_prompt_on(event, "C", "G"))
        self.Button_CG.bind("<Leave>", self.hover_text_off)
        # Displaying C-G edge
        self.Connection_CG = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_CD
        self.Button_CD = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("C", "D", "array1", 7))
        self.Button_CD.place(relx="0.613", rely="0.230")
        self.Button_CD.bind("<Enter>", lambda event: self.hover_prompt_on(event, "C", "D"))
        self.Button_CD.bind("<Leave>", self.hover_text_off)
        # Displaying C-D edge
        self.Connection_CD = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_GH
        self.Button_GH = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("G", "H", "array1", 8))
        self.Button_GH.place(relx="0.613", rely="0.430")
        self.Button_GH.bind("<Enter>", lambda event: self.hover_prompt_on(event, "G", "H"))
        self.Button_GH.bind("<Leave>", self.hover_text_off)
        # Displaying G-H edge
        self.Connection_GH = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_DH
        self.Button_DH = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("D", "H", "array1", 9))
        self.Button_DH.place(relx="0.775", rely="0.258")
        self.Button_DH.bind("<Enter>", lambda event: self.hover_prompt_on(event, "D", "H"))
        self.Button_DH.bind("<Leave>", self.hover_text_off)
        # Displaying D-H edge
        self.Connection_DH = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")

        # Button_EI
        self.Button_EI = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("E", "I", "array2", 0))
        self.Button_EI.place(relx="0.175", rely="0.457")
        self.Button_EI.bind("<Enter>", lambda event: self.hover_prompt_on(event, "E", "I"))
        self.Button_EI.bind("<Leave>", self.hover_text_off)
        # Displaying E-I edge
        self.Connection_EI = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_IJ
        self.Button_IJ = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("I", "J", "array2", 1))
        self.Button_IJ.place(relx="0.213", rely="0.630")
        self.Button_IJ.bind("<Enter>", lambda event: self.hover_prompt_on(event, "I", "J"))
        self.Button_IJ.bind("<Leave>", self.hover_text_off)
        # Displaying I-J edge
        self.Connection_IJ = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_FJ
        self.Button_FJ = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("F", "J", "array2", 2))
        self.Button_FJ.place(relx="0.375", rely="0.457")
        self.Button_FJ.bind("<Enter>", lambda event: self.hover_prompt_on(event, "F", "J"))
        self.Button_FJ.bind("<Leave>", self.hover_text_off)
        # Displaying F-J edge
        self.Connection_FJ = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_JK
        self.Button_JK = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("J", "K", "array2", 3))
        self.Button_JK.place(relx="0.413", rely="0.630")
        self.Button_JK.bind("<Enter>", lambda event: self.hover_prompt_on(event, "J", "K"))
        self.Button_JK.bind("<Leave>", self.hover_text_off)
        # Displaying J-K edge
        self.Connection_JK = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_GK
        self.Button_GK = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("G", "K", "array2", 4))
        self.Button_GK.place(relx="0.575", rely="0.457")
        self.Button_GK.bind("<Enter>", lambda event: self.hover_prompt_on(event, "G", "K"))
        self.Button_GK.bind("<Leave>", self.hover_text_off)
        # Displaying G-K edge
        self.Connection_GK = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_KL
        self.Button_KL = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("K", "L", "array2", 5))
        self.Button_KL.place(relx="0.613", rely="0.630")
        self.Button_KL.bind("<Enter>", lambda event: self.hover_prompt_on(event, "K", "L"))
        self.Button_KL.bind("<Leave>", self.hover_text_off)
        # Displaying K-L edge
        self.Connection_KL = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        #Button_HL
        self.Button_HL = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("H", "L", "array2", 6))
        self.Button_HL.place(relx="0.775", rely="0.457")
        self.Button_HL.bind("<Enter>", lambda event: self.hover_prompt_on(event, "H", "L"))
        self.Button_HL.bind("<Leave>", self.hover_text_off)
        # Displaying H-L edge
        self.Connection_HL = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")

        # Button_IM
        self.Button_IM = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("I", "M", "array3", 0))
        self.Button_IM.place(relx="0.175", rely="0.657")
        self.Button_IM.bind("<Enter>", lambda event: self.hover_prompt_on(event, "I", "M"))
        self.Button_IM.bind("<Leave>", self.hover_text_off)
        # Displaying I-M edge
        self.Connection_IM = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_MN
        self.Button_MN = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("M", "N", "array3", 1))
        self.Button_MN.place(relx="0.213", rely="0.834")
        self.Button_MN.bind("<Enter>", lambda event: self.hover_prompt_on(event, "M", "N"))
        self.Button_MN.bind("<Leave>", self.hover_text_off)
        # Displaying M-N edge
        self.Connection_MN = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_JN
        self.Button_JN = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("J", "N", "array3", 2))
        self.Button_JN.place(relx="0.375", rely="0.657")
        self.Button_JN.bind("<Enter>", lambda event: self.hover_prompt_on(event, "J", "N"))
        self.Button_JN.bind("<Leave>", self.hover_text_off)
        # Displaying J-N edge
        self.Connection_JN = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_NO
        self.Button_NO = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("N", "O", "array3", 3))
        self.Button_NO.place(relx="0.413", rely="0.834")
        self.Button_NO.bind("<Enter>", lambda event: self.hover_prompt_on(event, "N", "O"))
        self.Button_NO.bind("<Leave>", self.hover_text_off)
        # Displaying N-O edge
        self.Connection_NO = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_KO
        self.Button_KO = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("K", "O", "array3", 4))
        self.Button_KO.place(relx="0.575", rely="0.657")
        self.Button_KO.bind("<Enter>", lambda event: self.hover_prompt_on(event, "K", "O"))
        self.Button_KO.bind("<Leave>", self.hover_text_off)
        # Displaying K-O edge
        self.Connection_KO = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        # Button_OP
        self.Button_OP = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="82", height="1", borderwidth="0",
                                   command=lambda: self.addEdge("O", "P", "array3", 5))
        self.Button_OP.place(relx="0.613", rely="0.834")
        self.Button_OP.bind("<Enter>", lambda event: self.hover_prompt_on(event, "O", "P"))
        self.Button_OP.bind("<Leave>", self.hover_text_off)
        # Displaying O-P edge
        self.Connection_OP = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="85", height="1", borderwidth="0")
        # Button_LP
        self.Button_LP = tkinter.Button(self.GuiWindow, text="", bg="#227EB9", fg="white", cursor="hand2",
                                   font=("Agency FB bold", 5), width="2", height="20", borderwidth="0",
                                   command=lambda: self.addEdge("L", "P", "array3", 6))
        self.Button_LP.place(relx="0.775", rely="0.657")
        self.Button_LP.bind("<Enter>", lambda event: self.hover_prompt_on(event, "L", "P"))
        self.Button_LP.bind("<Leave>", self.hover_text_off)
        # Displaying L-P edge
        self.Connection_LP = tkinter.Label(self.GuiWindow, text="", bg="#B33838", fg="white",
                                      font=("Agency FB bold", 5), width="3", height="22", borderwidth="0")
        BgImages.pack()
        self.GuiWindow.mainloop()

    def hover_text_on(self, event, string):
        self.interface_text.configure(text="Vertex " + str(string))
        winsound.PlaySound("Sounds/Clicks/Hover.wav", winsound.SND_ASYNC)

    def hover_prompt_on(self, event, v1, v2):
        self.interface_text.configure(text="Connect " + str(v1) +" and " + str(v2))

    def hover_text_off(self, event):
        self.interface_text.configure(text="")

    def reveal_graph_array1(self, arrayNum):
        global turns, freeMove
        #turns += 1
        self.checkScore()
        print("turn is " + str(turns))
        if turns % 2 != 0:
            print(player1_name+"'s move")
            self.current_player_v.set(player1_name+"'s move")
        else:
            print(player2_name+"'s turn")
            self.current_player_v.set(player2_name+"'s move")
            sleep(1)
            self.find_fitness_values()
        self.turnsNo.place(relx="0.260", rely="0.150")
        #if freeMove == 1:
            #turns -= 1
            #freeMove = 0
        if array1[arrayNum] == 1 and arrayNum == 0:
            self.Button_AB.destroy()
            self.Connection_AB.place(relx="0.214", rely="0.230")
        elif array1[arrayNum] == 1 and arrayNum == 1:
            self.Button_AE.destroy()
            self.Connection_AE.place(relx="0.175", rely="0.252")
        elif array1[arrayNum] == 1 and arrayNum == 2:
            self.Button_EF.destroy()
            self.Connection_EF.place(relx="0.214", rely="0.430")
        elif array1[arrayNum] == 1 and arrayNum == 3:
            self.Button_BF.destroy()
            self.Connection_BF.place(relx="0.375", rely="0.252")
        elif array1[arrayNum] == 1 and arrayNum == 4:
            self.Button_BC.destroy()
            self.Connection_BC.place(relx="0.414", rely="0.230")
        elif array1[arrayNum] == 1 and arrayNum == 5:
            self.Button_FG.destroy()
            self.Connection_FG.place(relx="0.414", rely="0.430")
        elif array1[arrayNum] == 1 and arrayNum == 6:
            self.Button_CG.destroy()
            self.Connection_CG.place(relx="0.575", rely="0.252")
        elif array1[arrayNum] == 1 and arrayNum == 7:
            self.Button_CD.destroy()
            self.Connection_CD.place(relx="0.614", rely="0.230")
        elif array1[arrayNum] == 1 and arrayNum == 8:
            self.Button_GH.destroy()
            self.Connection_GH.place(relx="0.614", rely="0.430")
        elif array1[arrayNum] == 1 and arrayNum == 9:
            self.Button_DH.destroy()
            self.Connection_DH.place(relx="0.775", rely="0.252")

    def reveal_graph_array2(self, arrayNum):
        global turns, freeMove
        #turns += 1
        self.checkScore()
        print("turn is " + str(turns))
        if turns % 2 != 0:
            print(player1_name + "'s move")
            self.current_player_v.set(player1_name+"'s move")
        else:
            print(player2_name + "'s move")
            self.current_player_v.set(player2_name+"'s move")
            sleep(1)
            self.find_fitness_values()
        self.turnsNo.place(relx="0.260", rely="0.150")
        if array2[arrayNum] == 1 and arrayNum == 0:
            self.Button_EI.destroy()
            self.Connection_EI.place(relx="0.175", rely="0.452")
        elif array2[arrayNum] == 1 and arrayNum == 1:
            self.Button_IJ.destroy()
            self.Connection_IJ.place(relx="0.214", rely="0.630")
        elif array2[arrayNum] == 1 and arrayNum == 2:
            self.Button_FJ.destroy()
            self.Connection_FJ.place(relx="0.375", rely="0.452")
        elif array2[arrayNum] == 1 and arrayNum == 3:
            self.Button_JK.destroy()
            self.Connection_JK.place(relx="0.414", rely="0.630")
        elif array2[arrayNum] == 1 and arrayNum == 4:
            self.Button_GK.destroy()
            self.Connection_GK.place(relx="0.575", rely="0.452")
        elif array2[arrayNum] == 1 and arrayNum == 5:
            self.Button_KL.destroy()
            self.Connection_KL.place(relx="0.614", rely="0.630")
        elif array2[arrayNum] == 1 and arrayNum == 6:
            self.Button_HL.destroy()
            self.Connection_HL.place(relx="0.775", rely="0.452")

    def reveal_graph_array3(self, arrayNum):
        global turns, freeMove
        self.checkScore()
        print("turn is " + str(turns))
        if turns % 2 != 0:
            print(player1_name + "'s move")
            self.current_player_v.set(player1_name+"'s move")
        else:
            print(player2_name + "'s move")
            self.current_player_v.set(player2_name+"'s move")
            sleep(1)
            self.find_fitness_values()
        self.turnsNo.place(relx="0.260", rely="0.150")
        if array3[arrayNum] == 1 and arrayNum == 0:
            self.Button_IM.destroy()
            self.Connection_IM.place(relx="0.175", rely="0.652")
        elif array3[arrayNum] == 1 and arrayNum == 1:
            self.Button_MN.destroy()
            self.Connection_MN.place(relx="0.214", rely="0.830")
        elif array3[arrayNum] == 1 and arrayNum == 2:
            self.Button_JN.destroy()
            self.Connection_JN.place(relx="0.375", rely="0.652")
        elif array3[arrayNum] == 1 and arrayNum == 3:
            self.Button_NO.destroy()
            self.Connection_NO.place(relx="0.414", rely="0.830")
        elif array3[arrayNum] == 1 and arrayNum == 4:
            self.Button_KO.destroy()
            self.Connection_KO.place(relx="0.575", rely="0.652")
        elif array3[arrayNum] == 1 and arrayNum == 5:
            self.Button_OP.destroy()
            self.Connection_OP.place(relx="0.614", rely="0.830")
        elif array3[arrayNum] == 1 and arrayNum == 6:
            self.Button_LP.destroy()
            self.Connection_LP.place(relx="0.775", rely="0.652")

    def addEdge(self, vertex1, vertex2, arrayID, arrayNum):
        global recent_edge
        recent_edge=vertex1
        winsound.PlaySound("Sounds/Clicks/BtnClick1.wav", winsound.SND_ASYNC)
        #UndirectedGraph
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
        print(vertex1+" added to "+vertex2)
        if arrayID == "array1":
            array1[arrayNum] = 1
            self.reveal_graph_array1(arrayNum)
        elif arrayID == "array2":
            array2[arrayNum] = 1
            self.reveal_graph_array2(arrayNum)
        elif arrayID == "array3":
            array3[arrayNum] = 1
            self.reveal_graph_array3(arrayNum)

    def check_edge(self, vertex1, vertex2):
        for elements in self.graph[vertex1]:
            if elements == vertex2:
                #print(vertex2 + " found in " + vertex1)
                return 1
        return 0

    def checkScore(self):
        global turns, turn_saver, player1, player2
        self.score_p1.set("Player 1: "+str(player1))
        self.score_p2.set("Klara (AI): "+str(player2))
        self.score_p1_label.place(relx="0.650", rely="0.110")
        self.score_p2_label.place(relx="0.650", rely="0.150")
        turn_saver = 0
        arrayMapping = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"
            , "", "", "", "", "", ""]
        global recent_edge
        i = 0                   #used for searching element in arrays
        alphabets = 0           #while loop condition checking flag
        sumTiles = 0            #determines the total number of tiles
        while alphabets != 16:  #parent = arrayMapping[i] & will keep traversing untill all alphabets are secured
            alphabets += 1
            step = 1
            global e1, e2, e3, e4
            e1 = 0; e2 = 0; e3 = 0; e4 = 0
            while step != 4:

                if step == 1:
                    e1 = self.check_edge(arrayMapping[i], arrayMapping[i+1]) #Vertex Pattern Detection Algorithm
                    e2 = self.check_edge(arrayMapping[i], arrayMapping[i+4]) #Vertex Pattern Detection Algorithm

                elif step == 2:
                    e3 = self.check_edge(arrayMapping[i+1], arrayMapping[i+5]) #Mathmetical Formulation : (i+1)+4= i+5

                elif step == 3:
                    e4 = self.check_edge(arrayMapping[i+4], arrayMapping[i+5]) #Mathmetical Formulation : (i+4)+1= i+5

                if e1 == 1 and e2 == 1 and e3 == 1 and e4 == 1:
                    sumTiles += 1
                    print(recent_edge+"-"+arrayMapping[i])
                    self.scoringSystem(arrayMapping[i])
                    #self.checkRecentEdge(arrayMapping[i])
                    print("sumTiles " + str(sumTiles))

                if sumTiles == 9:
                    self.endgame_screen()
                    exit()
                step += 1
            i += 1
        turns += 1

    def scoringSystem(self, i):
        global tileScored,relx, rely
        if i == "A" and tileScored[0] == 0:
            tileScored[0] = 1
            relx="0.245"
            rely="0.290"
            self.playerPoints()
        elif i == "B" and tileScored[1] == 0:
            tileScored[1] = 1
            relx = "0.445"
            rely = "0.290"
            self.playerPoints()
        elif i == "C" and tileScored[2] == 0:
            tileScored[2] = 1
            relx = "0.645"
            rely = "0.290"
            self.playerPoints()
        elif i == "E" and tileScored[3] == 0:
            tileScored[3] = 1
            relx = "0.245"
            rely = "0.490"
            self.playerPoints()
        elif i == "F" and tileScored[4] == 0:
            tileScored[4] = 1
            relx = "0.445"
            rely = "0.490"
            self.playerPoints()
        elif i == "G" and tileScored[5] == 0:
            tileScored[5] = 1
            relx = "0.645"
            rely = "0.490"
            self.playerPoints()
        elif i == "I" and tileScored[6] == 0:
            tileScored[6] = 1
            relx = "0.245"
            rely = "0.690"
            self.playerPoints()
        elif i == "J" and tileScored[7] == 0:
            tileScored[7] = 1
            relx = "0.445"
            rely = "0.690"
            self.playerPoints()
        elif i == "K" and tileScored[8] == 0:
            tileScored[8] = 1
            relx = "0.645"
            rely = "0.690"
            self.playerPoints()

    def playerPoints(self):
        global turns, player1, player2, freeMove, relx, rely, numbers_user, numbers_ai, repeater, turn_saver
        turn_saver += 1
        if turn_saver == 2:
            turns += 1
        if turns % 2 != 0:
            player1 += 1
            print("P1 Awarded " + str(player1))
            self.score_p1.set("Player 1: "+str(player1))
            self.score_p2.set("Klara (AI): "+str(player2))
            self.score_p1_label.place(relx="0.650", rely="0.110")
            self.score_p2_label.place(relx="0.650", rely="0.150")
            self.user_A.place(relx=relx, rely=rely)
            if numbers_user == 1:
                self.user_1 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_1.place(relx=relx, rely=rely)
            if numbers_user == 2:
                self.user_2 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_2.place(relx=relx, rely=rely)
            if numbers_user == 3:
                self.user_3 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_3.place(relx=relx, rely=rely)
            if numbers_user == 4:
                self.user_4 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_4.place(relx=relx, rely=rely)
            if numbers_user == 5:
                self.user_5 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_5.place(relx=relx, rely=rely)
            if numbers_user ==6:
                self.user_6 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_6.place(relx=relx, rely=rely)
            if numbers_user == 7:
                self.user_7 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_7.place(relx=relx, rely=rely)
            if numbers_user == 8:
                self.user_8 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_8.place(relx=relx, rely=rely)
            if numbers_user == 9:
                self.user_9 = tkinter.Label(self.GuiWindow, image=self.user_logo, bg="#227EB9", fg="white",
                                            font=("Agency FB bold", 20), width="120", height="80", borderwidth="0")
                self.user_9.place(relx=relx, rely=rely)
            numbers_user += 1
            turns -= 1
            #freeMove = 1
        else:
            player2 += 1
            print("P2 Awarded " + str(player2))
            self.score_p1.set("Player 1: "+str(player1))
            self.score_p2.set("Klara (AI): "+str(player2))
            self.score_p1_label.place(relx="0.650", rely="0.110")
            self.score_p2_label.place(relx="0.650", rely="0.150")
            #self.klara_A.place(relx=relx, rely=rely)
            if numbers_ai == 1:
                self.klara_1 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_1.place(relx=relx, rely=rely)
            if numbers_ai ==2:
                self.klara_2 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_2.place(relx=relx, rely=rely)
            if numbers_ai == 3:
                self.klara_3 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_3.place(relx=relx, rely=rely)
            if numbers_ai == 4:
                self.klara_4 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_4.place(relx=relx, rely=rely)
            if numbers_ai == 5:
                self.klara_5 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_5.place(relx=relx, rely=rely)
            if numbers_ai ==6:
                self.klara_6 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_6.place(relx=relx, rely=rely)
            if numbers_ai == 7:
                self.klara_7 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_7.place(relx=relx, rely=rely)
            if numbers_ai == 8:
                self.klara_8 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_8.place(relx=relx, rely=rely)
            if numbers_ai == 9:
                self.klara_9 = tkinter.Label(self.GuiWindow, image=self.klara_logo, bg="#227EB9", fg="white",
                                             font=("Agency FB bold", 20), width="140", height="85", borderwidth="0")
                self.klara_9.place(relx=relx, rely=rely)
            numbers_ai += 1
            turns -= 1
            #freeMove = 1

#AI PART
    def set_crossover_values(self, vertice, probability):
        global crossover_array
        target_vertice = vertice
        elements = 0
        while elements != len(crossover_array):
            if target_vertice == crossover_array[elements]:
                if crossover_array[elements+1] == 0.8:
                    break;
                elif crossover_array[elements+1] == 0.2:
                    if probability == 0.8:
                        crossover_array[elements + 1] = probability
                    else:
                        break
                else:
                    crossover_array[elements + 1] = probability
            elements += 1


    def find_fitness_values(self):
        global crossover_array
        vertex_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"
            , "", "", "", "", "", ""]

        fitness_array = ["A", 1, "B", 1, "C", 1, "E", 1, "F", 1, "G", 1, "I", 1, "J",  1, "K", 1, "", 0, "", 0, "", 0]

        crossover_array = ["AB", 0, "AE", 0, "BF", 0, "EF", 0, "BC", 0, "CG", 0, "FG", 0, "CD", 0, "DH", 0, "GH", 0, "EI", 0, "FJ", 0,
                           "IJ", 0, "GK", 0, "JK", 0, "HL", 0, "KL", 0, "IM", 0, "JN", 0, "MN", 0, "KO", 0, "NO", 0, "LP", 0, "OP", 0,]
        traverse_point = 0
        skip_traverse_point = 0  # to make sure it skips @ 3, 7, 11 & 15, # pattern - each point are seperated by 4
        fitness_index = 0
        crossover_index = 0
        all_parents = 0
        queue = []
        while all_parents != 9:  # it will now traverse through parent zone
            parent = vertex_list[traverse_point]
            print(str(parent) + " is the new parent -->")
            steps = 1
            available_moves = 4
            edge1 = ""
            edge2 = ""
            edge3 = ""
            edge4 = ""
            while steps != 4:
                if steps == 1:
                    b1 = self.check_edge(vertex_list[traverse_point], vertex_list[traverse_point + 1])
                    b2 = self.check_edge(vertex_list[traverse_point], vertex_list[traverse_point + 4])
                    if b1 == 1:
                        available_moves -= 1
                    else:
                        edge1 = vertex_list[traverse_point] + vertex_list[traverse_point + 1]
                    print(edge1)

                    if b2 == 1:
                        available_moves -= 1
                    else:
                        edge2 = vertex_list[traverse_point] + vertex_list[traverse_point + 4]
                    print(edge2)

                elif steps == 2:
                    b3 = self.check_edge(vertex_list[traverse_point + 1], vertex_list[traverse_point + 5])
                    if b3 == 1:
                        available_moves -= 1
                    else:
                        edge3 = vertex_list[traverse_point + 1] + vertex_list[traverse_point + 5]
                    print(edge3)

                elif steps == 3:
                    b4 = self.check_edge(vertex_list[traverse_point + 4], vertex_list[traverse_point + 5])
                    if b4 == 1:
                        available_moves -= 1
                    else:
                        edge4 = vertex_list[traverse_point + 4] + vertex_list[traverse_point + 5]
                    print(edge4)
                steps += 1

            print(str(available_moves)+" Moves Left in Parent Array "+parent)
            fitness_array[fitness_index] = parent  # string
            if available_moves == 1:  # KB for available_moves == 1
                fitness_array[fitness_index + 1] = 0.8  # statistical value

            elif available_moves == 2:  # KB for available_moves == 2
                fitness_array[fitness_index + 1] = 0.2  # statistical value

            elif available_moves == 3:  # KB for available_moves == 3
                fitness_array[fitness_index + 1] = 0.5  # statistical value

            elif available_moves == 4:  # KB for available_moves == 4
                fitness_array[fitness_index + 1] = 0.7  # statistical value

            elif available_moves == 0:  # KB for available_moves == 4
                fitness_array[fitness_index + 1] = 0  # statistical value

            # All 4 edges will set a statistical value in crossover array
            self.set_crossover_values(edge1, fitness_array[fitness_index + 1])
            self.set_crossover_values(edge2, fitness_array[fitness_index + 1])
            self.set_crossover_values(edge3, fitness_array[fitness_index + 1])
            self.set_crossover_values(edge4, fitness_array[fitness_index + 1])
            fitness_index += 2
            if skip_traverse_point == 2 or skip_traverse_point == 5 or skip_traverse_point == 10:
                traverse_point += 1
            skip_traverse_point += 1        # it will skip the traverse point that is not a parent Exp(D,H,L,P)
            traverse_point += 1
            all_parents += 1                # determines the universal endpoint of the algorithm

        for x in crossover_array:
            print(x)

        highest_value1 = 0
        highest_vertex1 = ""
        highest_vertex2 = ""
        highest_vertex3 = ""

        element = 1
        while element != len(crossover_array)-1:
            #print(str(crossover_array[element])+" vs hv: "+str(highest_value1))
            if crossover_array[element] > highest_value1:
                highest_value1 = crossover_array[element]
                highest_vertex1 = crossover_array[element-1]
            #elif crossover_array[element] == highest_value1:
                #highest_vertex2 = crossover_array[element-1]
                #highest_vertex3 = crossover_array[element-1]
            element += 2

        #v1 = ""
        #v2 = ""
        random = randint(1, 3)
        print("AI is dumb")
        print(highest_vertex1)
        print(highest_vertex2)
        print(highest_vertex3)
        print("Best possible vertex move is: ")
        print(highest_vertex1)
        self.AI_mapping(highest_vertex1)
        #if random == 1:
            #v1 = highest_vertex1[0]
            #v2 = highest_vertex1[1]
            #print(highest_vertex1)
            #self.AI_mapping(highest_vertex1)
        #elif random == 2:
            #v1 = highest_vertex2[0]
            #v2 = highest_vertex2[1]
            #print(highest_vertex2)
            #self.AI_mapping(highest_vertex2)
        #else:
            #v1 = highest_vertex3[0]
            #v2 = highest_vertex3[1]
            #print(highest_vertex3)
            #self.AI_mapping(highest_vertex3)

    def AI_mapping(self, ai_move):
        print("in")
        if ai_move == "AB":
            #self.addEdge("A", "B", array1, 0)
            self.Button_AB.invoke()
        elif ai_move == "AE":
            #self.addEdge("A", "E", array1, 1)
            self.Button_AE.invoke()
        elif ai_move == "EF":
            #self.addEdge("E", "F", array1, 2)
            self.Button_EF.invoke()
        elif ai_move == "BF":
            #self.addEdge("B", "F", array1, 3)
            self.Button_BF.invoke()
        elif ai_move == "BC":
            #self.addEdge("B", "C", array1, 4)
            self.Button_BC.invoke()
        elif ai_move == "FG":
            #self.addEdge("F", "G", array1, 5)
            self.Button_FG.invoke()
        elif ai_move == "CG":
            #self.addEdge("C", "G", array1, 6)
            self.Button_CG.invoke()
        elif ai_move == "CD":
            #self.addEdge("C", "D", array1, 7)
            self.Button_CD.invoke()
        elif ai_move == "GH":
            #self.addEdge("G", "H", array1, 8)
            self.Button_GH.invoke()
        elif ai_move == "DH":
            #self.addEdge("D", "H", array1, 9)
            self.Button_DH.invoke()
        elif ai_move == "EI":
            #self.addEdge("E", "I", array2, 0)
            self.Button_EI.invoke()
        elif ai_move == "IJ":
            #self.addEdge("I", "J", array2, 1)
            self.Button_IJ.invoke()
        elif ai_move == "FJ":
            #self.addEdge("F", "J", array2, 2)
            self.Button_FJ.invoke()
        elif ai_move == "JK":
            #self.addEdge("J", "K", array2, 3)
            self.Button_JK.invoke()
        elif ai_move == "GK":
            #self.addEdge("G", "K", array2, 4)
            self.Button_GK.invoke()
        elif ai_move == "KL":
            #self.addEdge("K", "L", array2, 5)
            self.Button_KL.invoke()
        elif ai_move == "HL":
            #self.addEdge("H", "L", array2, 6)
            self.Button_HL.invoke()
        elif ai_move == "IM":
            #self.addEdge("I", "M", array3, 0)
            self.Button_IM.invoke()
        elif ai_move == "MN":
            #self.addEdge("M", "N", array3, 1)
            self.Button_MN.invoke()
        elif ai_move == "JN":
            #self.addEdge("J", "N", array3, 2)
            self.Button_JK.invoke()
        elif ai_move == "NO":
            #self.addEdge("N", "O", array3, 3)
            self.Button_NO.invoke()
        elif ai_move == "KO":
            #self.addEdge("K", "O", array3, 4)
            self.Button_KO.invoke()
        elif ai_move == "OP":
            #self.addEdge("O", "P", array3, 5)
            self.Button_OP.invoke()
        elif ai_move == "LP":
            #self.addEdge("L", "P", array3, 6)
            self.Button_LP.invoke()

    def klara_screen(self):
        self.klara_welcome = tkinter.Tk();
        self.GuiWindow9.title("Klara Welcome Screen");
        self.GuiWindow9.geometry("1920x1080");
        self.GuiWindow9.state('zoomed');
        photoImages = tkinter.PhotoImage(file="images\i.png", master=self.GuiWindow9);
        BgImages = tkinter.Label(self.GuiWindow9, image=photoImages);



global numbers_user, numbers_ai, recent_edge
recent_edge=""
current_player = ""
player1_name = "Player 1"
player2_name = "Klara (AI)"
numbers_user = 1
numbers_ai = 1
array1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
array2 = [0, 0, 0, 0, 0, 0, 0]
array3 = [0, 0, 0, 0, 0, 0, 0]
tileScored = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player1 = 0
player2 = 0
turns = 1
freeMove = 0
W = War_Game()
winsound.PlaySound("Sounds/Clicks/BtnClick1.wav", winsound.SND_ASYNC)
W.Interface()

