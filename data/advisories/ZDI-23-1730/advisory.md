# ZDI-23-1730: Fuji Electric Tellus Lite Incorrect Default Permissions Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1730
- **ZDI-CAN:** ZDI-CAN-21224
- **Date:** 2023-11-27
- **CVE:** CVE-2023-5299
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Tellus Lite
- **Credit:** Fritz Sands
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1730/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Fuji Electric Tellus Lite. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions set on product folders created by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of any user of the software.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-325-02

## Disclosure Timeline

- 2023-06-07 - Vulnerability reported to vendor
- 2023-11-27 - Coordinated public release of advisory
