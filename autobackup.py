#!/usr/bin/python3

from util import stdout_capture
import backup
import datetime
import subprocess
from dataclasses import dataclass
import getpass
import smtplib
from email.mime.text import MIMEText
import json
import os

__version__ = "1.0"


@dataclass
class CommitPushOutput:
    git_add_stderr: str
    git_commit_stdout: str
    git_commit_stderr: str
    git_push_stdout: str
    git_push_stderr: str


def get_head_diff():
    show = subprocess.run(
        ["git", "show", "HEAD"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return show.stdout


def commit_push(right_now):
    git_add = subprocess.run(
        ["git", "add", "saves"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )
    git_commit = subprocess.run(
        ["git", "commit", "-m", f"Automatic backup: {right_now}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    git_push = subprocess.run(
        ["git", "push"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    return CommitPushOutput(
        git_add.stderr,
        git_commit.stdout,
        git_commit.stderr,
        git_push.stdout,
        git_push.stderr,
    )

def get_credentials():
    with open("./credentials.json", "r") as credentials_json:
        return json.load(credentials_json)


def send_email(backup_ok, output, cpo, right_now):
    print("[Auto] Sending email")
    credentials = get_credentials()
    email_text = f"Dear {getpass.getuser()},\n\n"

    if not backup_ok:
        email_text += f"Unfortunately, the backup procedure at {right_now} has not happened successfully.\n\n"
    else:
        email_text += (
            f"Your save files have been backed up automatically at {right_now}.\n\n"
        )

    email_text += "________________________\n\nBackup script output:\n\n{output}\n\nGit add output (stderr):\n\n{cpo.git_add_stderr}\n\nGit commit output (stdout):\n\n{cpo.git_commit_stdout}\n\nGit commit output (stderr):\n\n{cpo.git_commit_stderr}\n\nGit push output (stdout):\n\n{cpo.git_push_stdout}\n\nGit push output (stderr):\n\n{cpo.git_push_stderr}\n\nSincerely, autobackup.py version {__version__}."

    message = MIMEText(email_text)
    message["Subject"] = f"Automatic save files backup at {right_now}"
    message["From"] = credentials["from-who"]
    message["To"] = credentials["to-who"]
    
    smtp = smtplib.SMTP(credentials["smtp"], 25)
    smtp.connect(credentials["smtp"], 25)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(credentials["username"], credentials["password"])
    smtp.sendmail(credentials["from-who"], credentials["to-who"], message.as_string())
    smtp.quit()
    print("[Auto] Email sent")

def set_wd():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)


def main():
    print("[Auto] Starting automatic backup")

    set_wd()
    right_now = datetime.datetime.now().strftime("%F %T")

    cap, old = stdout_capture.start()
    backup_ok = backup.main("backup")
    output = stdout_capture.end(cap, old)

    cpo = commit_push(right_now)

    send_email(backup_ok, output, cpo, right_now)


if __name__ == "__main__":
    main()
