# EPC QR Code Generator MCP Server

This project provides a Model Context Protocol (MCP) server for generating EPC QR codes based on payment information. 
It exposes a FastAPI web server with streamable HTTP endpoints, including support for Server-Sent Events (SSE).

## Features

- Generate EPC QR codes from structured payment data
- Streamable HTTP API via FastMCP
- SSE endpoint for real-time QR code generation
- Returns QR codes as base64-encoded PNG images

## Requirements

- Python 3.8+
- pip

## Installation

```bash
pip install -r requirements.txt