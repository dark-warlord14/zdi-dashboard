# ZDI-20-268: D-Link Multiple Routers HNAP strncmp Incorrect Comparison Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-268
- **ZDI-CAN:** ZDI-CAN-9471
- **Date:** 2020-02-24
- **CVE:** CVE-2020-8864
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** Multiple Routers
- **Credit:** chung96vn - Security Researcher of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-268/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DIR-867, DIR-878, and DIR-882 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HNAP login requests. The issue results from the lack of proper handling of empty passwords. An attacker can leverage this vulnerability to execute arbitrary code on the router.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10157

## Disclosure Timeline

- 2019-12-27 - Vulnerability reported to vendor
- 2020-02-24 - Coordinated public release of advisory
