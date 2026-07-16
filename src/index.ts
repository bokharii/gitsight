import fs from 'node:fs/promises';
import path from 'node:path';

async function readDirectory(dirPath: string) {
  try {
    // Reads all file and folder names inside the directory
    const files = await fs.readdir(dirPath);
    
    files.forEach(file => {
      console.log(file);
    });
  } catch (error) {
    console.error('Error reading directory:', error);
  }
}

readDirectory('./');