# ZDI-11-072: Adobe Reader BMP ColorData Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-072
- **ZDI-CAN:** ZDI-CAN-947
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0599
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-072/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the Bitmap parsing component of rt3d.dll. When allocating a destination buffer for handling 4/8-bit RLE compressed bitmaps, the process uses the bitmap bits per pixel and number of colors values directly. A pointer is created based on the specified color depth, which can then be used to copy user supplied data into the fixed-length color data buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-03.html

## Disclosure Timeline

- 2010-11-15 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
