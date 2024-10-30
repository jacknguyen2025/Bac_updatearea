## Bac Area Update Plugin

### Introduction
The **Bac Area Update Plugin** is a tool that helps calculate the area for features in a QGIS layer. This plugin allows users to easily add area fields (in both square meters and hectares) to a layer's attribute table and automatically populate each feature’s area based on its geometry.

This plugin is especially useful for GIS analysts and professionals in environmental science, urban planning, or land management who need to perform area calculations quickly and accurately.

---

### Key Features
- **Add Area Fields**: Automatically creates area fields in the attribute table in square meters and hectares.
- **Update Areas on Demand**: Allows users to choose whether to calculate areas for all features or only selected features.
- **Display Progress with Cancel Option**: Provides a progress bar to show completion percentage and a "Cancel" button to stop the process at any time.

---

### Installation Guide
1. **Move the Plugin to the QGIS Plugins Folder**:
   - Download the plugin to your computer and move the `Bac_updatearea` folder to the QGIS plugins directory:
     - **Windows**: `C:\Users\<YourUsername>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Bac_updatearea`
     - **macOS**: `/Users/<YourUsername>/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/Bac_updatearea`
     - **Linux**: `/home/<YourUsername>/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Bac_updatearea`

2. **Restart QGIS** to ensure it recognizes the new plugin.

3. **Enable the Plugin**:
   - Go to `Plugins > Manage and Install Plugins…`.
   - Find "Bac Area Update Plugin" in the list and select `Install` or `Enable`.

---

### Usage Guide

1. **Open the Target Layer**:
   - Select the layer for which you want to calculate areas for the features within it.

2. **Run the Bac Area Update Plugin**:
   - Once the plugin is enabled, its icon will appear on the QGIS toolbar or in the plugin menu.
   - Click on the `Update Area Fields` icon to launch the plugin.

3. **Using the Input Dialog**:
   - A new dialog box will open with the following options:
     - **Area (m²) Field**: Enter the name of the field to store the area in square meters (m²). The default value is `area_sq`.
     - **Area (ha) Field**: Enter the name of the field to store the area in hectares (ha). The default value is `area_ha`.
     - **Selected Features Only**: Select this option if you only want to calculate areas for selected features in the layer.

4. **Start Area Calculation**:
   - Click `OK` to begin updating area fields.
   - A **progress bar** will display the completion percentage, and a `Cancel` button allows you to stop the process if needed.

5. **Completion**:
   - Once complete, a notification will display the number of features that were updated with area values.
   - If you clicked `Cancel` during the process, the calculation will immediately stop, and any changes made will be rolled back.

---

### Notes
- The plugin requires that the layer is in **editable mode** to update the data.
- Be sure to choose unique field names for the area fields to avoid conflicts with existing fields.

---

With this guide, you can use the **Bac Area Update Plugin** to efficiently manage and calculate areas for GIS features within QGIS.
