# thorlabs-cam
Tools for thorlabs scientific camera sdk

This library is built with a thread-based algorithm that continuously polls frames from the camera in a dedicated background thread, ensuring high-performance and non-blocking camera operation.

## Installation
This package is for **Windows only**. 

### 1. Thorlabs SDK Setup

**Download**:  
Go to the [Thorlabs Software Page](https://www.thorlabs.co.jp/software_pages/ViewSoftwarePage.cfm?Code=ThorCam), select the "Programming Interfaces" tab, and download the "Windows SDK and Doc. for Scientific Cameras".
   
**Add to Path**:  
Extract the downloaded folder. Add the full path to `...\Scientific Camera Interfaces\SDK\Python Toolkit\dlls\64_lib` (for 64-bit Python) or `...\32_lib` (for 32-bit Python) to your system's Path environment variable.

### 2. Install Python Packages  

**Install Thorlabs Python SDK**:  
The zip folder `thorlabs_tsi_camera_python_sdk_package.zip` can be found within `...\Scientific Camera Interfaces\SDK\Python Toolkit`.  
```
pip install thorlabs_tsi_camera_python_sdk_package.zip
```

**Install This library**:

```
pip install git+https://github.com/pendwmpian/thorlabs-cam
```
