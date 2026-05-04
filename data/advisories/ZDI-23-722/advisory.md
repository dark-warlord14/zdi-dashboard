# ZDI-23-722: Microsoft Windows Active Directory Certificate Services Improper Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-722
- **ZDI-CAN:** ZDI-CAN-16184
- **Date:** 2023-05-24
- **CVE:** CVE-2022-34691
- **CVSS:** 8.4
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Oliver Lyak (@ly4k_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-722/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to escalate privileges on affected installations of Microsoft Windows Active Directory Certificate Services. Authentication is required to exploit this vulnerability. The specific flaw exists within the issuance of certificates. By including crafted data in a certificate request, an attacker can obtain a certificate that allows the attacker to authenticate to a domain controller with a high level of privilege. An attacker can leverage this vulnerability to escalate privileges and disclose stored credentials, leading to further compromise.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-34691

## Disclosure Timeline

- 2022-02-04 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory
