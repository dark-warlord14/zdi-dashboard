# ZDI-16-244: Hewlett Packard Enterprise Vertica validateAdminConfig Remote Command Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-244
- **ZDI-CAN:** ZDI-CAN-3417
- **Date:** 2016-04-15
- **CVE:** CVE-2016-2002
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Vertica
- **Credit:** agix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-244/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Vertica. Authentication is not required to exploit this vulnerability. The specific flaw exists within the validateAdminConfig handler. By providing an mcPort parameter containing command injection, an attacker can execute arbitrary commands as root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c05085303

## Disclosure Timeline

- 2015-12-01 - Vulnerability reported to vendor
- 2016-04-15 - Coordinated public release of advisory
