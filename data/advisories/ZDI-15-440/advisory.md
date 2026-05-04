# ZDI-15-440: GE MDS PulseNET Hidden Support Account Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-440
- **ZDI-CAN:** ZDI-CAN-2922
- **Date:** 2015-09-16
- **CVE:** CVE-2015-6456
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** GE
- **Affected Products:** MDS PulseNET
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-440/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE MDS PulseNET. Authentication is required to exploit this vulnerability but it can bypassed using static credentials. The specific flaw exists within the PulseNET web service. It contains a hidden support account, with static credentials, that gives full access. An attacker could leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-258-03

## Disclosure Timeline

- 2015-05-14 - Vulnerability reported to vendor
- 2015-09-16 - Coordinated public release of advisory
