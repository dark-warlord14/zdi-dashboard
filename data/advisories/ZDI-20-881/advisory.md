# ZDI-20-881: D-Link Multiple Routers HNAP GetCAPTCHAsetting Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-881
- **ZDI-CAN:** ZDI-CAN-10835
- **Date:** 2020-07-20
- **CVE:** CVE-2020-15633
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** Multiple Routers
- **Credit:** chung96vn of Vietnam Cyber Security Center
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-881/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DIR-867, DIR-878, and DIR-882 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HNAP requests. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the router.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10186

## Disclosure Timeline

- 2020-07-02 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
