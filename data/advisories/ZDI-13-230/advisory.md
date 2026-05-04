# ZDI-13-230: Adobe Reader U3D PCX Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-230
- **ZDI-CAN:** ZDI-CAN-1931
- **Date:** 2013-09-11
- **CVE:** CVE-2013-3358
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** vulnazoid
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-230/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the improper bounds checking of a U3D PCX external texture. The application performs insufficient bounds checking on user supplied data passed in which results in a heap buffer overflow. An attacker can leverage this situation to execute code under the context of the user running the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://www.adobe.com/support/security/bulletins/apsb13-22.html

## Disclosure Timeline

- 2013-07-30 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
