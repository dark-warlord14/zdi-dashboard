# ZDI-11-297: Adobe Reader U3D PCX Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-297
- **ZDI-CAN:** ZDI-CAN-1202
- **Date:** 2011-10-26
- **CVE:** CVE-2011-2437
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-297/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Adobe Image parsing library. When Adobe Reader tries to parse an .PCX image it creates a 32 bits loop counter based on the height and width of the image. It then enters a loop to copy data from the file in to a memory buffer, but the loop counter used in that function is only a 16 bit integer and as such can never reach the end of the loop when the max loop counter is bigger then 0xFFFF. Exploitation of this issue allows for remote code execution under the context of the user running the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
