# ZDI-24-038: D-Link DIR-X3260 prog.cgi SetWLanRadioSecurity Stack-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-038
- **ZDI-CAN:** ZDI-CAN-21595
- **Date:** 2024-01-11
- **CVE:** CVE-2023-51618
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-X3260
- **Credit:** Peter Girnus, Nicholas Zubrisky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-038/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-X3260 routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the prog.cgi binary, which handles HNAP requests made to the lighttpd webserver listening on TCP ports 80 and 443. The issue results from the lack of proper validation of a user-supplied string before copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10365

## Disclosure Timeline

- 2023-07-06 - Vulnerability reported to vendor
- 2024-01-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
