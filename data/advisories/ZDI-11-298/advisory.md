# ZDI-11-298: Adobe Reader U3D IFF RGBA Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-298
- **ZDI-CAN:** ZDI-CAN-1201
- **Date:** 2011-10-26
- **CVE:** CVE-2011-2436
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-298/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Adobe Image parsing library. When Adobe Reader tries to parse an .IFF image. While it tries to copy the image data from the RGBA chunk insufficient boundary checks are performed on a row counter which could lead to a heap overflow. This could result in remote code execution with the rights of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-24.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
