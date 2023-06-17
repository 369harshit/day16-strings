def compareVersion(version1, version2):
    # Split the version strings into components
    v1 = version1.split(".")
    v2 = version2.split(".")

    # Compare each corresponding component
    for i in range(max(len(v1), len(v2))):
        
        if i < len(v1):
             num1 = int(v1[i]) 
        else:
            0
       
        if i < len(v2):
             num2 = int(v2[i]) 
        else:
            0

        if num1 < num2:
            return -1
        elif num1 > num2:
            return 1

    return 0

version1 = "1.2.3"
version2 = "1.2.4"
print(compareVersion(version1, version2))  # Output: -1

version1 = "1.2.3"
version2 = "1.2.3"
print(compareVersion(version1, version2))  # Output: 0

version1 = "1.2.3"
version2 = "1.2.2"
print(compareVersion(version1, version2))  # Output: 1
