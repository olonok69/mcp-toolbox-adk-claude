https://cloud.google.com/sdk/docs/install#deb


https://googleapis.github.io/genai-toolbox/how-to/connect_via_mcp/
https://codelabs.developers.google.com/mcp-toolbox-bigquery-dataset?hl=en#1

 export GOOGLE_APPLICATION_CREDENTIALS=complete-tube-421007-208a4862c992.json
 gcloud auth application-default login --impersonate-service-account olonok@gmail.com


 ./toolbox --tools-file="tools.yaml"


 {
  "mcpServers": {
    "database-toolbox": {
      "command": "D:\\repos\\mcp-toolbox\\toolbox.exe",
      "args": ["--tools-file", "toolsdb.yaml", "--stdio"],
      "cwd": "D:\\repos\\mcp-toolbox",
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "complete-tube-421007-208a4862c992.json"
      }
    }
  }
}