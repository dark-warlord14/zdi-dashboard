# ZDI-10-079: Realnetworks Helix Server NTLM Authentication Invalid Base64 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-079
- **ZDI-CAN:** ZDI-CAN-507
- **Date:** 2010-04-28
- **CVE:** CVE-2010-1317
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** Helix Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-079/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Helix Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authentication provided by the administrative web interface and is only present if it is configured to use NTLM. The vulnerability can be triggered by specifying invalid Base64 string within the Authorization header. If the string is not proper Base64 the vulnerable function returns -1 which is not verified and is later used as a length to a string copy routine.

## Additional Details

This issue has been addressed in v14: http://www.realnetworks.com/uploadedFiles/Support/helix-support/SecurityUpdate041410HS.pdf

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-04-28 - Coordinated public release of advisory
