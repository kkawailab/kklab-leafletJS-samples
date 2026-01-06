import puppeteer from 'puppeteer';
import { readdir } from 'fs/promises';
import { join, basename } from 'path';

const samplesDir = '../samples';
const screenshotsDir = '../screenshots';

async function takeScreenshots() {
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const files = await readdir(samplesDir);
    const htmlFiles = files.filter(f => f.endsWith('.html')).sort();

    console.log(`Found ${htmlFiles.length} HTML files to screenshot`);

    for (const file of htmlFiles) {
        const filePath = join(process.cwd(), samplesDir, file);
        const screenshotName = file.replace('.html', '.png');
        const screenshotPath = join(screenshotsDir, screenshotName);

        console.log(`Capturing: ${file}`);

        const page = await browser.newPage();
        await page.setViewport({ width: 1200, height: 800 });

        try {
            await page.goto(`file://${filePath}`, {
                waitUntil: 'networkidle0',
                timeout: 30000
            });
            // Wait for map tiles to load
            await new Promise(resolve => setTimeout(resolve, 2000));
            await page.screenshot({ path: screenshotPath, fullPage: false });
            console.log(`  -> Saved: ${screenshotName}`);
        } catch (error) {
            console.error(`  -> Error: ${error.message}`);
        }

        await page.close();
    }

    await browser.close();
    console.log('Done!');
}

takeScreenshots();
