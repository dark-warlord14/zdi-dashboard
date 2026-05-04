# ZDI-18-932: Crestron Multiple Products CTP Console Incorrect Default Permissions Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-932
- **ZDI-CAN:** ZDI-CAN-6173
- **Date:** 2018-08-14
- **CVE:** CVE-2018-10630
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Crestron
- **Affected Products:** MC3
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-932/
## Vulnerability Details

This vulnerability allows remote attackers to execute execute arbitrary code on vulnerable installations of Crestron products. Authentication is not required to exploit this vulnerability. The specific flaw exists due to authentication being disabled by default on all Crestron devices. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Crestron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-221-01

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
