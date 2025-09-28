# borders

## Release Notes - Version 1.3.0

- Borders now depends on **textlinebreaker v1.0.0**.
- Internal implementation switched from `split_line()` to the new `TextLineBreaker` class.
- Improved compatibility and stability with the updated textlinebreaker package.
- No breaking changes for users: all features and usage remain unchanged.

### Release Notes - Version 1.2.0

- Added support for single string input.
- Enhanced Color Control: Any color available can now be used for the text, the frame and their background colors.
- Added new styles of frames.

### Release Notes - Version 1.1.2.post

- Fixed indentation issue in README.md.
- In the files requirements.txt and pyproject.toml specified dependencies version to be used.

### Release Notes - Version 1.1.2

- Enhanced Spacing Control: Added alignment control for the frame and the text within the frame.
- Improved Width Customization: Better control over minimum and maximum width of the frame and text lines.
