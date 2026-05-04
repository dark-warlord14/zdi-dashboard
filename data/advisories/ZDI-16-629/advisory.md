# ZDI-16-629: Advantech SUSIAccess Server Static Encryption Key Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-629
- **ZDI-CAN:** ZDI-CAN-3987
- **Date:** 2016-12-13
- **CVE:** CVE-2016-9353
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** SUSIAccess Server
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-629/
## Vulnerability Details

This vulnerability allows attackers to escalate privileges on vulnerable installations of Advantech SUSIAccess Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within encryption and storage of the administrator password. The password is stored in a known location and is encrypted with a static encryption key. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-336-04

## Disclosure Timeline

- 2016-08-30 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
