# ZDI-21-571: Microsoft Windows WalletService Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-571
- **ZDI-CAN:** ZDI-CAN-12792
- **Date:** 2021-05-13
- **CVE:** CVE-2021-31187
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea (@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-571/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within WalletService. By creating a directory junction, an attacker can abuse the service to create a file in an arbitrary location. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31187

## Disclosure Timeline

- 2021-01-29 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
