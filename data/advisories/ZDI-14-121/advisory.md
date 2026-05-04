# ZDI-14-121: (Pwn2Own\Pwn4Fun) Apple OS X Graphics Driver Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-121
- **ZDI-CAN:** ZDI-CAN-2208
- **Date:** 2014-05-02
- **CVE:** CVE-2014-1318
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Ian Beer of Google Project Zero
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-121/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Intel graphics driver. The issue lies in the failure to properly validate a pointer. An attacker can leverage this vulnerability to execute code within the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT6207

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-05-02 - Coordinated public release of advisory
