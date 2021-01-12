
import repoInfo,filechange
import gitcommands as git
def init():
    info = repoInfo.checkinfoInDir()
    if('n' in info):
        info.remove('n')
        git.init()
        git.createReadme()
        git.add(['.'])
        git.commit(['README.md'])
        git.setBranch(info[1])
        git.setremote(info[0])
        git.push(info[0] , info[1])
        print('initial setup done :)')
        filechange.ischanged(info[0] , info[1])
    else:
        print('Retrieving info from git directory')
        filechange.ischanged(info[0] , info[1])

if __name__ == '__main__':
    init()
