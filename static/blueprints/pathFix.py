def pathFixer(path, gid):
    print('PathFixer: {0} {1}'.format(path, gid))
    splitPath = str(path).rstrip().split('/')
    print("Fix list: {0}".format(splitPath))
    splitPath = splitPath if splitPath[0] not in ['', '.', '~', '..', '/','\\','&'] else splitPath[1:]
    splitPath = splitPath if splitPath[len(splitPath)-1] not in ['', '.', '~', '..', '/','\\','&'] else splitPath[:1]
    if splitPath[0] == 'home':
        splitPath[0] = gid
        path = '/'
        for part in splitPath:
                path = path + part + '/'
        print('In progress: {}'.format(path))
        return path