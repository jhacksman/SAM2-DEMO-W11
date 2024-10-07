# SAM2-DEMO-W11

![SAM2 GUI Mockup](path_to_your_image.png)
*Placeholder for GUI screenshot*

## Overview

### Objective

Welcome to the **SAM2 DEMO W11**! This project aims to simplify the process of showcasing Meta's **Segment Anything Model 2 (SAM2)** on Windows 11. Our goal is to make it extremely easy for users to install, run, and demonstrate SAM2 with minimal technical knowledge.

## Features

- **Easy Setup**: No command-line or PowerShell required.
- **Pre-built `.exe` File**: One-click installation and execution.
- **User-Friendly GUI**:
  - Start/Stop the SAM2 server.
  - Display local IP address automatically.
  - Choose between **LAN Mode** and **Local-only Mode**.
  - Optional advanced console for power users.
- **Webcam Integration**:
  - Select from multiple connected webcams.
  - Real-time segmentation display.
- **Modern Design**: Clean, intuitive interface focused on ease of use.

## Installation

### Prerequisites

- **Windows 11** operating system.
- An internet connection to download the application.

### Steps

1. **Download the Application**:
   - Go to the [Releases](https://github.com/jhacksman/SAM2-DEMO-W11/releases) page on GitHub.
   - Download the latest version of `SAM2_Easy_Demo.exe`.

2. **Run the Installer**:
   - Locate the downloaded `SAM2_Easy_Demo.exe` file.
   - Double-click to run the installer.
   - Follow the on-screen instructions to complete the installation.

3. **Launch the Application**:
   - After installation, a shortcut will appear on your desktop.
   - Double-click the **SAM2 Easy Demo** icon to open the GUI.

## Using the Application

### Launching the GUI

Upon launching the application, you'll see the main GUI:

![Main GUI Layout](path_to_your_image.png)
*Placeholder for GUI screenshot*

**Main Features**:

- **Start/Stop Buttons**: Easily control the SAM2 server.
- **Server Mode Selection**: Toggle between **LAN Mode** and **Local-only Mode**.
- **Webcam Selection**: Choose which connected webcam to use.
- **IP Address Display**: Automatically shows your local IP address.
- **Advanced Console** (optional): View detailed logs and server output.

### Server Modes

#### LAN Mode

- **Purpose**: Allows other devices on your LAN to access the SAM2 server.
- **Usage**:
  1. Select **LAN Mode**.
  2. Click **Start** to launch the server.
  3. Share the displayed IP address with devices on your network.

#### Local-only Mode

- **Purpose**: Restricts server access to your local machine.
- **Usage**:
  1. Select **Local-only Mode**.
  2. Click **Start** to launch the server.
  3. The server is accessible only on your machine.

### Webcam Segmentation

#### Selecting Your Webcam

- Use the **Webcam Selection** dropdown to choose from connected webcams.
- If only one webcam is connected, it will be selected by default.

#### Viewing Real-Time Segmentation

- **On Your Machine**:
  - Click **Start** to begin the server.
  - A window will display the real-time segmentation results from your webcam.

- **On Other Devices (LAN Mode Only)**:
  - Ensure the server is running in **LAN Mode**.
  - On another device connected to the same network, open a web browser.
  - Enter the displayed IP address (e.g., `http://192.168.1.2:8080`).
  - View the real-time segmentation stream.

### Starting and Stopping the Server

- **Start Server**:
  - Select your preferred **Server Mode** and **Webcam**.
  - Click the **Start** button.
  - The server status will update to **Running**.

- **Stop Server**:
  - Click the **Stop** button at any time to halt the server.
  - The server status will update to **Stopped**.

## Screenshots

### Main GUI Layout

![Main GUI](path_to_your_image.png)
*Placeholder for Main GUI screenshot*

### Real-Time Segmentation Display

![Segmentation Display](path_to_your_image.png)
*Placeholder for Segmentation Display screenshot*

## FAQs

### Q1: The application won't install. What should I do?

**A**: Ensure you're running **Windows 11**. If the problem persists:

- Temporarily disable any antivirus software.
- Right-click the installer and select **Run as administrator**.
- Check if you have sufficient disk space.

### Q2: The GUI doesn't display my IP address.

**A**:

- Make sure your computer is connected to a network.
- Restart the application.
- Disable any VPNs or proxy settings that might interfere.

### Q3: Other devices can't connect to the server in LAN Mode.

**A**:

- Confirm all devices are on the same LAN network.
- Check your firewall settings to ensure the application isn't blocked.
- Use the correct IP address displayed in the GUI.

### Q4: The webcam preview isn't displaying.

**A**:

- Ensure your webcam is properly connected and recognized by Windows.
- Close other applications that might be using the webcam.
- Try selecting a different webcam if available.

### Q5: The application crashes when I click **Start**.

**A**:

- Run the application as an administrator.
- Update your graphics drivers.
- Contact us by submitting an issue with details.

## Contributing

We welcome contributions to improve this project!

### Submitting Issues

- Navigate to the [Issues](https://github.com/jhacksman/SAM2-DEMO-W11/issues) section on GitHub.
- Click **New Issue**.
- Provide a clear description and steps to reproduce the issue.
- Include screenshots if applicable.

### Contributing Code

1. **Fork the Repository**:
   - Click the **Fork** button on the GitHub page.

2. **Clone Your Fork**:
   - ```bash
     git clone https://github.com/jhacksman/SAM2-DEMO-W11.git
     ```

3. **Create a New Branch**:
   - ```bash
     git checkout -b feature-name
     ```

4. **Make Your Changes**:
   - Commit your updates with clear messages.

5. **Push to Your Fork**:
   - ```bash
     git push origin feature-name
     ```

6. **Submit a Pull Request**:
   - Go to your fork on GitHub.
   - Click **Compare & pull request**.
   - Provide a detailed description of your changes.

### Guidelines

- Follow the existing code style.
- Test your changes thoroughly before submitting.
- Update documentation and screenshots as needed.

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for choosing the **SAM2 Easy Demo for Windows 11**! We're excited to see the amazing things you'll do with it.

For any questions or assistance, feel free to [open an issue](https://github.com/jhacksman/SAM2-DEMO-W11/issues) or reach out to us directly.
