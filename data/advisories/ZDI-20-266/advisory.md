# ZDI-20-266: D-Link DAP-2610 Router login Incorrect Comparison Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-266
- **ZDI-CAN:** ZDI-CAN-10082
- **Date:** 2020-02-21
- **CVE:** CVE-2020-8862
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2610
- **Credit:** chung96vn - Security Researcher of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-266/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DAP-2610 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of passwords. The issue results from the lack of proper password checking. An attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10154

## Disclosure Timeline

- 2020-01-21 - Vulnerability reported to vendor
- 2020-02-21 - Coordinated public release of advisory
