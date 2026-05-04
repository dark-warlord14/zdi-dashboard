# ZDI-14-120: (Pwn2Own\Pwn4Fun) Apple OS X IOKit Kernel Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-120
- **ZDI-CAN:** ZDI-CAN-2207
- **Date:** 2014-05-02
- **CVE:** CVE-2014-1320
- **CVSS:** 2.1
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Ian Beer of Google Project Zero
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-120/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within IOKit. The issue lies in the storage of kernel pointers in an object's data structure that could be retrieved from userland. An attacker can leverage this vulnerability to leak kernel pointers.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT6207

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-05-02 - Coordinated public release of advisory
