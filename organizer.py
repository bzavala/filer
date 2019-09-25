import os, shutil, string, platform, itertools

if platform.system() is 'Windows':
    home=os.environ.get("USERPROFILE")
    dl=home + '/Desktop/Downloads/'
else:
    home=os.environ.get("HOME")
    dl=home + '/Downloads/'

dirs_exist=home + '/dirs_exist.txt'

img_ext=('.gif','.jpg','.png','.tif','.eps','.psd','.ai')
doc_ext=('.pdf','.txt','.html','.py','.js','.css','.conf','.sh','.ttf')
vid_ext=('.mov','.mpg','.avi','.mp4','.wmv','.asf','.mpeg','.flv')
aud_ext=('.ogg','.mp3','.m4a','.aif','.wav','.wma','.au')
pkg_ext=('.zip','.dmg','.sit','.tar','.msi')
app_ext=('.app','.exe','.air')

ext_list=(img_ext,doc_ext,vid_ext,aud_ext,pkg_ext,app_ext)

class organizer:
    def __init__(self,root_dir):
        img_dir=root_dir + "/images/"
        doc_dir=root_dir + "/documents/"
        vid_dir=root_dir + "/video/"
        aud_dir=root_dir + "/audio/"
        pkg_dir=root_dir + "/packages/"
        app_dir=root_dir + "/applications/"
        misc_dir=root_dir + "/misc/"
        self.dest_dir=(img_dir,doc_dir,vid_dir,aud_dir,pkg_dir,app_dir,misc_dir)
        #self.adict=dict(itertools.izip(ext_list,self.dest_dir))

    def mk_dirs(self,root_dir):
        for dirpath,dirnames,filenames in os.walk(root_dir):
            for dir in dirnames:
                for newdir in self.dest_dir:
                    if not os.path.exists(newdir):
                        os.mkdir(newdir)
                        print "Creating proof that this function has run."
                        file=open(".dirs_exist","wb")
                        file.write("Yep...\n")
                        file.write("it has\n")
                        file.close
                    
    def mv_files(self,root_dir):
        for dirpath,dirnames,filenames in os.walk(root_dir):    
            for ext in ext_list:
                for file in filenames:
                    if string.lower(os.path.splitext(file)[1]) in img_ext:
                        shutil.move(os.path.join(root_dir,file),self.dest_dir[0])
                    elif string.lower(os.path.splitext(file)[1]) in doc_ext:
                        shutil.move(os.path.join(dl,file),self.dest_dir[1])
                    elif string.lower(os.path.splitext(file)[1]) in vid_ext:
                        shutil.move(os.path.join(dl,file),self.dest_dir[2])
                    elif string.lower(os.path.splitext(file)[1]) in aud_ext:
                        shutil.move(os.path.join(dl,file),self.dest_dir[3])
                    elif string.lower(os.path.splitext(file)[1]) in pkg_ext:
                        shutil.move(os.path.join(dl,file),self.dest_dir[4])
                    elif string.lower(os.path.splitext(file)[1]) in app_ext:
                        shutil.move(os.path.join(dl,file),self.dest_dir[5])
                        #for dir in dirnames:
                        #for ext,dir in self.adict:
                            #shutil.move(os.path.join(root_dir,file),dir)

    def mv_dirs(self,root_dir):
        for dirpath,dirnames,filenames in os.walk(root_dir):
            for dir in dirnames:
                for newdir in self.dest_dir:
                    if dir != newdir:
                        shutil.move(os.path.join(root_dir,dir),self.dest_dir[6])

o=organizer(dl)
if os.path.exists(dirs_exist):
    o.mv_files(dl)
    o.mv_dirs(dl)                                
else:
    o.mk_dirs(dl)
