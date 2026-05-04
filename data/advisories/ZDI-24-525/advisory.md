# ZDI-24-525: A10 Thunder ADC Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-525
- **ZDI-CAN:** ZDI-CAN-22754
- **Date:** 2024-05-29
- **CVE:** CVE-2024-30369
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** A10
- **Affected Products:** Thunder ADC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-525/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of A10 Thunder ADC. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the installer. The issue results from incorrect permissions on a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

A10 has issued an update to correct this vulnerability. More details can be found at: https://support.a10networks.com/support/security_advisory/cve-2024-30368-cve-2024-30369

## Disclosure Timeline

- 2023-12-06 - Vulnerability reported to vendor
- 2024-05-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
