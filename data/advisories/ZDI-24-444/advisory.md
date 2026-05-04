# ZDI-24-444: (0Day) D-Link DIR-2640 HTTP Referer Stack-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-444
- **ZDI-CAN:** ZDI-CAN-21853
- **Date:** 2024-05-24
- **CVE:** CVE-2024-5293
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2640
- **Credit:** Nicholas Zubrisky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-444/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-2640-US routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within prog.cgi, which handles HNAP requests made to the lighttpd webserver listening on TCP ports 80 and 443. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

08/09/23 – ZDI reported the vulnerability to the vendor 08/24/23 – The vendor communicated that the case would be fixed in Q4, 2023 release 05/01/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 05/14/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-08-09 - Vulnerability reported to vendor
- 2024-05-24 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
