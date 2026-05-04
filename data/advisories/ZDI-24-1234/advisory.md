# ZDI-24-1234: WinZip Mark-of-the-Web Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1234
- **ZDI-CAN:** ZDI-CAN-23983
- **Date:** 2024-09-17
- **CVE:** CVE-2024-8811
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WinZip Computing
- **Affected Products:** WinZip
- **Credit:** Peter Girnus (@gothburz) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1234/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Mark-of-the-Web protection mechanism on affected installations of WinZip. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of archive files. When opening an archive that bears the Mark-of-the-Web, WinZip removes the Mark-of-the-Web from the archive file. Following extraction, the extracted files also lack the Mark-of-the-Web. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

This vulnerability has been patched for the subscription and perpetual license versions listed below. * Subscription: 76.8 and later versions * Perpetual license versions: * 29.0 and later versions * 28.0.16371 and later versions * 27.0.16370 and later versions

## Disclosure Timeline

- 2024-05-03 - Vulnerability reported to vendor
- 2024-09-17 - Coordinated public release of advisory
- 2025-03-28 - Advisory Updated
