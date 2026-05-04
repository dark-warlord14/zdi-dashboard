# ZDI-23-1802: Ivanti Avalanche Printer Device Service Missing Authentication Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1802
- **ZDI-CAN:** ZDI-CAN-19503
- **Date:** 2023-12-19
- **CVE:** CVE-2022-43555
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1802/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Ivanti Avalanche. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of Apache Derby, used by the Printer Device Service. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://download.wavelink.com/Files/avalanche_v6.4.1.236_release_notes.txt

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-12-19 - Coordinated public release of advisory
