# ZDI-13-204: Hewlett-Packard System Management iprange Parameter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-204
- **ZDI-CAN:** ZDI-CAN-1676
- **Date:** 2013-08-13
- **CVE:** CVE-2013-2362
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** System Management
- **Credit:** agix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-204/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP System Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the iprange parameter when passed to /proxy/DataValidation in an HTTP request. Overflowing this parameter with data will cause a stack buffer overflow. An attacker can exploit this condition to gain remote code execution as SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03839862

## Disclosure Timeline

- 2013-01-08 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
