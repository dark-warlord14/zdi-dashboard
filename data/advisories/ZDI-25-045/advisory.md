# ZDI-25-045: 7-Zip Mark-of-the-Web Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-045
- **ZDI-CAN:** ZDI-CAN-25456
- **Date:** 2025-01-19
- **CVE:** CVE-2025-0411
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** 7-Zip
- **Affected Products:** 7-Zip
- **Credit:** Peter Girnus - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-045/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Mark-of-the-Web protection mechanism on affected installations of 7-Zip. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of archived files. When extracting files from a crafted archive that bears the Mark-of-the-Web, 7-Zip does not propagate the Mark-of-the-Web to the extracted files. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

Fixed in 7-Zip version 24.09

## Disclosure Timeline

- 2024-10-01 - Vulnerability reported to vendor
- 2025-01-19 - Coordinated public release of advisory
- 2025-01-19 - Advisory Updated
