# ZDI-26-194: Microsoft Exchange InterceptorSmtpAgent Improper Input Validation Security Feature Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-194
- **ZDI-CAN:** ZDI-CAN-28462
- **Date:** 2026-03-16
- **CVE:** CVE-2026-21527
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Vladislav Berghici of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-194/
## Vulnerability Details

This vulnerability allows remote attackers to bypass a security feature on affected installations of Microsoft Exchange. Authentication is not required to exploit this vulnerability. The specific flaw exists within the InterceptorSmtpAgent class. The issue results from the improper parsing of SMTP headers. An attacker can leverage this vulnerability to bypass a security feature offered by the product.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21527

## Disclosure Timeline

- 2025-11-14 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
