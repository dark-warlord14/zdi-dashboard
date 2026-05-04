# ZDI-11-077: Adobe Acrobat Reader U3D Texture Parser ILBM Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-077
- **ZDI-CAN:** ZDI-CAN-897
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0590
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's implementation of an image format supported by the Universal 3D compressed file format. When parsing a particular texture file specified by the format, the application will explicitly trust fields within the file in a multiply used to allocate space for the image data. Due to the application not accommodating for the result being larger than the architecture is able to store, the application will under allocate a buffer. When writing image data to this buffer the application will write outside the boundary of the allocation. This can lead to code execution under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-03.html

## Disclosure Timeline

- 2010-09-22 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
