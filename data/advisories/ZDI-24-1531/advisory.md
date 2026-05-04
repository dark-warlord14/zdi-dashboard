# ZDI-24-1531: RSA Security SecureID Software Token for Microsoft Windows Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1531
- **ZDI-CAN:** ZDI-CAN-21830
- **Date:** 2024-11-19
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** RSA Security
- **Affected Products:** SecureID Software Token for Microsoft Windows
- **Credit:** Sean de Regge
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1531/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of RSA Security SecureID Software Token for Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the Token Client. The process loads a DLL from an unsecured location. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Fixed in SecurID Authenticator 6.1.3 and later versions https://community.rsa.com/s/article/RSA-SecurID-Authenticator-6-1-3-for-Windows-Release-Notes

## Disclosure Timeline

- 2023-10-19 - Vulnerability reported to vendor
- 2024-11-19 - Coordinated public release of advisory
- 2024-11-19 - Advisory Updated
