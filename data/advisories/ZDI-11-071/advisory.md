# ZDI-11-071: Adobe Reader BMP RLE_8 Decompression Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-071
- **ZDI-CAN:** ZDI-CAN-972
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0596
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-071/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the Bitmap parsing component of 2d.dll. When allocating a destination buffer for handling RLE_8 compressed bitmaps the process uses the bitmap height and width values directly. Certain assumptions are made regarding minimum values of these fields during decompression resulting in a copy user supplied data into a fixed-length buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-03.html

## Disclosure Timeline

- 2010-11-05 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
