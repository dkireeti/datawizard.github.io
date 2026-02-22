#!/usr/bin/env python3
"""
Remove white background from images and convert to PNG with transparency.

This script processes images to remove white/near-white backgrounds,
converting them to transparent backgrounds for better theme compatibility.

Usage:
    python3 remove_bg.py
    
    Or with custom paths:
    python3 remove_bg.py --input-dir assets/images --output-dir assets/images
"""

from PIL import Image
import os
from pathlib import Path
import argparse


def remove_white_background(input_path, output_path, threshold=240):
    """
    Remove white/near-white background and make it transparent.
    
    Args:
        input_path (str): Path to input image file
        output_path (str): Path to save output image (will be PNG)
        threshold (int): RGB threshold for white detection (0-255)
                        Pixels with R,G,B > threshold are made transparent
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        img = Image.open(input_path)
        
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Get image data
        data = img.getdata()
        
        # Create new data with transparent background
        # Convert white and near-white pixels to transparent
        new_data = []
        for r, g, b, a in data:
            # If pixel is close to white (RGB values > threshold), make it transparent
            if r > threshold and g > threshold and b > threshold:
                new_data.append((r, g, b, 0))
            else:
                new_data.append((r, g, b, a))
        
        img.putdata(new_data)
        img.save(output_path, 'PNG')
        return True
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False


def process_images(input_dir, output_dir, extensions=['.png', '.jpg', '.jpeg', '.bmp'], threshold=240):
    """
    Process all images in a directory to remove white backgrounds.
    
    Args:
        input_dir (str): Directory containing images to process
        output_dir (str): Directory to save processed images
        extensions (list): Image file extensions to process
        threshold (int): RGB threshold for white detection
    
    Returns:
        dict: Statistics about processing (processed, failed, skipped)
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    stats = {'processed': 0, 'failed': 0, 'skipped': 0}
    
    # Find all image files
    image_files = []
    for ext in extensions:
        image_files.extend(input_path.glob(f'*{ext}'))
        image_files.extend(input_path.glob(f'*{ext.upper()}'))
    
    if not image_files:
        print(f"No images found in {input_dir}")
        return stats
    
    print(f"Found {len(image_files)} image(s) to process\n")
    
    for img_file in image_files:
        filename = img_file.name
        # Save all as PNG in output directory
        output_filename = img_file.stem + '.png'
        output_file = output_path / output_filename
        
        print(f"Processing: {filename}...", end=' ')
        
        if remove_white_background(str(img_file), str(output_file), threshold):
            print(f"✓ Saved to: {output_file}")
            stats['processed'] += 1
        else:
            print(f"✗ Failed")
            stats['failed'] += 1
    
    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Remove white background from images and convert to transparent PNG'
    )
    parser.add_argument(
        '--input-dir',
        default='assets/images',
        help='Directory containing images to process (default: assets/images)'
    )
    parser.add_argument(
        '--output-dir',
        default='assets/images',
        help='Directory to save processed images (default: assets/images)'
    )
    parser.add_argument(
        '--threshold',
        type=int,
        default=240,
        help='RGB threshold for white detection (0-255, default: 240)'
    )
    parser.add_argument(
        '--extensions',
        nargs='+',
        default=['.png', '.jpg', '.jpeg', '.bmp'],
        help='Image file extensions to process (default: .png .jpg .jpeg .bmp)'
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Image Background Remover")
    print("=" * 60)
    print(f"Input directory:  {args.input_dir}")
    print(f"Output directory: {args.output_dir}")
    print(f"Threshold:        {args.threshold}")
    print(f"Extensions:       {', '.join(args.extensions)}")
    print("=" * 60 + "\n")
    
    stats = process_images(
        args.input_dir,
        args.output_dir,
        extensions=args.extensions,
        threshold=args.threshold
    )
    
    print("\n" + "=" * 60)
    print("Processing Summary")
    print("=" * 60)
    print(f"Processed: {stats['processed']}")
    print(f"Failed:    {stats['failed']}")
    print(f"Skipped:   {stats['skipped']}")
    print("=" * 60)


if __name__ == '__main__':
    main()
