# ZDI-11-067: Adobe Acrobat Reader U3D Texture rgba RLE Decompression Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-067
- **ZDI-CAN:** ZDI-CAN-924
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0591
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-067/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's implementation of an image format supported by the Universal 3D compressed file format. When decoding the image data provided by the file, the application will one size for allocating space for the destination buffer and then trust the data when decompressing into that buffer. Due to the decompression being unbounded by the actual buffer size, a buffer overflow can be triggered leading to code execution under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-03.html

## Disclosure Timeline

- 2010-09-29 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
