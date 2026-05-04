# ZDI-23-1799: Ivanti Avalanche Incorrect Default Permissions Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1799
- **ZDI-CAN:** ZDI-CAN-21231
- **Date:** 2023-12-15
- **CVE:** CVE-2023-41726
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1799/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Ivanti Avalanche. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions set on product folders created by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://download.wavelink.com/Files/avalanche_v6.4.1.236_release_notes.txt

## Disclosure Timeline

- 2023-06-07 - Vulnerability reported to vendor
- 2023-12-15 - Coordinated public release of advisory
