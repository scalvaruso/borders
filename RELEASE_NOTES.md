# borders

## Release Notes – v1.4.0 (2025-10-04)

### Overview

This release introduces a **license change** for Borders, moving from the MIT License to the **Apache License, Version 2.0**.  
There are no functional or API changes in this release. All code behavior remains identical to v1.3.0.

### Why the License Change?

- To align Borders with other widely used scientific Python libraries (e.g., NumPy, Pandas).
- To provide stronger protections for both contributors and users, particularly regarding patents and contributions.
- To ensure long-term compatibility with projects and organizations that prefer Apache 2.0.

### Impact for Users

- **Code functionality**: Unchanged.
- **Legal/Compliance**: Projects embedding or redistributing Borders should verify compatibility with Apache 2.0.
- **Migration**: No changes required in your code — only license compliance should be reviewed.

### Next Steps

- Review the updated LICENSE file included in this release.
- Continue using Borders as before; no breaking changes have been introduced.

---

Thank you to all contributors and users for your support!

---

#### Release Notes - Version 1.3.0

- Borders now depends on **textlinebreaker v1.0.0**.
- Internal implementation switched from `split_line()` to the new `TextLineBreaker` class.
- Improved compatibility and stability with the updated textlinebreaker package.
- No breaking changes for users: all features and usage remain unchanged.

#### Release Notes - Version 1.2.0

- Added support for single string input.
- Enhanced Color Control: Any color available can now be used for the text, the frame and their background colors.
- Added new styles of frames.

#### Release Notes - Version 1.1.2.post

- Fixed indentation issue in README.md.
- In the files requirements.txt and pyproject.toml specified dependencies version to be used.

#### Release Notes - Version 1.1.2

- Enhanced Spacing Control: Added alignment control for the frame and the text within the frame.
- Improved Width Customization: Better control over minimum and maximum width of the frame and text lines.
