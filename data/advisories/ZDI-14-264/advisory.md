# ZDI-14-264: (0Day) Apple QuickTime 'mvhd' Atom Heap Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-264
- **ZDI-CAN:** ZDI-CAN-2082
- **Date:** 2014-07-23
- **CVE:** CVE-2014-4979
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-264/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the 'mvhd' atom. By providing a malformed version and flags, an attacker is able to create controllable memory corruption, and trigger an arbitrary write operation. By exploiting this, an attacker could execute code in the context of the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. 12/20/2013 - Disclosed to vendor 12/20/2013 - acknowledgement from vendor 05/30/2014 - Reminded vendor of 180-day deadline, 06/18/2014 05/30/2014 - Vendor advised update scheduled for 09/2014 07/23/2014 - Public release of advisory -- Vendor Mitigation: The vendor did not provide any mitigations. -- Mitigation: Given the stated purpose of QuickTime, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application to trusted media files.

## Disclosure Timeline

- 2014-02-18 - Vulnerability reported to vendor
- 2014-07-23 - Coordinated public release of advisory
