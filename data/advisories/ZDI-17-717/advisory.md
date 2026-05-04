# ZDI-17-717: Bitdefender Internet Security PDF Predictor Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-717
- **ZDI-CAN:** ZDI-CAN-4361
- **Date:** 2017-09-06
- **CVE:** CVE-2017-10954
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Bitdefender
- **Affected Products:** Internet Security
- **Credit:** Pagefault
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-717/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within pdf.xmd. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

The fix is in build version: 7.72918 and higher.

## Disclosure Timeline

- 2017-08-23 - Vulnerability reported to vendor
- 2017-09-06 - Coordinated public release of advisory
