# ZDI-26-185: Microsoft Windows GDI Bitmap Parsing Out-Of-Bound Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-185
- **ZDI-CAN:** ZDI-CAN-28271
- **Date:** 2026-03-10
- **CVE:** CVE-2026-25181
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-185/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. Interaction with the GDI library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of bitmap images. Crafted data in a bitmap header can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-25181

## Disclosure Timeline

- 2025-12-02 - Vulnerability reported to vendor
- 2026-03-10 - Coordinated public release of advisory
- 2026-03-10 - Advisory Updated
