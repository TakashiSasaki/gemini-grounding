# Shared Agent Rules for Gemini Grounding Repository

This document outlines general conventions and rules for AI agents operating within this repository.

## 1. Directory Structure Interpretation

Test cases are organized hierarchically:
-   `/gemini-2.5-flash-lite/caseX/tX/pX.XXX/` defines a specific test scenario with parameters.
    -   `caseX`: Test case identifier.
    -   `tX`: Temperature setting or test trial.
    -   `pX.XXX`: `top_p` parameter value.
-   Subdirectories like `/both/`, `/grounding-by-google-search/`, `/url-context-tool/`, `/none/` indicate the grounding/tooling configuration for that scenario.

## 2. File Naming Conventions and Relationships

-   **`*.py` files (e.g., `1.py`, `2.py`, `3.py`)**: Python scripts that implement Gemini API calls for a specific test. These often contain `types.Content` objects defining the conversation.
-   **`*.json` files (e.g., `1.json`, `2.json`, `3.json`)**:
    -   These represent the *initial conversation state* for the corresponding Python script.
    -   They typically contain the first user prompt and an empty model response placeholder.
    -   They are derived from the `contents` list in the `*.py` file: take the first `user` turn and add an empty `model` turn.
-   **`image.json`**: Defines the *intended* model configuration (e.g., Temperature, Top P, enabled tools like Grounding or URL Context) for the tests within its directory. This represents the target state.
-   **`image.png`**: A screenshot of a UI showing the intended model settings, which `image.json` is a JSON representation of.
-   **`README.md` / `AGENTS.md`**: Documentation providing context, explanations, and discrepancy analyses for the files in their respective directories.

## 3. Configuration Discrepancy Analysis

When comparing Python script implementations to `image.json`:
-   Python scripts' `generate_content_config` and `tools` parameters define the *actual* API call settings.
-   `image.json` defines the *intended* settings.
-   Identify and report discrepancies in parameters such as `temperature`, `top_p`, `max_output_tokens`, and tool enablement (e.g., `google_search`, `url_context`).

## 4. Default Parameter Assumptions

-   If a parameter is not explicitly set in a Python script, assume the default value for the Gemini API. This default may differ from the `image.json`'s intended explicit setting.
