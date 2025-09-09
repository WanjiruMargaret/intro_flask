from flask import Blueprint, jsonify, request

#create student blueprint
student_bp = Blueprint("student", __name__)

@student_bp.route("/",methods=["GET"])
def home():
    return "Welcome to Student Management System"

#routes and controller logic
@student_bp.route("/student/add", methods=["POST"])
def add_user():
    print("Add student was hit")
    return "Adding a student"

@student_bp.route("/student", methods=["GET"])
def list_users():
    print("List students")
    users=[{"id":1,"name":"John Doe"},{"id":2,"name":"Jane Doe"}]
    return jsonify(users)
