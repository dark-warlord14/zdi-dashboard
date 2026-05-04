# ZDI-16-242: (0Day) Apple QuickTime Atom Processing Heap Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-242
- **ZDI-CAN:** ZDI-CAN-3402
- **Date:** 2016-04-14
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-242/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within atom processing. By providing an invalid index, an attacker can write data outside of an allocated heap buffer. An attacker could leverage this to execute arbitrary code under the context of the QuickTime player.

## Additional Details

This vulnerability is being disclosed publicly without a patch because vendor indicates that the product is deprecated. 11/11/2015 - ZDI reported 2 vulnerabilities to the vendor 11/11/2015 - The vendor acknowledged receipt of both reports 02/29/2016 - ZDI wrote to the vendor requesting a status update 03/08/2016 - The vendor replied, inviting ZDI to a call 03/09/2016 - ZDI joined a call with the vendor: ZDI was advised that the product would be deprecated on Windows and the vendor would publish removal instructions for users. ZDI advised the vendor that the cases would be 0-day. 03/24/2016 - ZDI notified the vendor of the intent to 0-day on or after 4/13 04/01/2016 - The vendor acknowledged and provided a link to their removal instructions Vendor Response: https://support.apple.com/HT205771

## Disclosure Timeline

- 2015-11-11 - Vulnerability reported to vendor
- 2016-04-14 - Coordinated public release of advisory
