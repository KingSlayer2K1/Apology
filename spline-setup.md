# Spline.design Setup Instructions

## What is Spline?
Spline is a cloud-based 3D design tool that lets you create beautiful, interactive 3D models with animations. It exports directly to web embeds (iframe).

## Quick Setup (5-10 minutes):

### Step 1: Go to Spline
Visit: https://spline.design

### Step 2: Create/Generate Otter
- **Option A (Fastest)**: Click "New File" → Use AI Generate
  - Prompt: "Create a cute, adorable otter in water, realistic fur texture, big expressive eyes, looking at camera, swimming pose"
  - Let AI generate the base model
  
- **Option B (Custom)**: Use 3D shapes to sculpt your own otter
  - Sphere for head
  - Ellipsoid for body
  - Add materials/gradients

### Step 3: Animate the Otter
- Eye tracking: Add "Follow" behavior to eyes → point to cursor
- Breathing: Add scale animation to chest (0.95 → 1.05, loop, 3s)
- Blinking: Add animation to eyelid opacity
- Tail wave: Rotate tail with delayed loop animation

### Step 4: Export as Embed
1. Click "Share" button (top right)
2. Select "Embed"
3. Copy the iframe embed code
4. Paste into the HTML template below

### Step 5: Update HTML
Replace the `<!-- SPLINE_EMBED_HERE -->` with your Spline iframe code

## Expected Results:
✨ Professional 3D otter
✨ Smooth 60fps WebGL rendering
✨ Interactive animation
✨ Realistic lighting and shadows
