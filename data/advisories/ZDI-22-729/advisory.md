# ZDI-22-729: Microsoft Windows Active Directory Certificate Services Improper Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-729
- **ZDI-CAN:** ZDI-CAN-16168
- **Date:** 2022-05-10
- **CVE:** CVE-2022-26923
- **CVSS:** 9.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Oliver Lyak (@ly4k_) of Institut For Cyber Risk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-729/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to escalate privileges on affected installations of Microsoft Windows Active Directory Certificate Services. Authentication is required to exploit this vulnerability. The specific flaw exists within the issuance of certificates. By including crafted data in a certificate request, an attacker can obtain a certificate that allows the attacker to authenticate to a domain controller with a high level of privilege. An attacker can leverage this vulnerability to escalate privileges and disclose stored credentials, leading to further compromise.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26923

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-05-10 - Coordinated public release of advisory
