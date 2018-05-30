"""
Status code to system
@Marcin Ochociński
"""

from static.tool.console.vt1000 import ForeGround, BackGround

# TODO: prosze o dodatkowych kluczach na każdy typ blędu... i zachuj mi nie ciekawi że to jest nudne...

STATUSCODE = {
    '01': {
        'type': 'error',
        'max': 4,
        'not_used': (2, 4),
        'fcolor': ForeGround.blue,
        'bcolor': BackGround.red,
        # --------------------{only codes}------------------
        1: "Incorrect function.",
        2: "The system cannot find the file specified.",
        3: "The system cannot find the path specified.",
        4: "The system cannot open the file.",
        5: "The handle is invalid.",
        6: "The storage control block address is invalid.",
        7: "The environment is incorrect.",
        8: "An attempt was made to load a program with an incorrect format.",
        9: "The access code is invalid.",
        10: "The data is invalid.",
        11: "Not enough storage is available to complete this operation.",
        12: "The system cannot find the drive specified.",
        13: "The directory cannot be removed.",
        14: "There are no more files.",
        15: "The media is write protected.",
        16: "The system cannot find the device specified.",
        17: "The device is not ready.",
        18: "The device does not recognize the command.",
        19: "The program issued a command but the command length is incorrect.",
        20: "The drive cannot locate a specific area or track on the disk.",
        21: "Not enough storage is available to process this command.",
        22: "The system cannot move the file to a different disk drive.",
        23: "The specified disk cannot be accessed.",
        24: "The process cannot access the file because another process has locked a portion of the file.",
        25: "Too many files opened for sharing.",
        26: "Reached the end of the file.",
        27: "The disk is full.",
        28: "The request is not supported.",
        29: "The network path was not found.",
        30: "The network is busy.",
        31: "The network BIOS command limit has been reached.",
        32: "The specified server cannot perform the requested operation.",
        33: "An unexpected network error occurred.",
        34: "The specified network name is no longer available.",
        35: "Network access is denied.",
        36: "The network name cannot be found.",
        37: "The network BIOS session limit was exceeded.",
        38: "The directory or file cannot be created.",
        39: "Fail on INT 24.",
        40: "Storage to process this request is not available.",
        41: "A write fault occurred on the network.",
        42: "The system cannot open file specified.",
        43: "There is not enough space on the disk.",
        44: "No more internal file identifiers available.",
        45: "The target internal file identifier is incorrect.",
        46: "The system does not support the command requested.",
        47: "This function is not supported on this system.",
        48: "The filename, directory name, or volume label syntax is incorrect.",
        49: "The system call level is not correct.",
        50: "The specified module could not be found.",
        51: "The specified procedure could not be found.",
        52: "The system cannot join or substitute a drive to or for a directory on the same drive.",
        53: "The volume label you entered exceeds the label character limit of the target file system.",
        54: "Cannot create another thread.",
        55: "The recipient process has refused the signal.",
        56: "The segment is already discarded and cannot be locked.",
        57: "The address for the thread ID is not correct.",
        58: "One or more arguments are not correct.",
        59: "The file system does not support atomic changes to the lock type.",
        60: "The system detected a segment number that was not correct.",
        61: "The flag passed is not correct.",
        62: "All pipe instances are busy.",
        63: "The specified extended attribute name was invalid.",
        64: "The directory name is invalid.",
        65: "The extended attributes did not fit in the buffer.",
        66: "The mounted file system does not support extended attributes.",
        67: "The extended attribute table file is full.",
        68: "The subsystem needed to support the image type is not present.",
        69: "Operation is not allowed on a file system internal file.",
        70: "The scope specified was not found.",
        71: "The specified copy of the requested data could not be read.",
        72: "User profile cannot be loaded.",
        73: "Application verifier has found an error in the current process.",
        74: "Profiling not started.",
        75: "Profiling not stopped.",
        76: "The specified compression format is unsupported.",
        77: "The specified hardware profile configuration is invalid.",
        78: "The specified quota list is internally inconsistent with its descriptor.",
        79: "An assertion failure has occurred.",
        80: "WOW Assertion Error.",
        81: "A translator failed to translate resources.",
        82: "The create operation stopped after reaching a symbolic link.",
        83: "A long jump has been executed.",
        84: "Debugger did not handle the exception.",
        85: "One of the pages to lock was already locked.",
        86: "An open/create operation completed while an oplock break is underway.",
        87: "Page fault was a transition fault.",
        88: "Page fault was a demand zero fault.",
        89: "Page fault was satisfied by reading from a secondary storage device.",
        90: "Cached page was locked during operation.",
        91: "A process being terminated has no threads to terminate.",
        92: "The specified process is not part of a job.",
        93: "The specified process is part of a job.",
        94: "A file system or file system filter driver has successfully completed an FsFilter operation.",
        95: "The specified interrupt vector was already connected.",
        96: "Debugger handled exception.",
        97: "The implementation is not capable of performing the request.",
        98: "A version number could not be parsed.",
        99: "The iterator's start position is invalid.",
        100: "The attempted operation required self healing to be enabled.",

    },
    '02': {
        'type': 'critical',
        'max': 5,
        'not_used': (2, 5),
        'fcolor': ForeGround.white,
        'bcolor': BackGround.red,
        # --------------------{only codes}------------------
        1: "Access is denied.",
        2: "The storage control blocks were destroyed.",
        3: "The specified network resource or device is no longer available.",
        4: "A network adapter hardware error occurred.",
        5: "The network resource type is not correct.",
        6: "The segment is locked and cannot be reallocated.",
        7: "This file is checked out or locked for editing by another user.",
        8: "Operation did not complete successfully because the file contains a virus or potentially unwanted software.",
        9: "The pipe state is invalid.",
        10: "The pipe is being closed.",
        11: "The extended attributes are inconsistent.",
        12: "The extended attribute file on the mounted file system is corrupt.",
        13: "The specified extended attribute handle is invalid.",
        14: "An invalid oplock acknowledgment was received by the system.",
        15: "The volume is too fragmented to complete this operation.",
        16: "The file cannot be opened because it is in the process of being deleted.",
        17: "A requested file lock operation cannot be processed due to an invalid byte range.",
        18: "An invalid exception handler routine has been detected.",
        19: "Duplicate privileges were specified for the token.",
        20: "No ranges for the specified operation were able to be processed.",
        21: "A data integrity checksum error occurred. Data in the file stream is corrupt.",
        22: "The command specified a data offset that does not align to the device's granularity/alignment.",
        23: "The shutdown operation failed.",
        24: "The restart operation failed.",
        25: "The maximum number of sessions has been reached.",
        26: "The thread is already in background processing mode.",
        27: "The thread is not in background processing mode.",
        28: "The process is already in background processing mode.",
        29: "The process is not in background processing mode.",
        30: "Attempt to access invalid address.",
        31: "There is a process on other end of the pipe.",
        32: "Unwind exception code.",
        33: "An invalid or unaligned stack was encountered during an unwind operation.",
        34: "An invalid unwind target was encountered during an unwind operation.",
        35: "An attempt was made to lower a quota limit below the current usage.",
        36: "Windows cannot verify the digital signature for this file. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source.",
        37: "A Windows Server has an incorrect configuration.",
        38: "A volume has been accessed for which a file system driver is required that has not yet been loaded.",
        39: "The TDI client could not handle the data received during an indication.",
        40: "The request must be handled by the stack overflow code.",
        41: "The bucket array must be grown. Retry transaction after doing so.",
        42: "The user marshalling buffer has overflowed.",
        43: "The supplied variant structure contains invalid data.",
        44: "The specified buffer contains ill-formed data.",
        45: "There is an IP address conflict with another system on the network.",
        46: "A callback return system service cannot be executed when no callback is active.",
        47: "The validation process needs to continue on to the next step.",
        48: "There are no more matches for the current index enumeration.",
        49: "The range could not be added to the range list because of a conflict.",
        50: "A group marked use for deny only cannot be enabled.",
        51: "A frame consolidation has been executed.",
        52: "The specified registry key is referenced by a predefined handle.",
        53: "The page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.",
        54: "A yield execution was performed and no thread was available to run.",
        55: "The resumable flag to a timer API was ignored.",
        56: "The arbiter has deferred arbitration of these resources to its parent.",
        57: "Crash dump exists in paging file.",
        58: "Specified buffer contains all zeros.",
        59: "An exception occurred in a user mode callback and the kernel callback frame should be removed.",
        60: "Compression is disabled for this volume.",
        61: "The data provider cannot fetch backwards through a result set.",
        62: "The data provider cannot scroll backwards through a result set.",
        63: "The data provider requires that previously fetched data is released before asking for more data.",
        64: "The data provider was not able to interpret the flags set for a column binding in an accessor.",
        65: "One or more errors occurred while processing the request.",
        66: "The Desktop heap encountered an error while allocating session memory. There is more information in the system event log.",
        67: "One of the volume corruption logs is unavailable for being operated on.",
        68: "The handle with which this oplock was associated has been closed. The oplock is now broken.",
        69: "Access to the specified file handle has been revoked.",
        70: "Access to the extended attribute was denied.",
        71: "Invalid access to memory location.",
        72: "Error performing inpage operation.",
        73: "Recursion too deep; the stack overflowed.",
        74: "Cannot complete this function.",
        75: "Invalid flags.",
        76: "The requested operation cannot be performed in full-screen mode.",
        77: "An attempt was made to reference a token that does not exist.",
        78: "The configuration registry database is corrupt",
        79: "The configuration registry key is invalid.",
        80: "The configuration registry key could not be written.",
        81: "One of the files in the registry database had to be recovered by use of a log or alternate copy. The recovery was successful.",
        82: "Cannot create a symbolic link in a registry key that already has subkeys or values.",
        83: "Cannot create a stable subkey under a volatile parent key.",
        84: "The requested control is not valid for this service.",
        85: "A thread could not be created for the service.",
        86: "The service database is locked.",
        87: "An instance of the service is already running.",
        88: "Circular service dependency was specified.",
        89: "The service cannot accept control messages at this time.",
        90: "The specified service does not exist as an installed service.",
        91: "The service has returned a service-specific error code.",
        92: "The specified service has been marked for deletion.",
        93: "The specified service already exists.",
        94: "The system is currently running with the last-known-good configuration.",
        95: "No recovery program has been configured for this service.",
        96: "No more data is on the tape.",
        97: "No serial device was successfully initialized. The serial driver will unload.",
        98: "The floppy disk controller reported an error that is not recognized by the floppy disk driver.",
        99: "The base address or the file offset specified does not have the proper alignment.",
        100: "An attempt to change the system power state was vetoed by another application or driver.",
    },
    '03': {
        'type': 'info',
        'max': 6,
        'not_used': (1, 2, 3, 4),
        'fcolor': ForeGround.white,
        'bcolor': BackGround.blue,
        # --------------------{only codes}------------------
        1: "Configuration of ENVIRONMENT variables.",
        2: "The operation completed successfully.",
        3: "The file exists.",
        4: "The specified network password is not correct.",
        5: "The parameter is incorrect.",
        6: "The file name is too long.",
        7: "The data area passed to a system call is too small.",
        8: "The specified procedure could not be found.",
        9: "The specified module could not be found.",
        10: "There are no child processes to wait for.",
        11: "An attempt was made to move the file pointer before the beginning of the file.",
        12: "The directory is not a subdirectory of the root directory.",
        13: "The segment is already unlocked.",
        14: "The specified path is invalid.",
        15: "A signal is already pending.",
        16: "No more threads can be created in the system.",
        17: "Unable to lock a region of a file.",
        18: "The requested resource is in use.",
        19: "The file system does not support atomic changes to the lock type.",
        20: "The system detected a segment number that was not correct.",
        21: "Cannot create a file when that file already exists.",
        22: "The ring 2 stack is in use.",
        23: "The signal being posted is not correct.",
        24: "The file must be checked out before saving changes.",
        25: "The file type being saved or retrieved has been blocked.",
        26: "The file size exceeds the limit allowed and cannot be saved.",
        27: "The pipe is local.",
        28: "No process is on the other end of the pipe.",
        29: "More data is available.",
        30: "The session was canceled.",
        31: "The wait operation timed out.",
        32: "No more data is available.",
        33: "The copy functions cannot be used.",
        34: "The oplock request is denied.",
        35: "Short name settings may not be changed on this volume due to the global registry setting.",
        36: "Short names are not enabled on this volume.",
        37: "The command specified an invalid field in its parameter list.",
        38: "An operation is currently in progress with the device.",
        39: "An attempt was made to send down the command via an invalid path to the target device.",
        40: "The command specified a number of descriptors that exceeded the maximum supported by the device.",
        41: "An operation is not supported on a compressed file.",
        42: "An operation is not supported on a resident file.",
        43: "An operation is not supported on a directory.",
        44: "No action was taken as a system reboot is required.",
        45: "Waiting for a process to open the other end of the pipe.",
        46: "The number of active profiling objects is at the maximum and no more may be started.",
        47: "A malformed function table was encountered during an unwind operation.",
        48: "Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.",
        49: "Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.",
        50: "Page file quota was exceeded.",
        51: "The stream is not a tiny stream.",
        52: "There is insufficient account information to log you on.",
        53: "The password provided is too short to meet the policy of your user account. Please choose a longer password.",
        54: "The requested interface is not supported.",
        55: "A device was removed so enumeration must be restarted.",
        56: "Device will not start without a reboot.",
        57: "The system is in the process of shutting down.",
        58: "The specified range could not be found in the range list.",
        59: "The password provided is too long to meet the policy of your user account. Please choose a shorter password.",
        60: "The requested operation could not be completed due to a file system limitation.",
        61: "Debugger will reply later.",
        62: "Debugger cannot provide handle.",
        63: "Debugger terminated thread.",
        64: "Debugger terminated process.",
        65: "Debugger got control C.",
        66: "Debugger received RIP exception.",
        67: "Debugger received control break.",
        68: "Debugger command communication exception.",
        69: "An attempt was made to create an object and the object name already existed.",
        70: "This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.",
        71: "The TDI indication has completed successfully.",
        72: "The TDI indication has entered the pending state.",
        73: "The system was put into hibernation.",
        74: "The system was resumed from hibernation.",
        75: "The system has awoken.",
        76: "The requested operation requires elevation.",
        77: "A new volume has been mounted by a file system.",
        78: "The device has succeeded a query-stop and its resource requirements have changed.",
        79: "The translator has translated these resources into the global space and no further translations should be performed.",
        80: "The specified interrupt vector is still connected.",
        81: "The specified interrupt vector was already connected.",
        82: "An operation is blocked waiting for an oplock.",
        83: "Debugger continued.",
        84: "The window cannot act on the sent message.",
        85: "The configuration registry key could not be opened.",
        86: "The configuration registry key could not be read.",
        87: "The service has not been started.",
        88: "The service process could not connect to the service controller.",
        89: "The database specified does not exist.",
        90: "The dependency service or group failed to start.",
        91: "This service cannot be started in Safe Mode.",
        92: "The physical end of the tape has been reached.",
        93: "A tape access reached a filemark.",
        94: "The beginning of the tape or a partition was encountered.",
        95: "A tape access reached the end of a set of files.",
        96: "Tape could not be partitioned.",
        97: "Unable to unload the media.",
        98: "The media in the drive may have changed.",
        99: "No media in drive.",
        100: "A system shutdown is in progress.",
        101: "Start-up Server",
        102: "Create blueprint",
        103: "Login into system",
        104: "The filename or extension is too long.",
        105: "Brutal login to DataBase",
        106: "Register new user",
        107: "Create DataBase session"
    }
}