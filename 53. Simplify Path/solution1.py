class Solution:
    def simplifyPath(self, path: str) -> str:
        sp_path = path.split("/")

        if path[0] != '/':
            return "/"
        
        response = []
        # Remove last /
        # Replace // with /
        for dir in sp_path:
            if not dir: continue
            if dir == "..":
                if response: response.pop(-1)
            else:
                if not dir == ".": 
                    response.append(dir)
        
        response = "/" + "/".join(response)

        return response


# Example 1:
path = "/home/"
expected = "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
s = Solution()
result = s.simplifyPath(path)
print(result)
print(result == expected)

# Example 2:
path = "/../"
expected = "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
s = Solution()
result = s.simplifyPath(path)
print(result)
print(result == expected)


# Example 3:
path = "/home//foo/"
expected = "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
s = Solution()
result = s.simplifyPath(path)
print(result)
print(result == expected)

# Example 4:
path = "/a/./b/../../c/"
expected = "/c"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
s = Solution()
result = s.simplifyPath(path)
print(result)
print(result == expected)

# Example 5:
path = "/a/../../b/../c//.//"
expected = "/c"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
s = Solution()
result = s.simplifyPath(path)
print(result)
print(result == expected)

# Example 6:
path = "/../lGyI/"
expected = "/lGyI"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
s = Solution()
result = s.simplifyPath(path)
print(result)
print(result == expected)