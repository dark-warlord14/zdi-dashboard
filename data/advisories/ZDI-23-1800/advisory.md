# ZDI-23-1800: Ivanti Avalanche EnterpriseServer Service Unrestricted File Upload Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1800
- **ZDI-CAN:** ZDI-CAN-21006
- **Date:** 2023-12-19
- **CVE:** CVE-2023-41725
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1800/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Ivanti Avalanche. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the saveConfig method. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://download.wavelink.com/Files/avalanche_v6.4.1.236_release_notes.txt

## Disclosure Timeline

- 2023-05-30 - Vulnerability reported to vendor
- 2023-12-19 - Coordinated public release of advisory
