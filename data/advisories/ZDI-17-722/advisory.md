# ZDI-17-722: Hewlett Packard Enterprise Application Performance Management System Health Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-722
- **ZDI-CAN:** ZDI-CAN-4466
- **Date:** 2017-09-07
- **CVE:** CVE-2017-13983
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Application Performance Management System Health
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-722/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Hewlett Packard Enterprise Application Performance Management System Health. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the System Health service, which listens on TCP port 18080 by default. By submitting a crafted request, an attacker can bypass authentication to access the web application. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.hpe.com/km/KM02942065

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-09-07 - Coordinated public release of advisory
