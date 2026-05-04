# ZDI-25-252: (0Day) Cato Networks Cato Client for macOS Helper Service Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-252
- **ZDI-CAN:** ZDI-CAN-23275
- **Date:** 2025-04-23
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cato Networks
- **Affected Products:** Cato Client for macOS
- **Credit:** @patch1t
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-252/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Cato Networks Cato Client for macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Helper service. The issue results from the lack of proper locking when installing a package. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

04/17/24 – ZDI requested PSIRT contacts from the vendor 03/12/25 – ZDI reported the vulnerability to the vendor via https://vulnerabilityreport.catonetworks.com/ 04/15/25 – ZDI informed the vendor of the intention to publish the case as a zero-day advisory

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-04-23 - Coordinated public release of advisory
- 2025-04-24 - Advisory Updated
