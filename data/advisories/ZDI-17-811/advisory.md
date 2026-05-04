# ZDI-17-811: EMC Data Protection Advisor Application Service Static Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-811
- **ZDI-CAN:** ZDI-CAN-4699
- **Date:** 2017-09-15
- **CVE:** CVE-2017-8013
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** EMC
- **Affected Products:** Data Protection Advisor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-811/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of EMC Data Protection Advisor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the EMC DPA Application service, which listens on TCP port 9002 by default. The issue results from hard-coded hidden user entries within the application database. An attacker can leverage this vulnerability to bypass authentication under the context of the Administrator.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/fulldisclosure/2017/Sep/36

## Disclosure Timeline

- 2017-04-12 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
