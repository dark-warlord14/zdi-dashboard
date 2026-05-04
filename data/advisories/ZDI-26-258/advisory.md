# ZDI-26-258: (0Day) Docker Desktop extension-manager Exposed Dangerous Function Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-258
- **ZDI-CAN:** ZDI-CAN-27229
- **Date:** 2026-04-15
- **CVE:** N/A
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Nitesh Surana (niteshsurana.com) of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-258/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop for Windows. An attacker must first obtain the ability to execute high-privileged code within the container in order to exploit this vulnerability. The specific flaw exists within the the implemention of the Docker Extensions functionality. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the current user

## Additional Details

06/04/25 - ZDI submitted the report to the vendor 06/23/25 - the vendor requested technical clarification 09/03/25 - ZDI provided additional details 09/12/25 - the vendor communicated that the attack scenario was outside their security threat model 09/23/25 - ZDI indicated that the reported issue was a bypass of a previously exploited incident 11/11/25 - The vendor rejected the report because the exploitation required prior privileged access 04/08/26 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-05-28 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
