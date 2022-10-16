from flask import Flask, request, redirect, render_template, session
import db

app = Flask(__name__)
app.secret_key = "foo"