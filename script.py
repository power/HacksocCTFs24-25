import os
import time

def main():
    string = input("[+] Enter your string: ")
    f = input("[+] Filename: ")
    count = 0
    for c in string:
        count += 1
        if c == " ":
            print("imgs/flags-space.png")
            os.system("cp imgs/flag-space.png final/{0}final-flag-space.png".format(count))
        else:
            print("imgs/flag-{0}.png".format(c))
            os.system("cp imgs/flag-{0}.png final/{1}final-flag-{2}.png".format(c, count, c))


    print("Total images: {0}".format(count))
    time.sleep(5)


    os.system("cd final; cat *.png | ffmpeg -f image2pipe -i - {0}.mp4; mv {0}.mp4 ../{0}.mp4".format(f))
    os.system("rm final/*.png")
if __name__ == "__main__":
    main()