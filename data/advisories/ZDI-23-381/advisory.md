# ZDI-23-381: Microsoft Windows Remote Desktop Connection Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-381
- **ZDI-CAN:** ZDI-CAN-19598
- **Date:** 2023-04-11
- **CVE:** CVE-2023-28267
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Team BT5 (BoB 11th)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-381/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must open a remote desktop session to a host that has been compromised or otherwise under control of an attacker. The specific flaw exists within the Remote Desktop client. A crafted audio packet can trigger access to memory prior to initialization. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the Remote Desktop client process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28267

## Disclosure Timeline

- 2023-01-10 - Vulnerability reported to vendor
- 2023-04-11 - Coordinated public release of advisory
