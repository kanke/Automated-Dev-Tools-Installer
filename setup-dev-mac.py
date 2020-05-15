#!/usr/bin/env python

import re
import subprocess


def install_home_brew():
    print ("*** Installing Home Brew ***")

    # Installing Home brew
    subprocess.call("/usr/bin/ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"", shell=True)

    # Updating Home brew
    subprocess.call("brew update", shell=True)

    # Install other Dev tools using home brew
    install_all_tools()


def install_all_tools():

# Command Lne Tools

    # Install git
    print ("*** Installing Git ***")
    subprocess.call("brew install git", shell=True)

# Development Applications

    # Install java
    print ("*** Installing Java 8(AdoptOpenJDK) ***")
    subprocess.call("brew tap homebrew/cask-versions", shell=True)
    subprocess.call("brew cask install adoptopenjdk8", shell=True)

    # Install nodeenv
    print ("*** Installing Node Environment(npm/node) ***")
    subprocess.call("brew install node", shell=True)

    # Install Atlassian SDK
    # print ("*** Installing Atlassian SDK ***")
    # subprocess.call("brew tap atlassian/tap", shell=True)
    # subprocess.call("brew install atlassian/tap/atlassian-plugin-sdk", shell=True)

    # Install Atlassian SDK 6
    print ("*** Installing Atlassian SDK ***")
    subprocess.call("brew tap atlassian/tap", shell=True)
    subprocess.call("brew install atlassian/tap/atlassian-plugin-sdk62", shell=True)

    # Install yarn
    print ("*** Installing Yarn ***")
    subprocess.call("brew install yarn", shell=True)

    # Install ngrok
    print ("*** Installing Ngrok ***")
    subprocess.call("brew cask install ngrok", shell=True)

    # Install docker
    print ("*** Installing Docker ***")
    subprocess.call("brew cask install docker", shell=True)

    # Install iTerm2
    print ("*** Installing iTerm ***")
    subprocess.call("brew cask install iterm2", shell=True)

    # Install slack
    print ("*** Installing Slack ***")
    subprocess.call("brew cask install slack", shell=True)

    # Install chrome
    print ("*** Installing Google Chrome ***")
    subprocess.call("brew cask install google-chrome", shell=True)

    # Install zoom
    print ("*** Installing Zoom ***")
    subprocess.call("brew cask install zoomus", shell=True)

# IDE & Text Editors

    # Install IntelliJ IDEA Ultimate Edition
    print ("*** Installing IntelliJ IDEA Ultimate Edition ***")
    subprocess.call("brew cask install intellij-idea", shell=True)

def print_tool_versions():
    print ("You have installed the following app versions")
    subprocess.call("brew list --versions", shell=True)
    subprocess.call("brew cask list --versions", shell=True)

user_input = raw_input("This will setup your Mac. Do not run this if your Mac is not new! Continue? [y/N]")

if re.match("^([yY][eE][sS]|[yY])+$", user_input):
    print ("Cool! Starting now......")
    install_home_brew()
    print_tool_versions()

elif re.match("^([nN][oO]|[nN])+$", user_input):
    print ("Bye Felicia!.....")

else:
    print ("Your response is not recognised. Try: yes/no or y/N in any alphabet case")

