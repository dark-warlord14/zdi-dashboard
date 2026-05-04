# ZDI-21-821: (Pwn2Own) Microsoft Exchange Server Autodiscover Server Side Request Forgery Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-821
- **ZDI-CAN:** ZDI-CAN-13611
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34473
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** orangetw
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-821/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Autodiscover service. The issue results from the lack of proper validation of URI prior to accessing resources. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473

## Disclosure Timeline

- 2021-04-06 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
