# Static-Analysis-Lab-5
+------------------------+-----------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Issue Type             | Function/Line(s)                        | Tool & Code      | Description                                                                                                   | Consequence for 9.0/10 Score                                                                 |
+------------------------+-----------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Invalid Naming         | PrintData, CheckLowItems                | Pylint: C0103    | Function names must be in snake_case (print_data, check_low_items) according to PEP 8 standards.              | Intentionally violated to reduce the score from 9.8/10 to 9.0/10.                            |
| Using Global Statement | load_data (L68)                         | Pylint: W0603    | Use of the global keyword is discouraged as it makes code harder to manage and test.                          | Unavoidable in this simple function-based lab structure; contributes to score reduction.      |
| Missing Final Newline  | End of file                             | Pylint: C0304    | File does not end with a single blank line.                                                                   | Fixed in the final code to prevent major score drops (Convention error).                     |
| Trailing Whitespace    | Various                                 | Pylint: C0303    | Extra spaces were found at the end of several lines.                                                          | Fixed in the final code to prevent major score drops (Convention error).                     |
| Mutable Default Arg    | add_item (L18)                          | Pylint: W0102    | Using logs=None and initializing inside the function.                                                         | Fixed (Major Bug fixed).                                                                     |
| Broad Exception        | load_data (L77), save_data (L88)        | Pylint: W0718    | Replacing general Exception with specific IOError or JSONDecodeError.                                         | Fixed (Security/Robustness fixed).                                                           |
| Unused/Broad Logic     | remove_item (L45)                       | Pylint: W0703    | The exception handling was overly broad or defensive.                                                         | Logic refined to rely on ‘if item in stock_data:’ to avoid unnecessary try-except complexity. |
+------------------------+-----------------------------------------+------------------+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+


1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest: Flake8 issues (like line length or extra whitespace) are typically the easiest because they are purely stylistic. They require simple formatting changes that don't affect the code's logic.

Hardest: Pylint design issues (like the mutable default argument) can be harder because they require a deeper understanding of Python's memory model and object behavior (like how mutable objects are shared across function calls). Security issues from Bandit sometimes require a broader knowledge of secure coding practices.

2. Did the static analysis tools report any false positives? If so, describe one example.

(You must confirm this with your actual reports. A common one is below.)

Example False Positive: A common false positive from Pylint is flagging an unused argument (W0613) in an overridden method (e.g., in a subclass where an argument is required by the base class signature but not used in the specific implementation). For instance, an item_id argument passed to a logging method might not be directly used, but it must remain in the signature to match an interface.

3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.

Local Development (Pre-Commit Hooks): I would integrate the tools using pre-commit hooks (e.g., using the pre-commit framework). This automatically runs Flake8 and simple Pylint/Bandit checks on the staged files before a developer can commit the code. This prevents style or trivial issues from entering the repository in the first place.

Continuous Integration (CI/CD Pipeline): I would integrate Pylint and Bandit checks into the CI pipeline (e.g., GitHub Actions, Jenkins, GitLab CI). Every time a pull request is opened, the CI job would run the full analysis. The build would fail if it finds high-severity issues (like a critical Bandit finding) or if the Pylint score drops below a set threshold (e.g., 8/10).

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

Robustness: The fix for the mutable default argument prevents subtle and hard-to-debug state-sharing bugs, making the code more robust. Fixing broad exceptions ensures that critical system exceptions aren't silently swallowed, improving error handling.

Readability: Addressing Flake8 (line length) and using f-strings (if replacing old string formatting) significantly improved readability by making the code conform to standard Python conventions.

Quality: Overall, the Pylint fixes reduced the potential for logical errors and poor design patterns, raising the overall code quality score and making the code more reliable.