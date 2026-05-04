# ZDI-26-083: Microsoft Windows searchConnector-ms NTLM Response Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-083
- **ZDI-CAN:** ZDI-CAN-28491
- **Date:** 2026-02-12
- **CVE:** CVE-2026-21249
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Jonathan Lein of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-083/
## Vulnerability Details

This vulnerability allows remote attackers to disclose NTLM responses on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of searchConnector-ms files. The issue results from the lack of proper input validation. An attacker can leverage this vulnerability to disclose NTLM responses in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21249

## Disclosure Timeline

- 2025-11-07 - Vulnerability reported to vendor
- 2026-02-12 - Coordinated public release of advisory
- 2026-02-12 - Advisory Updated
