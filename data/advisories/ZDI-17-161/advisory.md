# ZDI-17-161: Hewlett Packard Enterprise Intelligent Management Center UrlAccessController Filter Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-161
- **ZDI-CAN:** ZDI-CAN-4056
- **Date:** 2017-03-11
- **CVE:** CVE-2017-5791
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-161/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. The specific flaw exists within UrlAccessController. The doFilter method contains multiple ways to bypass authentication if the URI contains specific strings. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03716en_us

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2017-03-11 - Coordinated public release of advisory
