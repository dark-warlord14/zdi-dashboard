# ZDI-18-920: Crestron Multiple Products CTP Console Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-920
- **ZDI-CAN:** ZDI-CAN-6160
- **Date:** 2018-08-14
- **CVE:** CVE-2018-13341
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Crestron
- **Affected Products:** TSW-760
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-920/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of all Crestron products. Authentication is required to exploit this vulnerability. The specific flaw exists within the two built-in accounts on all Crestron devices. An attacker can leverage this vulnerability to execute arbitrary code under the context of Administrator.

## Additional Details

Crestron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-221-01

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
