# ZDI-25-060: Google Chrome AI Manager Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-060
- **ZDI-CAN:** ZDI-CAN-25396
- **Date:** 2025-01-30
- **CVE:** CVE-2024-9954
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-060/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of Mojo messages. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current user at medium integrity.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2024/10/stable-channel-update-for-desktop_15.html

## Disclosure Timeline

- 2024-09-25 - Vulnerability reported to vendor
- 2025-01-30 - Coordinated public release of advisory
- 2025-01-30 - Advisory Updated
