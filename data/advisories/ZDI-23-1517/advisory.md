# ZDI-23-1517: (0Day) D-Link DIR-X3260 Prog.cgi Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1517
- **ZDI-CAN:** ZDI-CAN-20774
- **Date:** 2023-10-04
- **CVE:** CVE-2023-44419
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-X3260
- **Credit:** Nicholas Zubrisky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1517/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-X3260 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the prog.cgi binary, which handles HNAP requests made to the lighttpd webserver. The issue results from the lack of proper validation of the length an user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

04/13/23 – ZDI reported the vulnerability to the vendor. 08/25/23 – ZDI asked for an update. 08/30/23 – The vendor states the fix is still under development. 09/29/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 10/04/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-04-13 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
