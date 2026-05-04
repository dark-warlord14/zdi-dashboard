# ZDI-24-978: Microsoft PC Manager Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-978
- **ZDI-CAN:** ZDI-CAN-22503
- **Date:** 2024-07-29
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** PC Manager
- **Credit:** Filip Dragovic (@filip_dragovic)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-978/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft PC Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the MSPC Manager Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-us/acknowledgement/online

## Disclosure Timeline

- 2023-12-22 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
