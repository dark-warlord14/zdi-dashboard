# ZDI-11-300: Adobe Reader U3D PICT 10h Encoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-300
- **ZDI-CAN:** ZDI-CAN-1198
- **Date:** 2011-10-26
- **CVE:** CVE-2011-2433
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-300/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Adobe handles PICT images. When Adobe parses a PICT image containing an 0x10 opcode the following word in the file will be interpreted as a loop counter that copies data from the file into a heap buffer that has been created using the height and with of the picture. The resulting heap overflow can result in remote code execution under the rights of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
