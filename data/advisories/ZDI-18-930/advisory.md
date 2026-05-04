# ZDI-18-930: Crestron Multiple Products CTP Console LAUNCH Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-930
- **ZDI-CAN:** ZDI-CAN-6171
- **Date:** 2018-08-14
- **CVE:** CVE-2018-11229
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Crestron
- **Affected Products:** MC3
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-930/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary commands on vulnerable installations of Crestron Crestron's WindowCE-based products. Authentication is required to exploit this vulnerability. The specific flaw exists within the engineer built-in account that enables a hidden 'LAUNCH' command. An attacker can leverage this vulnerability to escape the CTP console's sandbox environment to execute commands with elevated privileges.

## Additional Details

Crestron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-221-01

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
