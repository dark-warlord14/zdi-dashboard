# ZDI-22-1608: (Pwn2Own) Microsoft Teams URL Allowlist Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1608
- **ZDI-CAN:** ZDI-CAN-17397
- **Date:** 2022-11-21
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Team DoubleDragon: Yonghwi Jin (@jinmo123) of Theori, Yongjin Kim (@adm1nkyj1) of Enki
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1608/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Teams. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the enforcement of the allowlist for domains. The issue lies in improper verification of approved subdomains for content delivery. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Fixed on August 31, 2022 https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
