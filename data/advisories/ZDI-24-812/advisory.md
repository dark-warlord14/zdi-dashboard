# ZDI-24-812: Hewlett Packard Enterprise OneView Apache Server-Side Request Forgery Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-812
- **ZDI-CAN:** ZDI-CAN-22691
- **Date:** 2024-06-18
- **CVE:** CVE-2021-40438
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** OneView
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-812/
## Vulnerability Details

This vulnerability allows remote attackers to initiate arbitrary server-side requests on affected installations of Hewlett Packard Enterprise OneView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the REST service, which listens on TCP port 443 by default. The issue results from the use of a vulnerable Apache HTTP server. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04586en_us&docLocale=en_US

## Disclosure Timeline

- 2023-12-01 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
